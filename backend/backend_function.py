from backend.User import User
from backend.Event import Event


from protobufs import CrisisDeck_pb2, CrisisDeck_pb2_grpc
def Login(name, password, stub):
    name = name.strip()
    password = password.strip()

    user = CrisisDeck_pb2.User(ID = -1, name = name, password = password, content = "")
    reply = stub.GetUser(user)
    if reply.ID == 0:
        return False , None
    else:
        login_user = User(
            ID = reply.ID,
            name = reply.name,
            password = reply.password,
            content = reply.content
        )
        return True , login_user
    
def GetEventByUser(user, stub):
    userID = CrisisDeck_pb2.UserID(ID = user.ID)
    replies = stub.GetEventByUser(userID)
    events = []
    for reply in replies:
        event = Event(reply.ID, reply.location, reply.time, reply.content)
        events.append(event)
    return events
