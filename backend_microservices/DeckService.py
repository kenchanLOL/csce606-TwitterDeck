import json
import http.server
import socketserver
from MongoDataAdapter import MongoDataAdapter
from RedisDataAdapter import RedisDataAdapter


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
        return 0

    def handle_get_queries_by_event(self, path):
        return 0

    def handle_get_tweets_by_query(self, path):
        return 0

    def handle_login(self):
        return 0

    def handle_create_client_user(self):
        return 0

    def handle_create_event(self):
        return 0

    def handle_create_query(self):
        return 0

    def handle_update_event(self, path):
        return 0

    def handle_update_query(self, path):
        return 0


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