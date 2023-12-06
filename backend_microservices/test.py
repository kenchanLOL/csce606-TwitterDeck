from MongoDataAdapter import MongoDataAdapter
from RedisDataAdapter import RedisDataAdapter
from bson.objectid import ObjectId
from models.ClientUser import ClientUser
from models.EventTemplate import EventTemplate
from models.Query import Query
from models.Tweet import Tweet

'''
url = "mongodb+srv://xutianyi:nqw9TdLszitw28UR@cluster0.al3scwp.mongodb.net/"
mongoDataAdapter = MongoDataAdapter(url)
tweet = mongoDataAdapter.readTweet(503999388864114688)
tweet.rawContent = '121213'
tweet.id =503999388864114690
result = mongoDataAdapter.createTweet(tweet)
print(result)

mongoDataAdapter.close_connection()
'''

redisDataAdapter = RedisDataAdapter(host='redis-12311.c11.us-east-1-2.ec2.cloud.redislabs.com',
                                    port=12311,
                                    password='ff7O5S04jRHY1JXUYLzdbwsRGt1YiYc8')

result1 = redisDataAdapter.createQueryTweet('333', '1')
result2 = redisDataAdapter.createQueryTweet('333', '2')
print(result1, result2)
ids = redisDataAdapter.readQueryTweet('333')
print(ids)

redisDataAdapter.close_connection()
