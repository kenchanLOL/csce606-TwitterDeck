import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFrame, QVBoxLayout
from twitter_deck import *
from management import *

class testWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        styleSheet = {
            "label": "font:bold 22px;",
            "text": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); font-size:22px; border-radius:10px",
            "btn": "background-color: rgb(33, 37, 43); color:rgb(255, 255, 255); border-radius:10px"
        }
        data_temp = {
            "username":"user1",
            "body":"RT @debbiegibson & #TeamDeb for @bizarro_chile #HITPARADE & @Blondieclub ! #chile #santiago http://t.co/A… "
        }
        tweets_list = [[data_temp] * i for i in range(3,10)]
        # self.text_edit2 = TweetsBlock(data)
        # self.frame = QFrame()
        # self.verticalLayout = QVBoxLayout(self.frame)
        # self.verticalLayout.addWidget(self.query)
        # self.verticalLayout.addWidget(self.text_edit2)
        # Set the HTML content
        # self.text_edit.setHtml(html_template)
        # self.setWindowTitle("HTML Template in QTextEdit")
        # query = TwitterDeck()
        query = ManagementPage()
        self.setCentralWidget(query)

def main():
    app = QApplication(sys.argv)
    window = testWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
