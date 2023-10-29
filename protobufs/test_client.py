import grpc
import CrisisDeck_pb2
import CrisisDeck_pb2_grpc
from ..backend.User import User


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = CrisisDeck_pb2_grpc.CrisisDeckStub(channel)
        user = CrisisDeck_pb2.User(
            ID = 0,
            name = "admin",
            password = "password",
            content = ""
        )
        reply = stub.CreateUser(user)
        print(reply)
if __name__ == '__main__':
    run()
