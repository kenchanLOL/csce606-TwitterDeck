import grpc
from protobufs import gRPC_pb2
from protobufs import gRPC_pb2_grpc
from backend import Status
from backend.User import User
from backend.Event import Event
from backend.Query import Query
from backend.Tweet import Tweet
from backend.Tweet import Tweet
from protobufs import CrisisDeck_pb2, CrisisDeck_pb2_grpc
import pickle

def Login(name, password, userStub):
    user = User(name=name, password=password)
    user_message = gRPC_pb2.UserMessage(ID=user.ID, name=user.name, password=user.password, content=user.content)
    serialized_user = user_message.SerializeToString()

    response = userStub.GetUser(gRPC_pb2.GetUserRequest(status=Status.STATUS_OK, body=serialized_user))
    # print(response)
    if response.status == Status.STATUS_OK:
        user_message = gRPC_pb2.UserMessage()
        user_message.ParseFromString(response.body)
        user.ID = user_message.ID
        user.content = user_message.content
        return True, user
    else:
        print("not found")
        return False, None


def GetEventByUser(userID, eventStub):
    events = []
    user = User(ID=userID)
    serialized_user = pickle.dumps(user)
    response = eventStub.GetEventByUser(gRPC_pb2.GetEventByUserRequest(status=Status.STATUS_OK, body=serialized_user))
    if response.status == Status.STATUS_OK:
        events = pickle.loads(response.EventList)
        return events
    else:
        print("database error")
        return None


def CreateEvent(event, eventStub):
    event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                          content=event.content, userID=event.userID)
    serialized_event = event_message.SerializeToString()

    response = eventStub.CreateEvent(gRPC_pb2.CreateEventRequest(status=Status.STATUS_OK, body=serialized_event))

    if response.status == Status.STATUS_OK:
        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(response.body)
        res_event = Event(ID=event_message.ID, location=event_message.location, time=event_message.time,
                          content=event_message.content, userID=event_message.userID)
        return res_event
    else:
        print("database error")
        return None


def LoadEvent(id, eventStub):
    event = Event(ID=id)
    event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                          content=event.content, userID=event.userID)
    serialized_event = event_message.SerializeToString()

    response = eventStub.GetEvent(gRPC_pb2.GetEventRequest(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(response.body)
        res_event = Event(ID=event_message.ID, location=event_message.location, time=event_message.time,
                          content=event_message.content, userID=event_message.userID)
        return res_event
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return None
    else:
        print("database error")
        return None


def UpdateEvent(event, eventStub):
    event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                          content=event.content, userID=event.userID)
    serialized_event = event_message.SerializeToString()

    response = eventStub.UpdateEvent(gRPC_pb2.UpdateEventRequest(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        print("updated")
        return 1
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return 0
    else:
        print("database error")
        return -1


def CreateQuery(query, queryStub):
    query = Query(content="injuries", eventID=10)
    query_message = gRPC_pb2.QueryMessage(ID=query.ID, content=query.content, eventID=query.eventID)
    serialized_query = query_message.SerializeToString()

    response = queryStub.CreateQuery(gRPC_pb2.CreateQueryRequest(status=Status.STATUS_OK, body=serialized_query))

    if response.status == Status.STATUS_OK:
        query_message = gRPC_pb2.QueryMessage()
        query_message.ParseFromString(response.body)
        res_query = Query(ID=query_message.ID, content=query_message.content, eventID=query_message.eventID)
        return res_query
    else:
        print("database error")
        return None


def LoadQuery(id, queryStub):
    query = Query(ID=49)
    query_message = gRPC_pb2.QueryMessage(ID=query.ID, content=query.content, eventID=query.eventID)
    serialized_query = query_message.SerializeToString()

    response = queryStub.GetQuery(gRPC_pb2.GetQueryRequest(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        query_message = gRPC_pb2.QueryMessage()
        query_message.ParseFromString(response.body)
        res_query = Query(ID=query_message.ID, content=query_message.content, eventID=query_message.eventID)
        return res_query
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return None
    else:
        print("database error")
        return None


def GetQueryByEvent(eventID, queryStub):
    event = User(ID=eventID)
    serialized_event = pickle.dumps(event)
    response = queryStub.GetQueryByEvent(gRPC_pb2.GetQueryByEventRequest(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        queries = pickle.loads(response.QueryList)
        return queries
    else:
        print("database error")
        return None


def GetTweetByQuery(queryID, tweetStub):
    query = Query(ID=queryID)
    serialized_query = pickle.dumps(query)
    response = tweetStub.GetTweetByQuery(
        gRPC_pb2.GetTweetByQueryRequest(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        tweets = pickle.loads(response.TweetList)
        return tweets
    else:
        print("database error")
        return None
# TODO: 
def searchTweet(event, query, tweetStub):
    query_message = gRPC_pb2.QueryMessage(ID=query.ID, content=query.content, eventID=query.eventID)
    serialized_query = query_message.SerializeToString()
    event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                          content=event.content, userID=event.userID)
    serialized_event = event_message.SerializeToString()
    response = tweetStub.SearchTweet(gRPC_pb2.SearchTweetRequest(status=Status.STATUS_OK, event=serialized_event,
                                                                 query=serialized_query))
    if response.status == Status.STATUS_OK:
        tweet_list = pickle.loads(response.TweetList)
        return tweet_list
    else:
        print("database error")
        return None
    

# def GetEventByID(eventID, stub):
#     if eventID == -1:
#         event = Event()
#     else:
#         eventID = CrisisDeck_pb2.EventID(ID = eventID)
#         reply = stub.GetEvent(eventID)
#         event = Event(reply.ID, reply.location, reply.time, reply.content)
#     return event
# /////////////////////////////////////////////////////
#  TODO:
# 0. New object design for event class
# 1. GetQueryByID
# Input: queryID
# Output: Event object (with customized filter) 
# 2. GetEventByID
# Input: eventID
# Output: Event object
# 3. searchTweet (Changes needed)
# Input: text, queryID
# Output: Tweet list
# 4. Create User
# Input: user object
# Output: user object
# 5. Update Event
# Input: config dict
# Output: Event object
# 6. Update Query
# Input: config dict
# Output: Event object
