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
import json

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        userStub = gRPC_pb2_grpc.UserServiceStub(channel)
        eventStub = gRPC_pb2_grpc.EventServiceStub(channel)
        queryStub = gRPC_pb2_grpc.QueryServiceStub(channel)
        tweetStub = gRPC_pb2_grpc.TweetServiceStub(channel)

        #login
        result = backend_function.Login("admin", "password", userStub)
        print(result[1].ID)

        #create user
        user = User(name="12123", password="aaaa8888")
        result = backend_function.CreateUser(user, userStub)
        print(result.ID)

        '''
        #create event
        event1 = Event(keyword="111 Eearthquake", userID=1, mediaType='A', since='2004-05-04T17:00:00',
                       until='2004-05-04T17:02:00', language="English", repost=1, latitude=30.5, longitude=135.2,
                       radius=10.3, radiusUnit="km", minRetweet=10, minFac=20)
        result = backend_function.CreateEvent(event1, eventStub)
        id = result.ID
        print(result.ID)
        '''

        #load event
        event2 = backend_function.LoadEvent(26, eventStub)
        instance_attributes = vars(event2)
        for attribute in instance_attributes:
            print(f"{attribute}: {instance_attributes[attribute]}")

        #update event
        config={}
        config["keyword"] = "222 Volcano"
        config["media_type"] = "B"
        config["time_since"] = "2004-05-04T18:00:00"
        config["time_until"] = "2004-05-04T19:00:00"
        config["language"] = "Spanish"
        config["repost"] = False
        config["latitude"] = "10.5"
        config["longitude"] = "100.33"
        config["radius"] = "22.33"
        config["radius_unit"] = "miles"
        config["min_retweet"] = 2
        config["min_fav"] = 5
        result = backend_function.UpdateEvent(27, config, eventStub)
        print(result)

        #get event by user
        events = backend_function.GetEventByUser(1, eventStub)
        for event in events:
            instance_attributes = vars(event)
            for attribute in instance_attributes:
                print(f"{attribute}: {instance_attributes[attribute]}")

        '''
        # create query
        config={}
        config["keyword"] = "333 Volcano"
        config["media_type"] = "C"
        config["time_since"] = "2004-05-04T12:00:00"
        config["time_until"] = "2004-05-04T15:00:00"
        config["language"] = "Chinese"
        config["repost"] = False
        config["latitude"] = "20.5"
        config["longitude"] = "80.33"
        config["radius"] = "1221.33"
        config["radius_unit"] = "m"
        config["min_retweet"] = 20
        config["min_fav"] = 50
        config_str = json.dumps(config)
        query1 = Query(content=config_str, eventID=28)
        result = backend_function.CreateQuery(query1, queryStub)
        print(result.ID)
        '''

        # update query
        config={}
        config["keyword"] = "444 Volcano"
        config["media_type"] = ""
        config["time_since"] = "2004-05-04T10:00:00"
        config["time_until"] = "2004-05-04T13:00:00"
        config["language"] = "English"
        config["repost"] = True
        config["latitude"] = ""
        config["longitude"] = ""
        config["radius"] = ""
        config["radius_unit"] = ""
        config["min_retweet"] = 20
        config["min_fav"] = 50
        result = backend_function.UpdateQuery(57, config, queryStub)
        print(result)

        #get query by id
        event = backend_function.LoadQuery(57, queryStub)
        print(event)
        instance_attributes = vars(event)
        for attribute in instance_attributes:
            print(f"{attribute}: {instance_attributes[attribute]}")

        '''
        query3 = Query(ID=45, content="earthquake", eventID=6)
        event4 = Event(ID=6, location="Chile", time="2014-04", content="Earthquake", userID=1)
        results = backend_function.searchTweet(event4, query3, tweetStub)
        for result in results:
            print(result)

        queries = backend_function.GetQueryByEvent(3, queryStub)
        for query in queries:
            print(query.ID, query.content, query.eventID)

        tweets = backend_function.GetTweetByQuery(41, tweetStub)
        for tweet in tweets:
            print(tweet.ID, tweet.content)
        '''

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