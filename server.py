from concurrent import futures
import pickle
import grpc
from protobufs import gRPC_pb2
from protobufs import gRPC_pb2_grpc
from backend import Status
from backend.DataAdapter import DataAdapter
from backend.User import User
from backend.Event import Event
from backend.Query import Query
from backend.Tweet import Tweet
import json
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gRPC.proto


class UserService(gRPC_pb2_grpc.UserServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateUser(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        user = pickle.loads(request.body)
        res_id = self.dataAdapter.saveUser(user)
        user.ID = res_id
        if res_id == -1:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)
        else:
            serialized_user = pickle.dumps(user)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_user)

    def GetUser(self, request, context):
        # 这里你可以实现获取用户的逻辑
        # dataAdapter = DataAdapter("TwitterDeck.db")
        user = pickle.loads(request.body)
        user = self.dataAdapter.loadUser(user.name, user.password)
        if user is None:
            return gRPC_pb2.Response(status=Status.NOT_FOUND)
        elif user == -1:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)
        else:
            serialized_user = pickle.dumps(user)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_user)

    def UpdateUser(self, request, context):

        return gRPC_pb2.Response()

    def DeleteUser(self, request, context):

        return gRPC_pb2.Response()


class EventService(gRPC_pb2_grpc.EventServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateEvent(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        event = pickle.loads(request.body)
        res_id = self.dataAdapter.saveEvent(event)
        event.ID = res_id
        if res_id == -1:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)
        else:
            serialized_event = pickle.dumps(event)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_event)

    def GetEvent(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        event = pickle.loads(request.body)
        event = self.dataAdapter.loadEvent(event.ID)
        if event is None:
            return gRPC_pb2.Response(status=Status.NOT_FOUND)
        else:
            serialized_event = pickle.dumps(event)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_event)

    def GetEventByUser(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        user = pickle.loads(request.body)
        events = self.dataAdapter.loadEventByUser(user.ID)
        serialized_event_list = pickle.dumps(events)
        return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_event_list)


    def UpdateEvent(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        event = pickle.loads(request.body)
        result = self.dataAdapter.updateEvent(event)
        if result > 0:
            return gRPC_pb2.Response(status=Status.STATUS_OK)
        elif result == 0:
            return gRPC_pb2.Response(status=Status.NOT_FOUND)
        else:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)

    def DeleteEvent(self, request, context):
        return gRPC_pb2.Response()


class QueryService(gRPC_pb2_grpc.QueryServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateQuery(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        query = pickle.loads(request.body)
        res_id = self.dataAdapter.saveQuery(query)
        query.ID = res_id

        if res_id == -1:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)
        else:
            serialized_query = pickle.dumps(query)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_query)

    def GetQuery(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        query = pickle.loads(request.body)
        query = self.dataAdapter.loadQuery(query.ID)
        event = self.dataAdapter.loadEvent(query.eventID)
        if query is None:
            return gRPC_pb2.Response(status=Status.NOT_FOUND)
        elif query.content is None:
            serialized_event = pickle.dumps(event)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_event)
        else:
            config = json.loads(query.content)
            # event = self.dataAdapter.loadEvent(query.eventID)
            event.since = config["time_since"]
            event.until = config["time_until"]
            event.repost=int(config["repost"])
            if config["keyword"] != "":
                event.keyword = config["keyword"]
            if config["media_type"] != "":
                event.mediaType = config["media_type"]
            if config["language"] != "":
                event.language = config["language"]
            if config["latitude"] != "":
                event.latitude = float(config["latitude"])
            if config["longitude"] != "":
                event.longitude = float(config["longitude"])
            if config["radius"] != "":
                event.radius = float(config["radius"])
            if config["radius_unit"] != "":
                event.radiusUnit = config["radius_unit"]
            if config["min_retweet"] != -1:
                event.minRetweet = config["min_retweet"]
            if config["min_fav"] != -1:
                event.minFav = config["min_fav"]
            serialized_event = pickle.dumps(event)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_event)

    def GetQueryByEvent(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        event = pickle.loads(request.body)
        queries = self.dataAdapter.loadQueryByEvent(event.ID)
        serialized_query_list = pickle.dumps(queries)
        return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_query_list)

    def UpdateQuery(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        query = pickle.loads(request.body)
        result = self.dataAdapter.updateQuery(query)
        if result > 0:
            return gRPC_pb2.Response(status=Status.STATUS_OK)
        elif result == 0:
            return gRPC_pb2.Response(status=Status.NOT_FOUND)
        else:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)

    def DeleteQuery(self, request, context):
        # Implement the logic for deleting a query here
        return gRPC_pb2.Response()

class TweetService(gRPC_pb2_grpc.TweetServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateTweet(self, request, context):
        return gRPC_pb2.Response()

    def GetTweet(self, request, context):
        return gRPC_pb2.Response()

    def UpdateTweet(self, request, context):
        return gRPC_pb2.Response()

    def DeleteTweet(self, request, context):
        return gRPC_pb2.Response()

    def GetTweetByQuery(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")
        query = pickle.loads(request.body)
        tweetIDs = self.dataAdapter.loadTweetIDByQuery(query.ID)
        tweets = []
        for tweetID in tweetIDs:
            tweet = self.dataAdapter.loadTweet(tweetID)
            tweets.append(tweet)
        serialized_tweet_list = pickle.dumps(tweets)
        return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_tweet_list)


    def SearchTweet(self, request, context):
        # dataAdapter = DataAdapter("TwitterDeck.db")

        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(request.event)
        query_message = gRPC_pb2.QueryMessage()
        query_message.ParseFromString(request.query)

        event = Event(ID=event_message.ID, location=event_message.location, time=event_message.time,
                      content=event_message.content, userID=event_message.userID)
        query = Query(ID=query_message.ID, content=query_message.content,
                      eventID=query_message.eventID)
        tweet_list = self.dataAdapter.searchTwitter(event, query)

        if tweet_list == -1:
            return gRPC_pb2.Response(status=Status.DATABASE_ERROR)
        else:
            serialized_tweet_list = pickle.dumps(tweet_list)
            return gRPC_pb2.Response(status=Status.STATUS_OK, body=serialized_tweet_list)

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    gRPC_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    gRPC_pb2_grpc.add_EventServiceServicer_to_server(EventService(), server)
    gRPC_pb2_grpc.add_QueryServiceServicer_to_server(QueryService(), server)
    gRPC_pb2_grpc.add_TweetServiceServicer_to_server(TweetService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print("listening on port 50051")
    serve()