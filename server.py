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
# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gRPC.proto


class UserService(gRPC_pb2_grpc.UserServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateUser(self, request, context):

        return gRPC_pb2.CreateUserResponse()

    def GetUser(self, request, context):

        user_message = gRPC_pb2.UserMessage()
        user_message.ParseFromString(request.body)

        user = self.dataAdapter.loadUser(user_message.name, user_message.password)

        if user is None:
            return gRPC_pb2.GetUserResponse(status=Status.NOT_FOUND)
        elif user == -1:
            return gRPC_pb2.GetUserResponse(status=Status.DATABASE_ERROR)
        else:
            user_message = gRPC_pb2.UserMessage(
                ID=user.ID, 
                name=user.name, 
                password=user.password,
                content=user.content if user.content else ""
            )
            serialized_user = user_message.SerializeToString()
            return gRPC_pb2.GetUserResponse(status=Status.STATUS_OK, body=serialized_user)

    def UpdateUser(self, request, context):

        return gRPC_pb2.UpdateUserResponse()

    def DeleteUser(self, request, context):

        return gRPC_pb2.DeleteUserResponse()


class EventService(gRPC_pb2_grpc.EventServiceServicer):

    def __init__(self):
       self.dataAdapter = DataAdapter("backend/TwitterDeck.db")

    def CreateEvent(self, request, context):

        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(request.body)

        event = Event(ID=event_message.ID, location=event_message.location, time=event_message.time,
                      content=event_message.content, userID=event_message.userID)
        res_id = self.dataAdapter.saveEvent(event)
        event.ID = res_id

        if res_id == -1:
            return gRPC_pb2.CreateEventResponse(status=Status.DATABASE_ERROR)
        else:
            event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                                  content=event.content, userID=event.userID)
            serialized_event = event_message.SerializeToString()
            return gRPC_pb2.CreateEventResponse(status=Status.STATUS_OK, body=serialized_event)

    def GetEvent(self, request, context):

        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(request.body)

        event = self.dataAdapter.loadEvent(event_message.ID)

        if event is None:
            return gRPC_pb2.GetEventResponse(status=Status.NOT_FOUND)
        else:
            event_message = gRPC_pb2.EventMessage(ID=event.ID, location=event.location, time=event.time,
                                                  content=event.content, userID=event.userID)
            serialized_event = event_message.SerializeToString()
            return gRPC_pb2.GetEventResponse(status=Status.STATUS_OK, body=serialized_event)

    def GetEventByUser(self, request, context):
        user = pickle.loads(request.body)
        events = self.dataAdapter.loadEventByUser(user.ID)
        serialized_event_list = pickle.dumps(events)
        return gRPC_pb2.GetEventByUserResponse(status=Status.STATUS_OK, EventList=serialized_event_list)


    def UpdateEvent(self, request, context):

        event_message = gRPC_pb2.EventMessage()
        event_message.ParseFromString(request.body)

        event = Event(ID=event_message.ID, location=event_message.location, time=event_message.time,
                      content=event_message.content, userID=event_message.userID)
        result = self.dataAdapter.updateEvent(event)
        if result > 0:
            return gRPC_pb2.UpdateEventResponse(status=Status.STATUS_OK)
        elif result == 0:
            return gRPC_pb2.UpdateEventResponse(status=Status.NOT_FOUND)
        else:
            return gRPC_pb2.UpdateEventResponse(status=Status.DATABASE_ERROR)

    def DeleteEvent(self, request, context):
        return gRPC_pb2.DeleteEventResponse()


class QueryService(gRPC_pb2_grpc.QueryServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateQuery(self, request, context):

        query_message = gRPC_pb2.QueryMessage()
        query_message.ParseFromString(request.body)

        query = Query(ID=query_message.ID, content=query_message.content,
                      eventID=query_message.eventID)
        res_id = self.dataAdapter.saveQuery(query)
        query.ID = res_id

        if res_id == -1:
            return gRPC_pb2.CreateQueryResponse(status=Status.DATABASE_ERROR)
        else:
            query_message = gRPC_pb2.QueryMessage(ID=query.ID, content=query.content,
                                                  eventID=query.eventID)
            serialized_query = query_message.SerializeToString()
            return gRPC_pb2.CreateQueryResponse(status=Status.STATUS_OK, body=serialized_query)

    def GetQuery(self, request, context):

        query_message = gRPC_pb2.QueryMessage()
        query_message.ParseFromString(request.body)

        query = self.dataAdapter.loadQuery(query_message.ID)

        if query is None:
            return gRPC_pb2.GetQueryResponse(status=Status.NOT_FOUND)
        else:
            query_message = gRPC_pb2.QueryMessage(ID=query.ID, content=query.content,
                                                  eventID=query.eventID)
            serialized_query = query_message.SerializeToString()
            return gRPC_pb2.GetQueryResponse(status=Status.STATUS_OK, body=serialized_query)

    def GetQueryByEvent(self, request, context):
        event = pickle.loads(request.body)
        queries = self.dataAdapter.loadQueryByEvent(event.ID)
        serialized_query_list = pickle.dumps(queries)
        return gRPC_pb2.GetQueryByEventResponse(status=Status.STATUS_OK, QueryList=serialized_query_list)

    def UpdateQuery(self, request, context):
        # Implement the logic for updating a query here
        return gRPC_pb2.UpdateQueryResponse()

    def DeleteQuery(self, request, context):
        # Implement the logic for deleting a query here
        return gRPC_pb2.DeleteQueryResponse()

class TweetService(gRPC_pb2_grpc.TweetServiceServicer):

    def __init__(self):
       self.dataAdapter =  DataAdapter("backend/TwitterDeck.db")

    def CreateTweet(self, request, context):
        return gRPC_pb2.CreateTweetResponse()

    def GetTweet(self, request, context):
        return gRPC_pb2.GetTweetResponse()

    def UpdateTweet(self, request, context):
        return gRPC_pb2.UpdateTweetResponse()

    def DeleteTweet(self, request, context):
        return gRPC_pb2.DeleteTweetResponse()

    def GetTweetByQuery(self, request, context):
        query = pickle.loads(request.body)
        tweetIDs = self.dataAdapter.loadTweetIDByQuery(query.ID)
        tweets = []
        for tweetID in tweetIDs:
            tweet = self.dataAdapter.loadTweet(tweetID)
            tweets.append(tweet)
        serialized_tweet_list = pickle.dumps(tweets)
        return gRPC_pb2.GetTweetByQueryResponse(status=Status.STATUS_OK, TweetList=serialized_tweet_list)


    def SearchTweet(self, request, context):

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
            return gRPC_pb2.SearchTweetResponse(status=Status.DATABASE_ERROR)
        else:
            serialized_tweet_list = pickle.dumps(tweet_list)
            return gRPC_pb2.SearchTweetResponse(status=Status.STATUS_OK, TweetList=serialized_tweet_list)

def serve():
    # dataAdapter = DataAdapter("TwitterDeck.db")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    gRPC_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    gRPC_pb2_grpc.add_EventServiceServicer_to_server(EventService(), server)
    gRPC_pb2_grpc.add_QueryServiceServicer_to_server(QueryService(), server)
    gRPC_pb2_grpc.add_TweetServiceServicer_to_server(TweetService(), server)
    print("Listening to port 50051...")
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()