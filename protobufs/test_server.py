from concurrent import futures
import grpc
import CrisisDeck_pb2
import CrisisDeck_pb2_grpc
# from ..backend.User import User

class Server(CrisisDeck_pb2_grpc.CrisisDeckServicer):
    def CreateUser(self, request, context):
        print("Hello !")
        reply = CrisisDeck_pb2.User()
        reply.ID = 0
        reply.name = request.name
        reply.password = request.password
        reply.content = "Hello World"
        return reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    CrisisDeck_pb2_grpc.add_CrisisDeckServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()