from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . tweets_query import TweetsQuery
import json
class TwitterDeck(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stylesheet = {
            "label": "font:bold 22px;",
            "text": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); font-size:22px; border-radius:10px",
            "btn": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); border-radius:10px"
        }
        # data_temp = {
        #     "username":"user1",
        #     "body":"RT @debbiegibson & #TeamDeb for @bizarro_chile #HITPARADE & @Blondieclub ! #chile #santiago http://t.co/A… "
        # }
        # tweets_list = [[data_temp] * i for i in range(3,10)]
        # self.data = tweets_list
        self.query_list = {}
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
        # self.setupQuery()
        self.layout_content.addWidget(self.scrollArea)
        self.layout_deck.addWidget(self.frame_content) 

    def setupQuery(self, data):
        self.query_list = data
        # delete existing child
        for child in self.widget_scroll.findChildren(TweetsQuery):
            child.deleteLater()
        for child in self.widget_scroll.findChildren(QPushButton):
            child.deleteLater()
        for queryID, ls in self.query_list.items():
            # print(i)
            query = ls[0]
            tweet_query = TweetsQuery(self.stylesheet, ls[1:])
            keyword = json.loads(query.content)["keyword"]
            tweet_query.text_search.setText(keyword)
            tweet_query.setObjectName(f"tweet_query_{queryID}")
            tweet_query.btn_edit.setObjectName(f"btn_edit_{queryID}")
            tweet_query.btn_search.setObjectName(f"btn_search_{queryID}")

            self.layout_scroll.addWidget(tweet_query)
        self.btn_new_query = QPushButton(" + ")
        self.btn_new_query.setObjectName("btn_new_query")
        self.btn_new_query.setStyleSheet("font: 50pt bold; padding-bottom:10px")
        self.layout_scroll.addWidget(self.btn_new_query)
        
    # def addQuery(self, query):
    #     tweet_query = TweetsQuery(self.stylesheet, [])
    #     tweet_query.setObjectName(f"tweet_query_{queryID}")
    #     self.layout_scroll.addWidget(tweet_query)
            # self.query_list.append(tweet_query)