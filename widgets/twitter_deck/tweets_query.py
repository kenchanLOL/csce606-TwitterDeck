from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . tweets_block import TweetsBlock
class TweetsQuery(QFrame):
    def __init__(self, styleSheet, data):
        super().__init__()
        self.stylesheet = styleSheet
        self.data = data
        self.tweets_block_lsit = []
        self.create_query()
        self.setMinimumWidth(400)

    def create_query(self):
        self.layout_query = QVBoxLayout(self)
        self.frame_search = QFrame(self)
        self.frame_search.setMaximumHeight(50)
        self.frame_content = QFrame(self)
        # search bar
        self.layout_search = QHBoxLayout(self.frame_search)
        self.label_search = QLabel(self.frame_search)
        self.label_search.setText("Query: ")
        self.label_search.setStyleSheet(self.stylesheet["label"])
        
        self.text_search = QPlainTextEdit(self.frame_search)
        self.text_search.setStyleSheet(self.stylesheet["text"])
        self.text_search.setFixedHeight(40)

        self.btn_search = QPushButton(self.frame_search)
        self.btn_search.setText("\u21b5")
        self.btn_search.setStyleSheet(self.stylesheet["btn"])
        self.btn_search.setFixedHeight(40)

        self.layout_search.addWidget(self.label_search, 1)
        self.layout_search.addWidget(self.text_search, 15)
        self.layout_search.addWidget(self.btn_search, 2)
        # tweets list
        self.layout_content = QVBoxLayout(self.frame_content)
        self.scroll_tweets = QScrollArea(self.frame_content)
        self.scroll_tweets.setWidgetResizable(True)
        self.scroll_widget_tweets = QWidget(self.scroll_tweets)
        # self.scroll_widget_tweets.setMinimumWidth(self.scroll_tweets.width())
        self.layout_scroll = QVBoxLayout(self.scroll_widget_tweets)
        self.scroll_tweets.setWidget(self.scroll_widget_tweets)
        self.scroll_tweets.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # self.scroll_tweets.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.add_tweets()
        self.layout_content.addWidget(self.scroll_tweets)

        self.layout_query.addWidget(self.frame_search)
        self.layout_query.addWidget(self.frame_content)

    def add_tweets(self):
        for i in range(len(self.data)):
            # print(i)
            tweet_block = TweetsBlock(self.data[i])
            tweet_block.setObjectName(f"tweet_block_{i}")
            # tweet_block.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Set horizontal size policy
            self.layout_scroll.addWidget(tweet_block)
            self.tweets_block_lsit.append(tweet_block)




