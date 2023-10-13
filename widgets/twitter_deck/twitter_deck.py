from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . tweets_query import TweetsQuery
class TwitterDeck(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stylesheet = {
            "label": "font:bold 22px;",
            "text": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); font-size:22px; border-radius:10px",
            "btn": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); border-radius:10px"
        }
        data_temp = {
            "username":"user1",
            "body":"RT @debbiegibson & #TeamDeb for @bizarro_chile #HITPARADE & @Blondieclub ! #chile #santiago http://t.co/A… "
        }
        tweets_list = [[data_temp] * i for i in range(3,10)]
        self.data = tweets_list
        self.query_list = []
        self.setupUi()

    def setupUi(self):
        self.layout_deck = QHBoxLayout(self)
        self.frame_content = QFrame(self)
        self.layout_content = QVBoxLayout(self.frame_content)
        self.scrollArea = QScrollArea(self.frame_content)
        self.scrollArea.setWidgetResizable(True)
        self.widget_scroll = QWidget(self.scrollArea)
        self.layout_scroll = QHBoxLayout(self.widget_scroll)
        self.scrollArea.setWidget(self.widget_scroll)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setupQuery()
        self.layout_content.addWidget(self.scrollArea)
        self.layout_deck.addWidget(self.frame_content) 

    def setupQuery(self):
        for i in range(len(self.data)):
            # print(i)
            tweet_query = TweetsQuery(self.stylesheet, self.data[i])
            tweet_query.setObjectName(f"tweet_query_{i}")
            self.layout_scroll.addWidget(tweet_query)
            self.query_list.append(tweet_query)