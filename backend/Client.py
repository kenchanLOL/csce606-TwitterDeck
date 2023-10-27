import grpc
import gRPC_pb2
import gRPC_pb2_grpc
import Status
from User import User


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gRPC_pb2_grpc.UserServiceStub(channel)

        # 创建用户
        # response = stub.CreateUser(gRPC_pb2.CreateUserRequest())
        # 在这里处理response...

        # 获取用户
        user1 = User(ID=0, name="admin", password="password", content="")
        user_message = gRPC_pb2.UserMessage(ID=user1.ID, name=user1.name, password=user1.password, content=user1.content)
        serialized_user = user_message.SerializeToString()

        response = stub.GetUser(gRPC_pb2.GetUserRequest(status=Status.STATUS_OK, body=serialized_user))

        if response.status == Status.STATUS_OK:
            user_message = gRPC_pb2.UserMessage()
            user_message.ParseFromString(response.body)
            print(user_message)
        else:
            print("incorrect name or password")

        # 更新用户
        # response = stub.UpdateUser(gRPC_pb2.UpdateUserRequest())
        # 在这里处理response...

        # 删除用户
        # response = stub.DeleteUser(gRPC_pb2.DeleteUserRequest())
        # 在这里处理response...


if __name__ == '__main__':
    run()