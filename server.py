from concurrent import futures
import grpc


from protobufs import CrisisDeck_pb2_grpc, CrisisDeck_pb2
from backend.DataAdapter import DataAdapter
from backend.User import User
from backend.Event import Event
from backend.Query import Query
from backend.Tweet import Tweet

# python -m grpc_tools.protoc -I.\protobufs\ --python_out=.\protobufs\ --grpc_python_out=.\protobufs\ .\protobufs\CrisisDeck.proto

class Server(CrisisDeck_pb2_grpc.ServiceServicer):
    def __init__(self):
        super().__init__()
        self.dataAdapter = DataAdapter("backend/TwitterDeck.db")

    def CreateUser(self, request, context):
        return CrisisDeck_pb2.User()

    def GetUser(self, request, context):
        # user = login(request.name, request.password, self.dataAdapter)
        # print(request)
        user = self.dataAdapter.loadUser(request.name, request.password)
        # print(user)
        reply = CrisisDeck_pb2.User()
        if user != None:
            reply.ID = user.ID
            reply.name = user.name
            reply.password = user.password
            reply.content = user.content if user.content else ""
        return reply
    
    def GetEventByUser(self, request, context):
        event_ls = self.dataAdapter.loadEventByUser(request.ID)
        for e in event_ls:
            event = CrisisDeck_pb2.Event()
            event.ID = e.ID
            event.location = e.location
            event.time = e.time
            event.content = e.content
            yield event
    
    def GetEvent(self, request, context):
        event = self.dataAdapter.loadEvent(request.ID)
        reply = CrisisDeck_pb2.Event()
        reply.ID = event.ID
        reply.location = event.location
        reply.time = event.time
        reply.content = event.content
        return reply
    
    def GetTweetsByEvent(self, request, context):
        tweet_dict = self.dataAdapter.loadTweetsByEventID(request.ID)
        # print(tweet_dict)
        for query_id, tweets in tweet_dict.items():
            for t in tweets:
                # print(query_id, t.ID)
                tweet = CrisisDeck_pb2.Tweet()
                tweet.ID = str(t.ID)
                tweet.location = t.location if t.location else ""
                tweet.time = t.time if t.time else ""
                tweet.content = t.content
                tweet.personID = t.personID if t.time else -1
                tweet.QueryID = query_id
                yield tweet        
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    CrisisDeck_pb2_grpc.add_ServiceServicer_to_server(Server(), server)
    print("Listening to port 50051...")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    print("Initiating Server...")
    serve()
