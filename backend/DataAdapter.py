import sqlite3
from backend.Event import Event
from backend.Tweet import Tweet
from backend.Query import Query
from backend.User import User
from datetime import datetime
import time

# dbname = 'TwitterDeck.db'
class DataAdapter:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def loadUser(self, username, password):
        try:
            sql_query = 'SELECT * FROM User WHERE UserName = ? AND UserPassword = ?'
            self.cursor.execute(sql_query, (username, password))
            result = self.cursor.fetchone()
            if result is not None:
                user = User(result[0], result[1], result[2], result[3])
                return user
            else:
                return None
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def saveUser(self, user):
        try:
            data_to_insert = (user.name, user.password)
            self.cursor.execute("INSERT INTO User (UserName, UserPassword) VALUES (?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def loadEvent(self, id):
        try:
            sql_query = 'SELECT * FROM DisasterEvent WHERE EventID = ?'
            self.cursor.execute(sql_query, (id, ))
            result = self.cursor.fetchone()
            last_inserted_id = self.cursor.lastrowid
            if result is not None:
                event = Event(ID=result[0], keyword=result[1], userID=result[2], mediaType=result[3], since=result[4],
                              until=result[5], language=result[6], repost=result[7], latitude=result[8],
                              longitude=result[9], radius=result[10], radiusUnit=result[11], minRetweet=result[12],
                              minFac=result[13])
                if result[4] is not None:
                    date_time_since = datetime.fromtimestamp(result[4])
                    event.since = date_time_since.strftime('%Y-%m-%dT%H:%M:%S')
                if result[5] is not None:
                    date_time_until = datetime.fromtimestamp(result[5])
                    event.until = date_time_until.strftime('%Y-%m-%dT%H:%M:%S')
                return event
            else:
                return None
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1
    
    def loadEventByUser(self, UserId):
        try:
            sql_query = 'SELECT * FROM DisasterEvent WHERE UserID = ?'
            self.cursor.execute(sql_query, (UserId, ))
            results = self.cursor.fetchall()
            events = []
            for result in results:
                event = Event(ID=result[0], keyword=result[1], userID=result[2], mediaType=result[3], since=result[4],
                              until=result[5], language=result[6], repost=result[7], latitude=result[8],
                              longitude=result[9], radius=result[10], radiusUnit=result[11], minRetweet=result[12],
                              minFac=result[13])
                if result[4] is not None:
                    date_time_since = datetime.fromtimestamp(result[4])
                    event.since = date_time_since.strftime('%Y-%m-%dT%H:%M:%S')
                if result[5] is not None:
                    date_time_until = datetime.fromtimestamp(result[5])
                    event.until = date_time_until.strftime('%Y-%m-%dT%H:%M:%S')
                events.append(event)
            return events
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def saveEvent(self, event):
        try:
            date_time_since = datetime.fromisoformat(event.since)
            date_time_until = datetime.fromisoformat(event.until)
            unix_timestamp_since = int(time.mktime(date_time_since.timetuple()))
            unix_timestamp_until = int(time.mktime(date_time_until.timetuple()))
            data_to_insert = (event.keyword, event.userID, event.mediaType,  unix_timestamp_since, unix_timestamp_until, event.language,
                              event.repost, event.latitude, event.longitude, event.radius, event.radiusUnit,
                              event.minRetweet, event.minFac)
            self.cursor.execute("INSERT INTO DisasterEvent (KeyWord, UserID, MediaType, Since, Until, Language, Repost, Latitude, Longitude, Radius, RadiusUnit, MinRetweet, MinFac) "
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def updateEvent(self, event):
        try:
            date_time_since = datetime.fromisoformat(event.since)
            date_time_until = datetime.fromisoformat(event.until)
            unix_timestamp_since = int(time.mktime(date_time_since.timetuple()))
            unix_timestamp_until = int(time.mktime(date_time_until.timetuple()))
            data_to_update = (unix_timestamp_since, unix_timestamp_until, event.ID)
            self.cursor.execute("UPDATE DisasterEvent SET Since = ?, Until = ? WHERE EventID = ?", data_to_update)
            if event.keyword is not None:
                data_to_update = (event.keyword, event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET KeyWord = ? WHERE EventID = ?", data_to_update)
            if event.mediaType is not None:
                data_to_update = (event.mediaType,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET MediaType = ? WHERE EventID = ?", data_to_update)
            if event.language is not None:
                data_to_update = (event.language,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET Language = ? WHERE EventID = ?", data_to_update)
            if event.repost is not None:
                data_to_update = (event.repost,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET Repost = ? WHERE EventID = ?", data_to_update)
            if event.latitude is not None:
                data_to_update = (event.latitude,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET Latitude = ? WHERE EventID = ?", data_to_update)
            if event.longitude is not None:
                data_to_update = (event.longitude,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET Longitude = ? WHERE EventID = ?", data_to_update)
            if event.radius is not None:
                data_to_update = (event.radius,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET Radius = ? WHERE EventID = ?", data_to_update)
            if event.radiusUnit is not None:
                data_to_update = (event.radiusUnit,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET RadiusUnit = ? WHERE EventID = ?", data_to_update)
            if event.minRetweet is not None:
                data_to_update = (event.minRetweet,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET MinRetweet = ? WHERE EventID = ?", data_to_update)
            if event.minFac is not None:
                data_to_update = (event.minFac,event.ID)
                self.cursor.execute("UPDATE DisasterEvent SET MinFac = ? WHERE EventID = ?", data_to_update)
            self.conn.commit()
            rows_affected = self.cursor.rowcount
            return rows_affected
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def saveQuery(self, query):
        try:
            data_to_insert = (query.content, query.eventID)
            self.cursor.execute("INSERT INTO Query (QueryContent, EventID) VALUES (?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def updateQuery(self, query):
        try:
            data_to_update = (query.content,  query.ID)
            self.cursor.execute("UPDATE Query SET QueryContent = ? WHERE QueryID = ?", data_to_update)
            self.conn.commit()
            rows_affected = self.cursor.rowcount
            return rows_affected
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def loadQuery(self, id):
        try:
            sql_query = 'SELECT * FROM Query WHERE QueryID = ?'
            self.cursor.execute(sql_query, (id, ))
            result = self.cursor.fetchone()
            last_inserted_id = self.cursor.lastrowid
            if result is not None:
                query = Query(result[0], result[1], result[2])
                return query
            else:
                return None
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1
    
    def loadTweetsByEventID(self, EventID):
        try:
            sql_query = '''SELECT Q.QueryID, T.*
FROM Tweet AS T
JOIN QueryTweet AS QT ON T.TweetID = QT.TweetID
JOIN Query AS Q ON QT.QueryID = Q.QueryID
WHERE Q.EventID = ?
''' 
            self.cursor.execute(sql_query, (EventID, ))
            results = self.cursor.fetchall()
            Tweets = {}
            for result in results:
                Tweets[result[0]] = Tweets.get(result[0], []) + [Tweet(result[1], result[2], result[3], result[4])]
            return Tweets
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def loadQueryByEvent(self, EventId):
        try:
            sql_query = 'SELECT * FROM Query WHERE EventID = ?'
            self.cursor.execute(sql_query, (EventId, ))
            results = self.cursor.fetchall()
            queries = []
            for result in results:
                query = Query(result[0], result[1], result[2])
                queries.append(query)
            return queries
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def loadTweet(self, id):
        try:
            sql_query = 'SELECT * FROM Tweet WHERE TweetID = ?'
            self.cursor.execute(sql_query, (id, ))
            result = self.cursor.fetchone()
            last_inserted_id = self.cursor.lastrowid
            if result is not None:
                tweet = Tweet(result[0], result[1], result[2], result[3], result[4])
                return tweet
            else:
                return None
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def loadTweetIDByQuery(self, QueryId):
        try:
            sql_query = 'SELECT * FROM QueryTweet WHERE QueryID = ?'
            self.cursor.execute(sql_query, (QueryId, ))
            results = self.cursor.fetchall()
            TweetIDs = []
            for result in results:
                TweetID = result[2]
                TweetIDs.append(TweetID)
            return TweetIDs
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def searchTwitter(self, event, query):
        try:
            self.cursor.execute('SELECT * FROM Tweet')
            rows = self.cursor.fetchall()

            tweet_list = []
            for row in rows:
                tweet_content = row[3]
                if query.content in tweet_content:
                    tweet = Tweet(row[0], row[1], row[2], row[3], row[4])
                    tweet_list.append(tweet)
                    data_to_insert0 = (event.ID, row[0])
                    data_to_insert1 = (query.ID, row[0])
                    self.cursor.execute("INSERT INTO EventTweet (EventID, TweetID) VALUES (?, ?)", data_to_insert0)
                    self.cursor.execute("INSERT INTO QueryTweet (QueryID, TweetID) VALUES (?, ?)", data_to_insert1)

            self.conn.commit()
            return tweet_list
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1


