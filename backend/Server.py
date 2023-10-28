from concurrent import futures
import grpc
import gRPC_pb2
import gRPC_pb2_grpc
import Status
from User import User
from DataAdapter import DataAdapter

# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gRPC.proto

class UserService(gRPC_pb2_grpc.UserServiceServicer):

    # def __init__(self, string):
    #    self.dataAdapter =  DataAdapter(string)

    def CreateUser(self, request, context):
        # 这里你可以实现创建用户的逻辑
        return gRPC_pb2.CreateUserResponse()

    def GetUser(self, request, context):
        # 这里你可以实现获取用户的逻辑
        dataAdapter = DataAdapter("TwitterDeck.db")

        user_message = gRPC_pb2.UserMessage()
        user_message.ParseFromString(request.body)

        res_user = dataAdapter.loadUser(user_message.name, user_message.password)

        if res_user is None:
            return gRPC_pb2.GetUserResponse(status=Status.NOT_FOUND)
        else:
            user_message = gRPC_pb2.UserMessage(ID=res_user.ID, name=res_user.name, password=res_user.password,
                                                content=res_user.content)
            serialized_user = user_message.SerializeToString()
            return gRPC_pb2.GetUserResponse(status=Status.STATUS_OK, body=serialized_user)

    def UpdateUser(self, request, context):
        # 这里你可以实现更新用户的逻辑
        return gRPC_pb2.UpdateUserResponse()

    def DeleteUser(self, request, context):
        # 这里你可以实现删除用户的逻辑
        return gRPC_pb2.DeleteUserResponse()

def serve():
    # dataAdapter = DataAdapter("TwitterDeck.db")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    gRPC_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()