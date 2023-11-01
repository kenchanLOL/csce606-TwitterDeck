# MAIN FILE
# ///////////////////////////////////////////////////////////////
# from main import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from modules.app_settings import Settings
from widgets import CustomGrip
from modules.ui_dialog import Ui_Dialog
from backend import backend_function
class UIFunctions():
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        # global self.global_state
        # status = self.global_state
        if self.global_state == False:
            self.showMaximized()
            self.global_state = True
            self.ui.appLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            self.global_state = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            # self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.appLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return self.global_state

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        self.global_state = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")
 
    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////   
    def toggleLeftGrp(self, selected_btn, enable):
        other_grps = []
        other_btns = []
        height_grps = []
        for grp in self.ui.extraTopMenu.findChildren(QGroupBox):
            if grp.objectName().split("_")[-1] != selected_btn.objectName().split("_")[-1]:
                other_grps.append(grp)
            else:
                selected_grp = grp
        for btn in self.ui.extraTopMenu.findChildren(QPushButton):
            if btn.objectName() != selected_btn.objectName():
                other_btns.append(btn)

        if enable:
            # GET WIDTH
            selected_height = selected_grp.height()
            for grp in other_grps:
                height_grps.append(grp.height())
            # maxExtend = Settings.GRP_HEIGHT
            color = Settings.BTN_LEFT_BOX_COLOR
            # standard = 0

            # GET BTN STYLE
            style = selected_btn.styleSheet()

            # SET MAX WIDTH
            if selected_height == 0:
                # SELECT BTN
                selected_btn.setStyleSheet(style + color)
                for btn, height in zip(other_btns, height_grps):
                    if height != 0:
                        style = btn.styleSheet()
                        btn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                # RESET BTN
                selected_btn.setStyleSheet(style.replace(color, ''))
        # print(selected_btn, selected_grp, other_grps)
        UIFunctions.start_grp_animation(self, selected_grp, other_grps, selected_height, height_grps)


    def start_grp_animation(self, selected_grp, other_grps, selected_height, other_start):
        if selected_height == 0:
            height_end = Settings.GRP_HEIGHT
        else:
            height_end = 0
        other_height_end = 0
        self.group2 = QParallelAnimationGroup()
        self.selected_animation = QPropertyAnimation(selected_grp, b"maximumHeight")
        self.selected_animation.setDuration(Settings.TIME_ANIMATION)
        self.selected_animation.setStartValue(selected_height)
        self.selected_animation.setEndValue(height_end)
        self.selected_animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.group2.addAnimation(self.selected_animation)
        # self.other_btns_animation = []

        for grp, other_height_start in zip(other_grps, other_start):
            unselected_animation = QPropertyAnimation(grp, b"maximumHeight")
            unselected_animation.setDuration(Settings.TIME_ANIMATION)
            unselected_animation.setStartValue(other_height_start)
            unselected_animation.setEndValue(other_height_end)
            unselected_animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.group2.addAnimation(unselected_animation)
        self.group2.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    #  LOGIN AND SETUP
    # ///////////////////////////////////////////////////////////////
    def login(self):
        name  = self.ui.text_username.text()
        password = self.ui.text_password.text()
        success, user = backend_function.Login(name, password, self.userStub)
        if not success:
            popUp = dialog("Login Failed")
            popUp.exec()
        else:
            self.user = user
            # uplock btns
            self.ui.btn_widgets.setEnabled(True)
            self.ui.btn_management.setEnabled(True)
            self.ui.btn_deck.setEnabled(True)
            # jump to management page
            UIFunctions.setup_management(self)
            self.ui.stackedWidget.setCurrentWidget(self.ui.management)

    
    def register(self):
        name  = self.ui.text_username.text()
        password = self.ui.text_password.text()
        pass
        # name  = self.ui.text_username.text()
        # password = self.ui.text_password.text()
        # print(name, password)
        # TODO: uplock btns
        # TODO: jump to management page

    def setup_management(self):
        events = backend_function.GetEventByUser(self.user.ID, self.eventStub)
        self.ui.management.setup_events(events)
        self.connect_event_btnClick()
        # def openCloseLeftBox():
        #     UIFunctions.toggleLeftBox(self, True)

    def setup_deck(self, row_number, column_number):
        # self.ui.management.table_event.item()
        event_id = int(self.ui.management.table_event.item(row_number, 0).text())
        Queries = backend_function.GetQueryByEvent(event_id, self.queryStub)
        tweets = {}
        for query in Queries:
            tweets[query.ID] = backend_function.GetTweetByQuery(query.ID, self.tweetStub)
        # tweets = backend_function.GetTweetsByEvent(event_id, self.eventStub)
        self.ui.deck.setupQuery(tweets)
        self.connect_query_btnClick()
        UIFunctions.resetStyle(self, "btn_deck")
        self.ui.btn_deck.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_deck.styleSheet()))


    # TOGGLE BAR AND EVENT RELATED
    # ////////////////////////////////////////////////////////////////////////// 
    def toggleLeftBox_withID(self, ID, isEvent):
        if isEvent :
            self.current_event = backend_function.LoadEvent(ID, self.eventStub)
            # TODO: display event attribute in toggle bar
            if ID != -1:
                self.ui.extraLabel.setText("Event " + str(self.current_event.ID))
                # self.ui.extraLabel.setText("Event " + str(eventID))
            else:
                self.ui.extraLabel.setText("New Event")
            self.ui.btn_submit.clicked.connect(lambda: UIFunctions.updateEvent(self))

        else: # is Query
            # TODO: link with backend function
            # self.current_query = backend_function.GetQueryByID(ID, self.stub)
            self.current_query = ID
            # TODO: display event attribute in toggle bar
            if ID != -1:
                # self.ui.extraLabel.setText("Query " + str(self.current_event.ID))
                self.ui.extraLabel.setText("Query " + str(self.current_query))
            else:
                self.ui.extraLabel.setText("New Query")
                # TODO: add new widget to scroll area
            self.ui.btn_submit.clicked.connect(lambda: UIFunctions.updateQuery(self))
        
        UIFunctions.toggleLeftBox(self, True)
        
    def updateEvent(self):
        print("Update Event")
        config = UIFunctions.readToggleLeftInfo(self)
        # backend_function.UpdateEvent(config)
        UIFunctions.toggleLeftBox(self, True)
    
    def updateQuery(self):
        print("Update Query")
        config = UIFunctions.readToggleLeftInfo(self)
        # backend_function.UpdateQuery(config)
        UIFunctions.toggleLeftBox(self, True)
    
    def readToggleLeftInfo(self):
        config = {}
        # Content group
        config["keyword"] = self.ui.text_keywords.text()
        config["media_type"] = self.ui.box_media_type.currentText()
        config["time_since"] = self.ui.time_since.time()
        config["time_until"] = self.ui.time_until.time()
        config["language"] = self.ui.box_lang.text()
        config["repost"] = self.ui.btn_repost.isChecked()

        # Location group
        config["latitude"] = self.ui.text_latitude.text()
        config["longitude"] = self.ui.text_longitude.text()
        config["radius"] = self.ui.text_radius.text()
        config["radius_unit"] = self.ui.box_radius_unit.currentText()

        # Engagement group
        config["min_retweet"] = self.ui.box_min_retweet.value()
        config["min_fav"] = self.ui.box_min_fav.value()
        print(config)
        return config    

    def search(self, text, queryID):
        print(f"searching {text} in queryID {queryID}")
        # event = Event()
        # backend_function.searchTweet(self, text, queryID)

    # END - GUI DEFINITIONS

class dialog(QDialog):
    def __init__(self, context):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(300, 200)
        self.ui.setupUi(self)
        self.ui.label.setText(context)
