import grpc
from protobufs import gRPC_pb2
from protobufs import gRPC_pb2_grpc
from backend import Status
from backend.User import User
from backend.Event import Event
from backend.Query import Query
from backend.Tweet import Tweet
import pickle
from backend import backend_function

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        userStub = gRPC_pb2_grpc.UserServiceStub(channel)
        eventStub = gRPC_pb2_grpc.EventServiceStub(channel)
        queryStub = gRPC_pb2_grpc.QueryServiceStub(channel)
        tweetStub = gRPC_pb2_grpc.TweetServiceStub(channel)
        '''
        result = backend_function.Login("admin", "password", userStub)
        print(result.ID)

        event1 = Event(location="Texas, USA", time="2022-12", content="Earthquake", userID=1)
        result = backend_function.CreateEvent(event1, eventStub)
        print(result.ID)

        event2 = backend_function.LoadEvent(3, eventStub)
        print(event2.ID, event2.location, event2.time, event2.userID, event2.content)

        event3 = Event(ID=15, location="Texas, USA", time="2018-12", content="Earthquake", userID=1)
        result = backend_function.UpdateEvent(event3, eventStub)
        print(result)

        query1 = Query(content="injuries", eventID=10)
        result = backend_function.CreateQuery(query1, queryStub)
        print(result.ID)

        query2 = backend_function.LoadQuery(49, queryStub)
        print(query2.ID, query2.content, query2.eventID)

        query3 = Query(ID=45, content="earthquake", eventID=6)
        event4 = Event(ID=6, location="Chile", time="2014-04", content="Earthquake", userID=1)
        results = backend_function.searchTweet(event4, query3, tweetStub)
        for result in results:
            print(result)
        '''
        events = backend_function.GetEventByUser(1, eventStub)
        for event in events:
            print(event.ID, event.content, event.location, event.time)

        queries = backend_function.GetQueryByEvent(3, queryStub)
        for query in queries:
            print(query.ID, query.content, query.eventID)

        tweets = backend_function.GetTweetByQuery(41, tweetStub)
        for tweet in tweets:
            print(tweet.ID, tweet.content)


        # 创建用户
        # response = stub.CreateUser(gRPC_pb2.CreateUserRequest())
        # 在这里处理response...

        # 获取用户
        '''
        user1 = User(name="admin", password="password")
        user_message = gRPC_pb2.UserMessage(ID=user1.ID, name=user1.name, password=user1.password, content=user1.content)
        serialized_user = user_message.SerializeToString()

        response = userStub.GetUser(gRPC_pb2.GetUserRequest(status=Status.STATUS_OK, body=serialized_user))

        if response.status == Status.STATUS_OK:
            user_message = gRPC_pb2.UserMessage()
            user_message.ParseFromString(response.body)
            print(user_message)
        else:
            print("incorrect name or password")
        '''

        # 更新用户
        # response = stub.UpdateUser(gRPC_pb2.UpdateUserRequest())
        # 在这里处理response...

        # 删除用户
        # response = stub.DeleteUser(gRPC_pb2.DeleteUserRequest())
        # 在这里处理response...

        # create event
        '''
        event1 = Event(location="Texas, USA", time="2020-12", content="Earthquake", userID=1)
        event_message = gRPC_pb2.EventMessage(ID=event1.ID, location=event1.location, time=event1.time,
                                              content=event1.content, userID=event1.userID)
        serialized_event = event_message.SerializeToString()

        response = eventStub.CreateEvent(gRPC_pb2.CreateEventRequest(status=Status.STATUS_OK, body=serialized_event))

        if response.status == Status.STATUS_OK:
            event_message = gRPC_pb2.EventMessage()
            event_message.ParseFromString(response.body)
            print(event_message)
        else:
            print("database error")
        '''

        # load event
        '''
        event2 = Event(ID=10)
        event_message = gRPC_pb2.EventMessage(ID=event2.ID, location=event2.location, time=event2.time,
                                              content=event2.content, userID=event2.userID)
        serialized_event = event_message.SerializeToString()

        response = eventStub.GetEvent(gRPC_pb2.GetEventRequest(status=Status.STATUS_OK, body=serialized_event))
        if response.status == Status.STATUS_OK:
            event_message = gRPC_pb2.EventMessage()
            event_message.ParseFromString(response.body)
            print(event_message)
        elif response.status == Status.NOT_FOUND:
            print("not found")
        else:
            print("database error")
        '''


        # update event
        '''
        event3 = Event(ID=10, location="Texas, USA", time="2021-12", content="Earthquake", userID=1)
        event_message = gRPC_pb2.EventMessage(ID=event3.ID, location=event3.location, time=event3.time,
                                              content=event3.content, userID=event3.userID)
        serialized_event = event_message.SerializeToString()

        response = eventStub.UpdateEvent(gRPC_pb2.UpdateEventRequest(status=Status.STATUS_OK, body=serialized_event))
        if response.status == Status.STATUS_OK:
            print("updated")
        elif response.status == Status.NOT_FOUND:
            print("not found")
        else:
            print("database error")
        '''

        # create query
        '''
        query1 = Query(content="injuries", eventID=10)
        query_message = gRPC_pb2.QueryMessage(ID=query1.ID, content=query1.content, eventID=query1.eventID)
        serialized_query = query_message.SerializeToString()

        response = queryStub.CreateQuery(gRPC_pb2.CreateQueryRequest(status=Status.STATUS_OK, body=serialized_query))

        if response.status == Status.STATUS_OK:
            query_message = gRPC_pb2.QueryMessage()
            query_message.ParseFromString(response.body)
            print(query_message)
        else:
            print("database error")
        '''

        # load query
        '''
        query2 = Query(ID=49)
        query_message = gRPC_pb2.QueryMessage(ID=query2.ID, content=query2.content, eventID=query2.eventID)
        serialized_query = query_message.SerializeToString()

        response = queryStub.GetQuery(gRPC_pb2.GetQueryRequest(status=Status.STATUS_OK, body=serialized_query))
        if response.status == Status.STATUS_OK:
            query_message = gRPC_pb2.QueryMessage()
            query_message.ParseFromString(response.body)
            print(query_message)
        elif response.status == Status.NOT_FOUND:
            print("not found")
        else:
            print("database error")

        tweetStub = gRPC_pb2_grpc.TweetServiceStub(channel)
        '''

        # search tweet
        '''
        query3 = Query(ID=45, content="earthquake", eventID=6)
        query_message = gRPC_pb2.QueryMessage(ID=query3.ID, content=query3.content, eventID=query3.eventID)
        serialized_query = query_message.SerializeToString()
        event4 = Event(ID=6, location="Chile", time="2014-04", content="Earthquake", userID=1)
        event_message = gRPC_pb2.EventMessage(ID=event4.ID, location=event4.location, time=event4.time,
                                              content=event4.content, userID=event4.userID)
        serialized_event = event_message.SerializeToString()
        response = tweetStub.SearchTweet(gRPC_pb2.SearchTweetRequest(status=Status.STATUS_OK, event=serialized_event,
                                                                     query=serialized_query))
        if response.status == Status.STATUS_OK:
            tweet_list = pickle.loads(response.TweetList)
            for tweet in tweet_list:
                print(tweet.ID, tweet.content)
        else:
            print("database error")
        '''


if __name__ == '__main__':
    run()