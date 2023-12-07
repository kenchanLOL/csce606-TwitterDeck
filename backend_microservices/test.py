from MongoDataAdapter import MongoDataAdapter
from RedisDataAdapter import RedisDataAdapter
from bson.objectid import ObjectId
from models.ClientUser import ClientUser
from models.EventTemplate import EventTemplate
from models.Query import Query
from models.Tweet import Tweet
import requests
import json
from datetime import datetime

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
'''

# insert event
'''
url = "http://localhost:5050/events"
datetime_since = datetime(2014, 8, 20, 00, 00, 00, 0)
datetime_until = datetime(2020, 8, 30, 23, 30, 30, 0)

event_data = {
    "KeyWord": "test_event3",
    "UserID": "656e9c6ea29d9379a2190a14",
    "MediaType": "images",
    "Since": datetime_since.isoformat(),
    "Until": datetime_until.isoformat(),
    "Language": "EN",
    "Repost": True,
    "Latitude": 30.5,
    "Longitude": 135.2,
    "Radius": 10.3,
    "RadiusUnit": "km",
    "MinRetweet": 10,
    "MinFac": 20
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(event_data), headers=headers)
'''
# insert query

url = "http://localhost:5050/queries"

datetime_since = datetime(2014, 8, 24, 00, 00, 00, 0)
datetime_until = datetime(2020, 8, 26, 23, 30, 30, 0)

data = {
    "keyword": "test_query",
    "media_type": "",
    "time_since": datetime_since,
    "time_until": datetime_until,
    "language": "",
    "repost": False,
    "latitude": "",
    "longitude": "",
    "radius": "",
    "radius_unit": "",
    "min_retweet": 30,
    "min_fav": 40
}

data['time_since'] = data['time_since'].isoformat()
data['time_until'] = data['time_until'].isoformat()

query_data = {
    "QueryContent": json.dumps(data),
    "EventID": "6571012cf474e176329aa8b9"
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(query_data), headers=headers)

# update event
'''
url = "http://localhost:5050/events/6570eec0dcd4331788266eff"
datetime_since = datetime(2018, 8, 20, 00, 00, 00, 0)
datetime_until = datetime(2029, 8, 30, 23, 30, 30, 0)

event_data = {
    "ID": "6570eec0dcd4331788266eff",
    "KeyWord": "test_event1",
    "UserID": "656e9c6ea29d9379a2190a14",
    "MediaType": "images",
    "Since": datetime_since.isoformat(),
    "Until": datetime_until.isoformat(),
    "Language": "EN",
    "Repost": True,
    "Latitude": 30.5,
    "Longitude": 135.2,
    "Radius": 10.3,
    "RadiusUnit": "km",
    "MinRetweet": 10,
    "MinFac": 20
}
headers = {'Content-Type': 'application/json'}
response = requests.put(url, data=json.dumps(event_data), headers=headers)

'''

# update query
'''
url = "http://localhost:5050/queries/6570f258e54075dad3f6433a"

datetime_since = datetime(2018, 8, 24, 00, 00, 00, 0)
datetime_until = datetime(2019, 8, 26, 23, 30, 30, 0)

data = {
    "keyword": "test_query",
    "media_type": "",
    "time_since": datetime_since,
    "time_until": datetime_until,
    "language": "",
    "repost": False,
    "latitude": "",
    "longitude": "",
    "radius": "",
    "radius_unit": "",
    "min_retweet": 30,
    "min_fav": 40
}

data['time_since'] = data['time_since'].isoformat()
data['time_until'] = data['time_until'].isoformat()

query_data = {
    "ID": "6570f258e54075dad3f6433a",
    "QueryContent": json.dumps(data)
}

headers = {'Content-Type': 'application/json'}

response = requests.put(url, data=json.dumps(query_data), headers=headers)
'''

# read event by user
url = "http://localhost:5050/client_users/656e9c6ea29d9379a2190a14/events"

data = {
    "ID":"656e9c6ea29d9379a2190a14"
}

headers = {'Content-Type': 'application/json'}

response = requests.get(url, data=json.dumps(data), headers=headers)
if response.status_code == 201:
    events_data = json.loads(response.text)
    for event_dict in events_data:
        print(event_dict['ID'], event_dict['Keyword'])
print("Status Code:", response.status_code)

# read query by event
url = "http://localhost:5050/events/656d70945880ee0ddf97d865/queries"
data = {
    "ID":"656d70945880ee0ddf97d865"
}

headers = {'Content-Type': 'application/json'}

response = requests.get(url, data=json.dumps(data), headers=headers)
if response.status_code == 201:
    queries_data = json.loads(response.text)
    for query_dict in queries_data:
        print(query_dict['ID'], query_dict['QueryContent'])
print("Status Code:", response.status_code)
