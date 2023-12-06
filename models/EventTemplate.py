class EventTemplate:
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

    def to_dict(self):
        return {
            "ID": self.ID,
            "Keyword": self.keyword,
            "UserID": self.userID,
            "MediaType": self.mediaType,
            "Since": self.since.isoformat(),
            "Until": self.until.isoformat(),
            "Language": self.language,
            "Repost": self.repost,
            "Latitude": self.latitude,
            "Longitude": self.longitude,
            "Radius": self.radius,
            "RadiusUnit": self.radiusUnit,
            "MinRetweet": self.minRetweet,
            "MinFac": self.minFac
        }