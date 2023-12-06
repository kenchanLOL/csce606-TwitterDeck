from pymongo import MongoClient
from bson.objectid import ObjectId
from models.ClientUser import ClientUser
from models.EventTemplate import EventTemplate
from models.Query import Query
from models.Tweet import Tweet


class MongoDataAdapter:
    def __init__(self, url):
        # url = "mongodb+srv://xutianyi:nqw9TdLszitw28UR@cluster0.al3scwp.mongodb.net/"
        self.client = MongoClient(url)
        self.db = self.client['TwitterDeck_db']
        self.Client_user_collection = self.db['Client_user']
        self.Tweet_user_collection = self.db['Tweet_user']
        self.Event_template_collection = self.db['Event_template']
        self.Query_collection = self.db['Query']
        self.Tweet_collection = self.db['Tweet']

    def close_connection(self):
        try:
            self.client.close()
            print("Database connection closed.")
        except Exception as e:
            print(f"Error closing database connection: {e}")

    # ClientUser CRUD
    def readClientUser(self, username, password):
        try:
            query = {"UserName": username, "UserPassword": password}
            result = self.Client_user_collection.find_one(query)
            if result is not None:
                clientUser = ClientUser(ID=str(result['_id']), name=result['UserName'], password=result['UserPassword'])
                return clientUser
            else:
                return None
        except Exception as e:
            print("DB error:", e)
            return -1

    def createClientUser(self, clientUser):
        try:
            data_to_insert = {"UserName": clientUser.name, "UserPassword": clientUser.password}
            result = self.Client_user_collection.insert_one(data_to_insert)
            return str(result.inserted_id)
        except Exception as e:
            print("DB error:", e)
            return -1

    # EventTemplate CRUD
    def readEventTemplate(self, id):
        try:
            event_id = ObjectId(id)
            result = self.Event_template_collection.find_one({"_id": event_id})
            if result is not None:
                eventTemplate = EventTemplate(ID=id, keyword=result['KeyWord'], mediaType=result['MediaType'],
                                              since=result['Since'], until=result['Until'], language=result['Language'],
                                              repost=result['Repost'], latitude=result['Latitude'],
                                              longitude=result['Longitude'], radius=result['Radius'],
                                              radiusUnit=result['RadiusUnit'], minRetweet=result['MinRetweet'],
                                              minFac=result['MinFac'], userID=result['UserID'])
                return eventTemplate
            else:
                return None
        except Exception as e:
            print("DB error:", e)
            return -1

    def createEventTemplate(self, eventTemplate):
        try:
            data_to_insert = {
                "KeyWord": eventTemplate.keyword,
                "UserID": eventTemplate.userID,
                "MediaType": eventTemplate.mediaType,
                "Since": eventTemplate.since,
                "Until": eventTemplate.until,
                "Language": eventTemplate.language,
                "Repost": eventTemplate.repost,
                "Latitude": eventTemplate.latitude,
                "Longitude": eventTemplate.longitude,
                "Radius": eventTemplate.radius,
                "RadiusUnit": eventTemplate.radiusUnit,
                "MinRetweet": eventTemplate.minRetweet,
                "MinFac": eventTemplate.minFac
            }
            result = self.Event_template_collection.insert_one(data_to_insert)
            return str(result.inserted_id)
        except Exception as e:
            print("DB error:", e)
            return -1

    def updateEventTemplate(self, eventTemplate):
        try:
            event_id = ObjectId(eventTemplate.ID)

            if self.Event_template_collection.count_documents({"_id": event_id}) == 0:
                print("No document found with the given ID")
                return 0

            data_to_update = {
                "$set": {
                    "KeyWord": eventTemplate.keyword,
                    "UserID": eventTemplate.userID,
                    "MediaType": eventTemplate.mediaType,
                    "Since": eventTemplate.since,
                    "Until": eventTemplate.until,
                    "Language": eventTemplate.language,
                    "Repost": eventTemplate.repost,
                    "Latitude": eventTemplate.latitude,
                    "Longitude": eventTemplate.longitude,
                    "Radius": eventTemplate.radius,
                    "RadiusUnit": eventTemplate.radiusUnit,
                    "MinRetweet": eventTemplate.minRetweet,
                    "MinFac": eventTemplate.minFac
                }
            }
            result = self.Event_template_collection.update_one({"_id": event_id}, data_to_update)
            return result.modified_count
        except Exception as e:
            print("DB error:", e)
            return -1

    # Query CRUD
    def readQuery(self, id):
        try:
            query_id = ObjectId(id)
            result = self.Query_collection.find_one({"_id": query_id})
            if result is not None:
                query = Query(ID=id, content=result['QueryContent'])
                return query
            else:
                return None
        except Exception as e:
            print("DB error:", e)
            return -1

    def createQuery(self, query):
        try:
            data_to_insert = {
                "QueryContent": query.content
            }
            result = self.Query_collection.insert_one(data_to_insert)
            return str(result.inserted_id)
        except Exception as e:
            print("DB error:", e)
            return -1

    def updateQuery(self, query):
        try:
            query_id = ObjectId(query.ID)
            if self.Query_collection.count_documents({"_id": query_id}) == 0:
                print("No document found with the given ID")
                return 0
            data_to_update = {
                "$set": {
                    "QueryContent": query.content
                }
            }
            result = self.Query_collection.update_one({"_id": query_id}, data_to_update)
            return result.modified_count
        except Exception as e:
            print("DB error:", e)
            return -1

    # Tweet CRUD
    def readTweet(self, id):
        try:
            result = self.Tweet_collection.find_one({"_id": id})
            if result is not None:
                tweet = Tweet(result)
                return tweet
            else:
                return None
        except Exception as e:
            print("DB error:", e)
            return -1

    def createTweet(self, tweet):
        try:
            if self.Tweet_collection.find_one({"_id": tweet.id}):
                print("Tweet already exists in the database.")
                return 0
            data_to_insert = {"_id": tweet.id,
                              "id_str": tweet.id_str,
                              "url": tweet.url,
                              "date": tweet.date,
                              "user": tweet.user,
                              "lang": tweet.lang,
                              "rawContent": tweet.rawContent,
                              "replyCount": tweet.replyCount,
                              "retweetCount": tweet.retweetCount,
                              "likeCount": tweet.likeCount,
                              "quoteCount": tweet.quoteCount,
                              "conversationId": tweet.conversationId,
                              "hashtags": tweet.hashtags,
                              "viewCount": tweet.viewCount,
                              "place": tweet.place,
                              "coordinates": tweet.coordinates}
            result = self.Tweet_collection.insert_one(data_to_insert)
            return result.inserted_id
        except Exception as e:
            print("DB error:", e)
            return -1

    # TweetUser CRUD
    # ...