from Tweet import Tweet


def loadTweetfromDB(event, query, dataAdapter):
    tweet_list = dataAdapter.searchTwitter(event, query)
    return tweet_list
