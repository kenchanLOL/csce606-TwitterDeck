import redis
from backend.models.TweetInRedis import TweetInRedis

class RedisDataAdapter:
    def __init__(self, host, port, password, ssl=False, decode_responses=False):
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=ssl,
            decode_responses=decode_responses
        )

    def close_connection(self):
        self.redis_client.close()

    # Tweet CRUD
    def readTweet(self, tweetID):
        try:
            redis_key = "doc:tweets:" + tweetID
            if self.redis_client.exists(redis_key):
                result = self.redis_client.hgetall(redis_key)
                decoded_result = {}
                for key, value in result.items():
                    if key.decode('utf-8') != "content_vector":
                        decoded_result[key.decode('utf-8')] = value.decode('utf-8')
                tweetInRedis = TweetInRedis(ID=redis_key, tweetID=decoded_result["tweet_id"], content=decoded_result['content'], userID=decoded_result['user_id'])
                return tweetInRedis
            else:
                print('None')
                return None
        except Exception as e:
            print("DB error:", e)
            return -1

    def createTweet(self, TweetInRedis):
        try:
            tweet_id = TweetInRedis.ID
            key = 'doc:tweets:' + tweet_id
            if not self.redis_client.exists(key):
                self.redis_client.hset(key, 'id', tweet_id)
                self.redis_client.hset(key, 'content', TweetInRedis.content)
                self.redis_client.hset(key, 'user_id', TweetInRedis.userID)
                return tweet_id
            else:
                return 0
        except Exception as e:
            print("DB error:", e)
            return -1

    #User_Event CRUD
    def readUserEvent(self, UserID):
        try:
            key = "user:" + UserID
            event_ids = self.redis_client.smembers(key)
            event_ids = [event_id.decode('utf-8') for event_id in event_ids]
            return event_ids
        except Exception as e:
            print("DB error:", e)
            return -1

    def createUserEvent(self, UserID, EventID):
        try:
            key = "user:" + UserID
            self.redis_client.sadd(key, EventID)
            return 0
        except Exception as e:
            print("DB error:", e)
            return -1

    #Event_Query CRUD
    def readEventQuery(self, EventID):
        try:
            key = "event:" + EventID
            query_ids = self.redis_client.smembers(key)
            query_ids = [query_id.decode('utf-8') for query_id in query_ids]
            return query_ids
        except Exception as e:
            print("DB error:", e)
            return -1

    def createEventQuery(self, EventID, QueryID):
        try:
            key = "event:" + EventID
            self.redis_client.sadd(key, QueryID)
            return 0
        except Exception as e:
            print("DB error:", e)
            return -1

    #Query_Tweet CRUD
    def readQueryTweet(self, QueryID):
        try:
            key = "query:" +QueryID
            tweet_ids = self.redis_client.smembers(key)
            tweet_ids = [tweet_id.decode('utf-8') for tweet_id in tweet_ids]
            return tweet_ids
        except Exception as e:
            print("DB error:", e)
            return -1

    def createQueryTweet(self, QueryID, TweetIDs):
        try:
            key = "query:" + QueryID
            for id in TweetIDs:
                self.redis_client.sadd(key, id)
            return 0
        except Exception as e:
            print("DB error:", e)
            return -1

    def updateQueryTweet(self, QueryID, newTweetIDs):
        try:
            key = "query:" + QueryID

            # Remove the existing set of TweetIDs for this QueryID
            self.redis_client.delete(key)

            # Add the new set of TweetIDs
            for tweet_id in newTweetIDs:
                self.redis_client.sadd(key, tweet_id)

            return 0  # Indicate success
        except Exception as e:
            print("DB error:", e)
            return -1  # Indicate failure

