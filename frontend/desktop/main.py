import sys
import os
import platform
import grpc
import protobufs.gRPC_pb2 as gRPC_pb2
from protobufs.gRPC_pb2_grpc import UserServiceStub, EventServiceStub, QueryServiceStub, TweetServiceStub
from datetime import date
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# https://twitter.com/search-advanced
# IMPORT / GUI AND MODULES AND widgets
# ///////////////////////////////////////////////////////////////
from frontend.desktop.modules.ui_main import Ui_MainWindow
from frontend.desktop.modules.ui_functions import UIFunctions 
from frontend.desktop.modules.app_settings import Settings
from frontend.desktop.widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

class MainWindow(QMainWindow):
    def __init__(self):
        # CREATE gRPC client
        # //////////////////////////////////////////////////////////////
        channel = grpc.insecure_channel("localhost:50051")
        self.userStub = UserServiceStub(channel)
        self.eventStub = EventServiceStub(channel)
        self.queryStub = QueryServiceStub(channel)
        self.tweetStub = TweetServiceStub(channel)

        self.url = "http://localhost:8000/"
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.queries_dict = {}
        QMainWindow.__init__(self)

        # SET AS GLOBAL self.ui
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.global_state = False
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Crisis Deck"
        description = "Crisis Deck - A social monitoring tool for tracking real-time crisis humanitarian information."
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.ui.titleRightInfo.setText(description)
        # self.ui.titleLeftName.setText("")
        today = date.today()
        today = today.strftime("%b-%d-%Y")
        self.ui.titleLeftDate.setText(f"{today}")

        # DISABLE 
        self.ui.btn_widgets.setEnabled(False)
        self.ui.btn_management.setEnabled(False)
        self.ui.btn_deck.setEnabled(False)
        # self.ui.btn_exit.setEnabled(False)



        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        self.ui.btn_home.clicked.connect(self.buttonClick)
        self.ui.btn_widgets.clicked.connect(self.buttonClick)
        self.ui.btn_deck.clicked.connect(self.buttonClick)
        self.ui.btn_management.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        self.ui.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)


        # EXTRA LEFT GROUP BOX BUTTON
        self.ui.btn_content.clicked.connect(self.openCloseLeftGroupBox)
        self.ui.btn_location.clicked.connect(self.openCloseLeftGroupBox)
        self.ui.btn_engagement.clicked.connect(self.openCloseLeftGroupBox)
        # self.ui.btn_submit.clicked.connect(lambda: UIFunctions.updateEvent(self))


        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        self.ui.settingsTopBtn.clicked.connect(openCloseRightBox)
        # HOME PAGE
        self.ui.btn_login.clicked.connect(lambda: UIFunctions.login(self))
        self.ui.btn_register.clicked.connect(lambda: UIFunctions.register(self))


        # MANAGEMENT STACK
        # ///////////////////////////////////////////////////////////////
        self.ui.management.table_event.doubleClicked.connect(self.management_buttonClick)
        self.ui.management.btn_add_event.clicked.connect(self.event_btnClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            self.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW self.ui PAGE
        if btnName == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_deck":
            self.ui.stackedWidget.setCurrentWidget(self.ui.deck)
            # self.ui.stackedWidget.setCurrentWidget(self.ui.deck) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        if btnName == "btn_management":
            self.ui.stackedWidget.setCurrentWidget(self.ui.management) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def deck_buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        # NAVIGATE TO DECK
        # if btnName == "btn_login_login":
        #     self.ui.stackedWidget.setCurrentWidget(self.ui.deck)

        # SHOW QUERIES
        if btnName == "btn_search":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.queries)
        
        # SHOW FILTER
        if "btn_query" in btnName:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.filter)
        
        # SHOW QUERIES
        if btnName == "btn_apply":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.queries)

    def openCloseLeftGroupBox(self):
        btn = self.sender()
        UIFunctions.toggleLeftGrp(self, btn, True)
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def management_buttonClick(self):
        table = self.sender()
        # print(btn
        idx = table.selectionModel().selectedIndexes()[0]
        row_number = idx.row()
        column_number = idx.column()
        event_id = self.ui.management.table_event.item(row_number, 0).text()
            # print(row_number, column_number)
        # if column_number == 0:

        UIFunctions.setup_deck(self, event_id)
        self.ui.stackedWidget.setCurrentWidget(self.ui.deck)

    def connect_event_btnClick(self):
        # for i in range(self.ui.management.table_event.rowCount()):
            # self.ui.management.table_event.findChild(QPushButton, f"btn_edit_event_{i}").clicked.connect(openCloseLeftBox)
        for btn in self.ui.management.table_event.findChildren(QPushButton):
            btn.clicked.connect(self.event_btnClick)
    
    def event_btnClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_add_event":
            btnID = -1
        else:
            btnID = btnName.split('_')[-1]
        UIFunctions.toggleLeftBox_withID(self, btnID, isEvent=True)

    def connect_query_btnClick(self):
        for btn in self.ui.deck.scrollArea.findChildren(QPushButton):
            if btn.objectName() ==  "btn_new_query" or "btn_edit" in btn.objectName():
                btn.clicked.connect(self.query_btnClick)
            else:
                btn.clicked.connect(self.search_btnClick)

    def query_btnClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_new_query":
            btnID = -1
        else:
            btnID = btnName.split('_')[-1]
        UIFunctions.toggleLeftBox_withID(self, btnID, isEvent=False)
        
    def search_btnClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        queryID = btnName.split('_')[-1]
        tweet_query = self.ui.deck.scrollArea.findChild(QWidget, f"tweet_query_{queryID}")
        text = tweet_query.text_search.text()
        UIFunctions.search(self, text, queryID)

    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

        self.ui.text_latitude.setText()
        self.ui.text_longitude.setText()
        self.ui.text_radius.setText()
        self.ui.box_radius_unit.setCurrentText()

        self.ui.box_min_retweet.setValue()
        self.ui.box_min_fav.setValue()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
