class Event:
    def __init__(self, ID=None, keyword=None, mediaType=None, since=None, until=None, language=None,
                 repost=None, latitude=None, longitude=None, radius=None, radiusUnit=None, minRetweet=None,
                 minFac=None, userID=None):
        self.ID = ID
        self.keyword = keyword
        self.userID = userID
        self.mediaType = mediaType
        self.since = since
        self.until = until
        self.language = language
        self.repost = repost
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.radiusUnit = radiusUnit
        self.minRetweet = minRetweet
        self.minFac = minFac
