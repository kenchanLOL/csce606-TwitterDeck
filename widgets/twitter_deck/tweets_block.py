from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class TweetsBlock(QTextEdit):
    def __init__(self, data):
        super().__init__()
        self.setReadOnly(True)
        self.username = data.personID
        self.content = data.content
        self.html_head = """
            <html>
            <head>
                <style type="text/css">
                    p, li { white-space: pre-wrap; }
                    /* Style for normal text (black color) */
                    body {
                        color: black;
                    }
                    /* Style for links (blue color) */
                    a {
                        color: #1da1f2;
                        text-decoration: underline;
                    }
                    /* Style for hashtags (blue color) */
                    span.hashtag {
                        color: #1da1f2;
                    }
                </style>
            </head>
            """ 
        self.html_body = """
<body style="font-family: 'Segoe UI'; font-size: 10pt; font-weight: 400; font-style: normal;">
<p style="margin-top: 10px; margin-bottom: 5px; margin-left: 10px; margin-right: 10px; -qt-block-indent: 0; text-indent: 0px;">
    <img src="twitter-avatar.jpg" alt="Twitter Avatar" /><span style="font-size: 9pt; font-weight: 696;">@{username}</span>
</p>
<p style="margin-top: 12px; margin-bottom: 12px; margin-left: 10px; margin-right: 10px; -qt-block-indent: 0; text-indent: 0px;">
    <span style="font-size: 9pt;">{content}</span>
</p>
</body>
</html>"""
        self.styleSheets = "background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;"
        self.setHtml(self.html_head + self.html_body.format(username=self.username, content=self.content))
        self.setStyleSheet(self.styleSheets)
        self.setMinimumHeight(150)

# <a href="http://t.co/6Kj1mkBCT3"><span style="font-size:9pt; text-decoration: underline; color:#1da1f2;">http://t.co/6Kj1mkBCT3</span></a><span class="hashtag" style="font-size:9pt;"> #ChileEarthquake </span></p>
# <p style="margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;"><span class="hashtag" style="font-size:9pt;">Like</span><span style="font-size:9pt;"> </span><span class="hashtag" style="font-size:9pt;">Retweet</span><span style="font-size:9pt;"> </span></p>
