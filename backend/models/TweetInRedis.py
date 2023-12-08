class TweetInRedis:
    def __init__(self, ID=None, content=None, tweetID=None, userID=None):
        self.ID = ID
        self.content = content
        self.tweetID = tweetID
        self.userID = userID
    
    def to_dict(self):
        return {
            "ID": self.ID,
            "content": self.content,
            "tweetID": self.tweetID,
            "userID": self.userID
        }