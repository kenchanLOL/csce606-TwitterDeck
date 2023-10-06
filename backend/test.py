from DataAdapter import DataAdapter
from LoginControl import login
from EventControl import saveEventfromFrontend
from QueryControl import saveQueryfromFrontend
from TweetControl import loadTweetfromDB

if __name__ == "__main__":
    dataAdapter = DataAdapter("TwitterDeck.db")
    user = login('admin', 'password', dataAdapter)
    print(user.ID)

    location = "Texas, USA"
    time = "2020-10"
    content = "Volcano"
    event = saveEventfromFrontend(location, time, content, user, dataAdapter)
    print(event.ID, event.location, event.time, event.content, event.userID)

    content = "injuries"
    query = saveQueryfromFrontend(content, event, dataAdapter)
    print(query.ID, query.content, query.eventID)

    tweet_list = loadTweetfromDB(event, query, dataAdapter)
    for tweet in tweet_list:
        print(tweet.ID, tweet.content, tweet.personID)
