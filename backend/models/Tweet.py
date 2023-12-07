from datetime import datetime
class Tweet:
    def __init__(self, ID=None, id_str=None, url=None, date=None, user=None, lang=None, rawContent=None,
                 replyCount=None, retweetCount=None, likeCount=None, quoteCount=None, conversationId=None,
                 hashtags=None, viewCount=None, place=None, coordinates=None):
        self.ID = ID
        self.id_str = id_str
        self.url = url
        self.date = date
        self.user = user
        self.lang = lang
        self.rawContent = rawContent
        self.replyCount = replyCount
        self.retweetCount = retweetCount
        self.likeCount = likeCount
        self.quoteCount = quoteCount
        self.conversationId = conversationId
        self.hashtags = hashtags
        self.viewCount = viewCount
        self.place = place
        self.coordinates = coordinates

    def to_dict(self):
        return {
            "ID": self.ID,
            "id_str": self.id_str,
            "url": self.url,
            "date": self.date,
            "user": self.user,
            "lang": self.lang,
            "rawContent": self.rawContent,
            "replyCount": self.replyCount,
            "retweetCount": self.retweetCount,
            "likeCount": self.likeCount,
            "quoteCount": self.quoteCount,
            "conversationId": self.conversationId,
            "hashtags": self.hashtags,
            "viewCount": self.viewCount
            # "place": self.place,
            # "coordinates": self.coordinates
        }