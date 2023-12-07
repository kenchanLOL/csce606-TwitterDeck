import json
import http.server
import socketserver
from MongoDataAdapter import MongoDataAdapter
from RedisDataAdapter import RedisDataAdapter
from models.ClientUser import ClientUser
from models.EventTemplate import EventTemplate
from models.Query import Query
from models.Tweet import Tweet
from datetime import datetime

'''
login              POST /login
create Clientuser  POST /client_users  
get event by user  GET /client_users/{userId}/events
create event       POST /events
update event       PUT /events/{eventId}
get query by event GET /events/{eventId}/queries
create query       POST /queries
update query       PUT /queries/{queryId}
get tweet by query GET /queries/{queryId}/tweets
'''


class DeckService(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        url = "mongodb+srv://xutianyi:nqw9TdLszitw28UR@cluster0.al3scwp.mongodb.net/"
        self.mongoDataAdapter = MongoDataAdapter(url)
        self.redisDataAdapter = RedisDataAdapter(
            host='redis-12311.c11.us-east-1-2.ec2.cloud.redislabs.com',
            port=12311,
            password='ff7O5S04jRHY1JXUYLzdbwsRGt1YiYc8'
        )
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path_parts = self.path.split('/')

        if len(path_parts) < 2:
            self.send_error(404, "Not Found")
            return
        if path_parts[1] == "client_users" and len(path_parts) == 4 and path_parts[3] == "events":
            self.handle_get_events_by_client_user(path_parts[2])
        elif path_parts[1] == "events" and len(path_parts) == 4 and path_parts[3] == "queries":
            self.handle_get_queries_by_event(path_parts[2])
        elif path_parts[1] == "queries" and len(path_parts) == 4 and path_parts[3] == "tweets":
            self.handle_get_tweets_by_query(path_parts[2])
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        path_parts = self.path.split('/')

        if len(path_parts) < 2:
            self.send_error(404, "Not Found")
            return

        if self.path == "/login":
            self.handle_login()
        elif self.path == "/client_users":
            self.handle_create_client_user()
        elif self.path == "/events":
            self.handle_create_event()
        elif self.path == "/queries":
            self.handle_create_query()
        else:
            self.send_error(404, "Not Found")

    def do_PUT(self):
        path_parts = self.path.split('/')
        if len(path_parts) < 3:
            self.send_error(404, "Not Found")
            return

        if path_parts[1] == "events" and len(path_parts) == 3:
            self.handle_update_event(path_parts[2])
        elif path_parts[1] == "queries" and len(path_parts) == 3:
            self.handle_update_query(path_parts[2])
        else:
            self.send_error(404, "Not Found")

    def handle_get_events_by_client_user(self, path):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)

        ids = self.redisDataAdapter.readUserEvent(data.get('ID'))
        events = []
        for id in ids:
            event = self.mongoDataAdapter.readEventTemplate(id)
            if event == -1:
                self.send_error(500, "Internal Server Error")
            elif event is not None:
                events.append(event)
        events_dict = [event.to_dict() for event in events]
        if len(events_dict) > 0:
            json_data = json.dumps(events_dict)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_error(404, 'Record not found')

    def handle_get_queries_by_event(self, path):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)

        ids = self.redisDataAdapter.readEventQuery(data.get('ID'))
        print(ids)
        queries = []
        for id in ids:
            query = self.mongoDataAdapter.readQuery(id)
            if query == -1:
                self.send_error(500, "Internal Server Error")
            elif query is not None:
                queries.append(query)
        queries_dict = [query.to_dict() for query in queries]
        if len(queries_dict) > 0:
            json_data = json.dumps(queries_dict)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))
        else:
            self.send_error(404, 'Record not found')

    def handle_get_tweets_by_query(self, path):
        return 0

    def handle_login(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)

        result = self.mongoDataAdapter.readClientUser(data['UserName'], data['UserPassword'])

        if result == -1:
            self.send_error(500, "Internal Server Error")
        elif result is not None:
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'ID': result.ID, 'name':result.name, 'password':result.password}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(401, "Unauthorized")

    def handle_create_client_user(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)
        clientUser = ClientUser(name=data['UserName'], password=data['UserPassword'])

        result = self.mongoDataAdapter.createClientUser(clientUser)

        if result == -1:
            self.send_error(500, "Internal Server Error")
        else:
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'ID': result}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_create_event(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)
        event_template = EventTemplate(
            keyword=data.get('KeyWord'),
            userID=data.get('UserID'),
            mediaType=data.get('MediaType'),
            since=datetime.fromisoformat(data.get('Since')),
            until=datetime.fromisoformat(data.get('Until')),
            language=data.get('Language'),
            repost=data.get('Repost'),
            latitude=data.get('Latitude'),
            longitude=data.get('Longitude'),
            radius=data.get('Radius'),
            radiusUnit=data.get('RadiusUnit'),
            minRetweet=data.get('MinRetweet'),
            minFac=data.get('MinFac')
        )

        result = self.mongoDataAdapter.createEventTemplate(event_template)

        if result == -1:
            self.send_error(500, "Internal Server Error")
        else:
            self.redisDataAdapter.createUserEvent(data.get('UserID'), result)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'ID': result}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_create_query(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)
        query = Query(content=data.get('QueryContent'))

        result = self.mongoDataAdapter.createQuery(query)

        if result == -1:
            self.send_error(500, "Internal Server Error")
        else:
            self.redisDataAdapter.createEventQuery(data.get('EventID'), result)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'ID': result}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_update_event(self, path):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)
        event_template = EventTemplate(
            ID=data.get('ID'),
            keyword=data.get('KeyWord'),
            userID=data.get('UserID'),
            mediaType=data.get('MediaType'),
            since=datetime.fromisoformat(data.get('Since')),
            until=datetime.fromisoformat(data.get('Until')),
            language=data.get('Language'),
            repost=data.get('Repost'),
            latitude=data.get('Latitude'),
            longitude=data.get('Longitude'),
            radius=data.get('Radius'),
            radiusUnit=data.get('RadiusUnit'),
            minRetweet=data.get('MinRetweet'),
            minFac=data.get('MinFac')
        )

        result = self.mongoDataAdapter.updateEventTemplate(event_template)

        if result == -1:
            self.send_error(500, "Internal Server Error")
        elif result == 0:
            self.send_error(404, 'Record not found')
        else:
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

    def handle_update_query(self, path):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        data = json.loads(request_body)
        query = Query(ID=data.get('ID'), content=data.get('QueryContent'))

        result = self.mongoDataAdapter.updateQuery(query)

        if result == -1:
            self.send_error(500, "Internal Server Error")
        elif result == 0:
            self.send_error(404, 'Record not found')
        else:
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()


def register():
    print('register')


def run(server_class=socketserver.TCPServer, handler_class=DeckService, port=5050):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        register()
        print(f"Starting ProductInfo service at port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()