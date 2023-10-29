from concurrent import futures
import grpc
from protobufs import CrisisDeck_pb2_grpc, CrisisDeck_pb2
from backend.DataAdapter import DataAdapter
from backend.LoginControl import login
# from ..backend.User import User

class Server(CrisisDeck_pb2_grpc.CrisisDeckServicer):
    def __init__(self):
        super().__init__()
        self.dataAdapter = DataAdapter("backend/TwitterDeck.db")

    def CreateUser(self, request, context):
        print("Hello !")
        reply = CrisisDeck_pb2.User()
        reply.ID = 0
        reply.name = request.name
        reply.password = request.password
        reply.content = "Hello World"
        return reply

    def Login(self, request, context):
        user = login(request.name, request.password, self.dataAdapter)
        reply = CrisisDeck_pb2.User()
        if user != None:
            reply.ID = user.ID
            reply.name = user.name
            reply.password = user.password
            reply.content = user.content if user.content else ""
        return reply
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    CrisisDeck_pb2_grpc.add_CrisisDeckServicer_to_server(Server(), server)
    print("Listening to port 50051...")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    print("Initiating Server...")
    serve()