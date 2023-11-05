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
import json

def Login(name, password, userStub):
    user = User(name=name, password=password)
    serialized_user = pickle.dumps(user)
    response = userStub.GetUser(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_user))
    # print(response)
    if response.status == Status.STATUS_OK:
        user = pickle.loads(response.body)
        return True, user
    else:
        print("not found")
        return False, None

def CreateUser(user, userStub):
    serialized_user = pickle.dumps(user)
    response = userStub.CreateUser(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_user))
    if response.status == Status.STATUS_OK:
        res_user = pickle.loads(response.body)
        return res_user
    else:
        print("database error")
        return None


def GetEventByUser(userID, eventStub):
    events = []
    user = User(ID=userID)
    serialized_user = pickle.dumps(user)
    response = eventStub.GetEventByUser(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_user))
    if response.status == Status.STATUS_OK:
        events = pickle.loads(response.body)
        return events
    else:
        print("database error")
        return None


def CreateEvent(event, eventStub):
    serialized_event = pickle.dumps(event)
    response = eventStub.CreateEvent(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        res_event = pickle.loads(response.body)
        return res_event
    else:
        print("database error")
        return None


def LoadEvent(id, eventStub):
    event = Event(ID=id)
    serialized_event = pickle.dumps(event)
    response = eventStub.GetEvent(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        res_event = pickle.loads(response.body)
        return res_event
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return None
    else:
        print("database error")
        return None


def UpdateEvent(id, config, eventStub):
    event = Event(ID=id, since=config["time_since"], until=config["time_until"], repost=int(config["repost"]))
    if config["keyword"] != "":
        event.keyword=config["keyword"]
    if config["media_type"] != "":
        event.mediaType=config["media_type"]
    if config["language"] != "":
        event.language=config["language"]
    if config["latitude"] != "":
        event.latitude=float(config["latitude"])
    if config["longitude"] != "":
        event.longitude=float(config["longitude"])
    if config["radius"] != "":
        event.radius=float(config["radius"])
    if config["radius_unit"] != "":
        event.radiusUnit=config["radius_unit"]
    if config["min_retweet"] != -1:
        event.minRetweet=config["min_retweet"]
    if config["min_fav"] != -1:
        event.minFac=config["min_fav"]
    serialized_event = pickle.dumps(event)
    response = eventStub.UpdateEvent(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_event))
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
    serialized_query = pickle.dumps(query)
    response = queryStub.CreateQuery(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        res_query = pickle.loads(response.body)
        return res_query
    else:
        print("database error")
        return None


def LoadQuery(id, queryStub):
    query = Query(ID=id)
    serialized_query = pickle.dumps(query)
    response = queryStub.GetQuery(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        res_query = pickle.loads(response.body)
        return res_query
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return None
    else:
        print("database error")
        return None


def UpdateQuery(id, config, queryStub):
    config_str = json.dumps(config)
    query = Query(ID=id, content=config_str)
    serialized_query = pickle.dumps(query)
    response = queryStub.UpdateQuery(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        print("updated")
        return 1
    elif response.status == Status.NOT_FOUND:
        print("not found")
        return 0
    else:
        print("database error")
        return -1



def GetQueryByEvent(eventID, queryStub):
    event = Event(ID=eventID)
    serialized_event = pickle.dumps(event)
    response = queryStub.GetQueryByEvent(gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_event))
    if response.status == Status.STATUS_OK:
        queries = pickle.loads(response.body)
        return queries
    else:
        print("database error")
        return None


def GetTweetByQuery(queryID, tweetStub):
    query = Query(ID=queryID)
    serialized_query = pickle.dumps(query)
    response = tweetStub.GetTweetByQuery(
        gRPC_pb2.Request(status=Status.STATUS_OK, body=serialized_query))
    if response.status == Status.STATUS_OK:
        tweets = pickle.loads(response.body)
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
        tweet_list = pickle.loads(response.body)
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
# √0. New object design for event class
# √1. GetQueryByID
# Input: queryID
# Output: Event object (with customized filter) 
# √2. GetEventByID
# Input: eventID
# Output: Event object
# 3. searchTweet (Changes needed)
# Input: text, queryID
# Output: Tweet list
# 4. Create User
# Input: user object
# Output: user object
# √5. Update Event
# Input: config dict
# Output: Event object
# √6. Update Query
# Input: config dict
# Output: Event object
