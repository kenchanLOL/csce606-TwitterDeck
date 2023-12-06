class Tweet:
    def __init__(self, document):
        for key, value in document.items():
            setattr(self, key, value)