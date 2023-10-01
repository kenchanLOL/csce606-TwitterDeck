from Tweet import Tweet


def loadTweetfromDB(event, query, dataAdapter):
    tweet_list = dataAdapter.loadTwitter(event, query)
    return tweet_list
