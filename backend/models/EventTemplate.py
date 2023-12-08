from datetime import datetime
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
        
    def update_from_dict(self, update_dict):
        # Define a mapping of attribute names to their expected data types
        data_types = {
            "id": int,
            "keyword": str,
            "userID": str,
            "mediaType": str,
            "since": datetime,
            "until": datetime,
            "language": str,
            "repost": bool,
            "latitude": float,
            "longitude": float,
            "radius": float,
            "radiusunit": str,
            "minRetweet": int,
            "minFac": int
        }

        for key, value in update_dict.items():
            # Check if the attribute exists and its type is defined
            if hasattr(self, key) and key in data_types:
                # Convert the value to the expected type
                try:
                    if data_types[key] == datetime:
                         converted_value = datetime.fromisoformat(value)
                    else:
                        converted_value = data_types[key](value)
                    setattr(self, key, converted_value)
                except ValueError:
                    print(f"Value for {key} is not of expected type {data_types[key]}")
