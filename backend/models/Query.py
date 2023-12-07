class Query:
    def __init__(self, ID=None, content=None, eventID = None):
        self.ID = ID
        self.content = content
        self.eventID = eventID

    def to_dict(self):
        return {
            "ID": self.ID,
            "QueryContent": self.content,
            "EventID": self.eventID
        }