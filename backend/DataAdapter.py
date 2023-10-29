import sqlite3
from backend.Event import Event
from backend.Tweet import Tweet
from backend.Query import Query
from backend.User import User

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

    def loadEvent(self, id):
        try:
            sql_query = 'SELECT * FROM DisasterEvent WHERE EventID = ?'
            self.cursor.execute(sql_query, (id, ))
            result = self.cursor.fetchone()
            last_inserted_id = self.cursor.lastrowid
            if result is not None:
                event = Event(result[0], result[1], result[2], result[3], result[4])
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
                event = Event(result[0], result[1], result[2], result[3], result[4])
                events.append(event)
            return events
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def saveEvent(self, event):
        try:
            data_to_insert = (event.location, event.time, event.content, event.userID)
            self.cursor.execute("INSERT INTO DisasterEvent (EventLocation, EventTime, EventContent, UserID) VALUES (?, ?, ?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return -1

    def updateEvent(self, event):
        try:
            data_to_update = (event.location, event.time, event.content, event.userID, event.ID)
            sql_query = '''UPDATE DisasterEvent 
                           SET EventLocation = ?, 
                               EventTime = ?, 
                               EventContent = ?, 
                               UserID = ? 
                           WHERE EventID = ?'''
            self.cursor.execute(sql_query, data_to_update)
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


