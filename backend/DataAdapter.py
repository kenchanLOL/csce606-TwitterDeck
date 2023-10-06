import sqlite3
from Event import Event
from Tweet import Tweet
from Query import Query
from User import User

# dbname = 'TwitterDeck.db'
class DataAdapter:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
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
            return None

    def saveEvent(self, event):
        try:
            data_to_insert = (event.location, event.time, event.content, event.userID)
            self.cursor.execute("INSERT INTO DisasterEvent (EventLocation, EventTime, EventContent, UserID) VALUES (?, ?, ?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return None

    def saveQuery(self, query):
        try:
            data_to_insert = (query.content, query.eventID)
            self.cursor.execute("INSERT INTO Query (QueryContent, EventID) VALUES (?, ?)", data_to_insert)
            self.conn.commit()
            last_inserted_id = self.cursor.lastrowid
            return last_inserted_id
        except sqlite3.Error as e:
            print("DB error:", e)
            return None


    def loadTwitter(self, event, query):
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
            return None


