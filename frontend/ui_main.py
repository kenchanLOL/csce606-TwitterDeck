# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QSize(800, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_23 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toodle = QFrame(self.frame_top)
        self.frame_toodle.setObjectName(u"frame_toodle")
        self.frame_toodle.setMinimumSize(QSize(80, 55))
        self.frame_toodle.setMaximumSize(QSize(80, 55))
        self.frame_toodle.setStyleSheet(u"background:rgb(0,143,150);")
        self.frame_toodle.setFrameShape(QFrame.NoFrame)
        self.frame_toodle.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toodle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toodle = QPushButton(self.frame_toodle)
        self.toodle.setObjectName(u"toodle")
        self.toodle.setMinimumSize(QSize(80, 55))
        self.toodle.setMaximumSize(QSize(80, 55))
        self.toodle.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,178,178);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/1x/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toodle.setIcon(icon)
        self.toodle.setIconSize(QSize(22, 12))
        self.toodle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.toodle)


        self.horizontalLayout.addWidget(self.frame_toodle)

        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.lab_appname.setFont(font)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lab_person = QLabel(self.frame_person)
        self.lab_person.setObjectName(u"lab_person")
        self.lab_person.setMaximumSize(QSize(55, 55))
        self.lab_person.setPixmap(QPixmap(u"icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lab_person)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_max = QFrame(self.frame_top_east)
        self.frame_max.setObjectName(u"frame_max")
        self.frame_max.setMinimumSize(QSize(55, 55))
        self.frame_max.setMaximumSize(QSize(55, 55))
        self.frame_max.setFrameShape(QFrame.NoFrame)
        self.frame_max.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_max)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.bn_max = QPushButton(self.frame_max)
        self.bn_max.setObjectName(u"bn_max")
        self.bn_max.setMaximumSize(QSize(55, 55))
        self.bn_max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_max.setIcon(icon2)
        self.bn_max.setIconSize(QSize(22, 22))
        self.bn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.bn_max)


        self.horizontalLayout_4.addWidget(self.frame_max)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon3)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout_23.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon4)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_news = QFrame(self.frame_bottom_west)
        self.frame_news.setObjectName(u"frame_news")
        self.frame_news.setMinimumSize(QSize(80, 55))
        self.frame_news.setMaximumSize(QSize(160, 55))
        self.frame_news.setFrameShape(QFrame.NoFrame)
        self.frame_news.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_news)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_news = QPushButton(self.frame_news)
        self.bn_news.setObjectName(u"bn_news")
        self.bn_news.setMinimumSize(QSize(80, 55))
        self.bn_news.setMaximumSize(QSize(160, 55))
        self.bn_news.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/worldAsset 60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_news.setIcon(icon5)
        self.bn_news.setIconSize(QSize(22, 22))
        self.bn_news.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_news)


        self.verticalLayout_3.addWidget(self.frame_news)

        self.frame_login_icon = QFrame(self.frame_bottom_west)
        self.frame_login_icon.setObjectName(u"frame_login_icon")
        self.frame_login_icon.setMinimumSize(QSize(80, 55))
        self.frame_login_icon.setMaximumSize(QSize(160, 55))
        self.frame_login_icon.setFrameShape(QFrame.NoFrame)
        self.frame_login_icon.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_login_icon)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_login = QPushButton(self.frame_login_icon)
        self.bn_login.setObjectName(u"bn_login")
        self.bn_login.setMinimumSize(QSize(80, 55))
        self.bn_login.setMaximumSize(QSize(160, 55))
        self.bn_login.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/peopleAsset 62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_login.setIcon(icon6)
        self.bn_login.setIconSize(QSize(22, 12))
        self.bn_login.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_login)


        self.verticalLayout_3.addWidget(self.frame_login_icon)

        self.frame_deck = QFrame(self.frame_bottom_west)
        self.frame_deck.setObjectName(u"frame_deck")
        self.frame_deck.setMinimumSize(QSize(80, 55))
        self.frame_deck.setMaximumSize(QSize(160, 55))
        self.frame_deck.setFrameShape(QFrame.NoFrame)
        self.frame_deck.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_deck)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_deck = QPushButton(self.frame_deck)
        self.bn_deck.setObjectName(u"bn_deck")
        self.bn_deck.setMinimumSize(QSize(80, 55))
        self.bn_deck.setMaximumSize(QSize(160, 55))
        self.bn_deck.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_deck.setIcon(icon5)
        self.bn_deck.setIconSize(QSize(20, 22))
        self.bn_deck.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_deck)


        self.verticalLayout_3.addWidget(self.frame_deck)

        self.btn_extend = QPushButton(self.frame_bottom_west)
        self.btn_extend.setObjectName(u"btn_extend")
        self.btn_extend.setMinimumSize(QSize(0, 55))
        self.btn_extend.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/dragAsset 52.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extend.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.btn_extend)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 55))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(24)
        self.lab_home_main_hed.setFont(font1)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_main_disc = QLabel(self.frame_home_main)
        self.lab_home_main_disc.setObjectName(u"lab_home_main_disc")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.lab_home_main_disc.setFont(font2)
        self.lab_home_main_disc.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_home_main_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lab_home_main_disc.setWordWrap(True)
        self.lab_home_main_disc.setMargin(5)

        self.verticalLayout_5.addWidget(self.lab_home_main_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.lab_home_stat_hed = QLabel(self.frame_home_stat)
        self.lab_home_stat_hed.setObjectName(u"lab_home_stat_hed")
        self.lab_home_stat_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_stat_hed.setMaximumSize(QSize(16777215, 55))
        self.lab_home_stat_hed.setFont(font1)
        self.lab_home_stat_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_stat_hed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lab_home_stat_hed)

        self.lab_home_stat_disc = QLabel(self.frame_home_stat)
        self.lab_home_stat_disc.setObjectName(u"lab_home_stat_disc")
        self.lab_home_stat_disc.setFont(font2)
        self.lab_home_stat_disc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lab_home_stat_disc)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(24)
        self.lab_about_home.setFont(font3)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextEdit(self.frame_about_home)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        self.text_about_home.setFont(font2)
        self.text_about_home.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_home.setFrameShape(QFrame.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)

        self.vsb_about_home = QScrollBar(self.frame_about_home)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.page_about_login = QWidget()
        self.page_about_login.setObjectName(u"page_about_login")
        self.page_about_login.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_login)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_login)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(30)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_login)
        self.page_about_deck = QWidget()
        self.page_about_deck.setObjectName(u"page_about_deck")
        self.page_about_deck.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_deck)
        self.page_about_news = QWidget()
        self.page_about_news.setObjectName(u"page_about_news")
        self.page_about_news.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_news)
        self.page_news = QWidget()
        self.page_news.setObjectName(u"page_news")
        self.page_news.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_news)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_Bug = QLabel(self.page_news)
        self.lab_Bug.setObjectName(u"lab_Bug")
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        self.lab_Bug.setFont(font1)
        self.lab_Bug.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_7.addWidget(self.lab_Bug)

        self.frame_news_main = QFrame(self.page_news)
        self.frame_news_main.setObjectName(u"frame_news_main")
        self.frame_news_main.setMinimumSize(QSize(0, 200))
        self.frame_news_main.setMaximumSize(QSize(16777215, 200))
        self.frame_news_main.setFrameShape(QFrame.NoFrame)
        self.frame_news_main.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_news_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_news = QComboBox(self.frame_news_main)
        self.comboBox_news.addItem("")
        self.comboBox_news.addItem("")
        self.comboBox_news.addItem("")
        self.comboBox_news.addItem("")
        self.comboBox_news.setObjectName(u"comboBox_news")
        self.comboBox_news.setMaximumSize(QSize(16777215, 25))
        self.comboBox_news.setFont(font2)
        self.comboBox_news.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"")
        self.comboBox_news.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_news.setFrame(False)
        self.comboBox_news.setModelColumn(0)

        self.gridLayout.addWidget(self.comboBox_news, 0, 6, 1, 1)

        self.progressBar_news = QProgressBar(self.frame_news_main)
        self.progressBar_news.setObjectName(u"progressBar_news")
        self.progressBar_news.setEnabled(True)
        self.progressBar_news.setStyleSheet(u"QProgressBar\n"
"{\n"
"	color:rgb(255,255,255);\n"
"	background-color :rgb(51,51,51);\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border : 2px;\n"
"	border-radius:4px;\n"
"	background-color:rgb(0,143,170);\n"
"}")
        self.progressBar_news.setValue(0)
        self.progressBar_news.setAlignment(Qt.AlignCenter)
        self.progressBar_news.setTextVisible(True)
        self.progressBar_news.setOrientation(Qt.Horizontal)
        self.progressBar_news.setInvertedAppearance(False)
        self.progressBar_news.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar_news, 1, 5, 1, 3)

        self.bn_news_start = QPushButton(self.frame_news_main)
        self.bn_news_start.setObjectName(u"bn_news_start")
        self.bn_news_start.setMinimumSize(QSize(69, 25))
        self.bn_news_start.setMaximumSize(QSize(69, 25))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.bn_news_start.setFont(font5)
        self.bn_news_start.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")
        self.bn_news_start.setCheckable(False)
        self.bn_news_start.setFlat(True)

        self.gridLayout.addWidget(self.bn_news_start, 0, 7, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_news_main)

        self.verticalSpacer = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_news)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_login)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_login_main = QLabel(self.page_login)
        self.lab_login_main.setObjectName(u"lab_login_main")
        self.lab_login_main.setMinimumSize(QSize(0, 55))
        self.lab_login_main.setMaximumSize(QSize(16777215, 55))
        self.lab_login_main.setFont(font3)
        self.lab_login_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_login_main)

        self.frame_login = QFrame(self.page_login)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setEnabled(True)
        self.frame_login.setMinimumSize(QSize(0, 235))
        self.frame_login.setMaximumSize(QSize(16777215, 235))
        self.frame_login.setFont(font5)
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 2)

        self.bn_login_login = QPushButton(self.frame_login)
        self.bn_login_login.setObjectName(u"bn_login_login")
        self.bn_login_login.setMinimumSize(QSize(69, 25))
        self.bn_login_login.setMaximumSize(QSize(69, 25))
        self.bn_login_login.setFont(font5)
        self.bn_login_login.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_login_login, 2, 4, 1, 1)

        self.label_login_id = QLabel(self.frame_login)
        self.label_login_id.setObjectName(u"label_login_id")
        self.label_login_id.setMinimumSize(QSize(100, 0))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label_login_id.setFont(font6)
        self.label_login_id.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_login_id, 0, 0, 1, 1)

        self.label_login_password = QLabel(self.frame_login)
        self.label_login_password.setObjectName(u"label_login_password")
        self.label_login_password.setMinimumSize(QSize(100, 0))
        self.label_login_password.setFont(font6)
        self.label_login_password.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_login_password, 1, 0, 1, 1)

        self.line_login_id = QLineEdit(self.frame_login)
        self.line_login_id.setObjectName(u"line_login_id")
        self.line_login_id.setEnabled(True)
        self.line_login_id.setMinimumSize(QSize(400, 25))
        self.line_login_id.setMaximumSize(QSize(500, 25))
        self.line_login_id.setFont(font5)
        self.line_login_id.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_login_id, 0, 1, 1, 4)

        self.bn_login_clear = QPushButton(self.frame_login)
        self.bn_login_clear.setObjectName(u"bn_login_clear")
        self.bn_login_clear.setEnabled(True)
        self.bn_login_clear.setMinimumSize(QSize(69, 25))
        self.bn_login_clear.setMaximumSize(QSize(69, 25))
        self.bn_login_clear.setFont(font5)
        self.bn_login_clear.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_login_clear, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 6, 1, 1)

        self.line_login_password = QLineEdit(self.frame_login)
        self.line_login_password.setObjectName(u"line_login_password")
        self.line_login_password.setMinimumSize(QSize(400, 25))
        self.line_login_password.setMaximumSize(QSize(500, 25))
        self.line_login_password.setFont(font5)
        self.line_login_password.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.line_login_password, 1, 1, 1, 4)

        self.bn_login_register = QPushButton(self.frame_login)
        self.bn_login_register.setObjectName(u"bn_login_register")
        self.bn_login_register.setMinimumSize(QSize(69, 25))
        self.bn_login_register.setMaximumSize(QSize(69, 25))
        font7 = QFont()
        font7.setPointSize(12)
        self.bn_login_register.setFont(font7)
        self.bn_login_register.setMouseTracking(True)
        self.bn_login_register.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.gridLayout_2.addWidget(self.bn_login_register, 2, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_login)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_login)
        self.page_deck = QWidget()
        self.page_deck.setObjectName(u"page_deck")
        self.page_deck.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_deck)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_deck_menu = QFrame(self.page_deck)
        self.frame_deck_menu.setObjectName(u"frame_deck_menu")
        self.frame_deck_menu.setMinimumSize(QSize(0, 30))
        self.frame_deck_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_deck_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_deck_menu.setFrameShape(QFrame.NoFrame)
        self.frame_deck_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_deck_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_deck_event = QFrame(self.frame_deck_menu)
        self.frame_deck_event.setObjectName(u"frame_deck_event")
        self.frame_deck_event.setMinimumSize(QSize(80, 30))
        self.frame_deck_event.setMaximumSize(QSize(80, 30))
        self.frame_deck_event.setFrameShape(QFrame.NoFrame)
        self.frame_deck_event.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_deck_event)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_deck_event = QPushButton(self.frame_deck_event)
        self.bn_deck_event.setObjectName(u"bn_deck_event")
        self.bn_deck_event.setMinimumSize(QSize(80, 30))
        self.bn_deck_event.setMaximumSize(QSize(80, 30))
        self.bn_deck_event.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_deck_event.setIcon(icon5)
        self.bn_deck_event.setIconSize(QSize(13, 16))
        self.bn_deck_event.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_deck_event)


        self.horizontalLayout_20.addWidget(self.frame_deck_event)

        self.frame_deck_query = QFrame(self.frame_deck_menu)
        self.frame_deck_query.setObjectName(u"frame_deck_query")
        self.frame_deck_query.setMinimumSize(QSize(80, 30))
        self.frame_deck_query.setMaximumSize(QSize(80, 30))
        self.frame_deck_query.setFrameShape(QFrame.NoFrame)
        self.frame_deck_query.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_deck_query)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_deck_query = QPushButton(self.frame_deck_query)
        self.bn_deck_query.setObjectName(u"bn_deck_query")
        self.bn_deck_query.setMinimumSize(QSize(80, 30))
        self.bn_deck_query.setMaximumSize(QSize(80, 30))
        self.bn_deck_query.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_deck_query.setIcon(icon5)
        self.bn_deck_query.setIconSize(QSize(20, 13))
        self.bn_deck_query.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_deck_query)


        self.horizontalLayout_20.addWidget(self.frame_deck_query)

        self.frame_deck_advance = QFrame(self.frame_deck_menu)
        self.frame_deck_advance.setObjectName(u"frame_deck_advance")
        self.frame_deck_advance.setMinimumSize(QSize(80, 30))
        self.frame_deck_advance.setMaximumSize(QSize(80, 30))
        self.frame_deck_advance.setFrameShape(QFrame.NoFrame)
        self.frame_deck_advance.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_deck_advance)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_deck_advance = QPushButton(self.frame_deck_advance)
        self.bn_deck_advance.setObjectName(u"bn_deck_advance")
        self.bn_deck_advance.setMinimumSize(QSize(80, 30))
        self.bn_deck_advance.setMaximumSize(QSize(80, 30))
        self.bn_deck_advance.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_deck_advance.setIcon(icon5)
        self.bn_deck_advance.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_deck_advance)


        self.horizontalLayout_20.addWidget(self.frame_deck_advance)

        self.frame_deck_clean = QFrame(self.frame_deck_menu)
        self.frame_deck_clean.setObjectName(u"frame_deck_clean")
        self.frame_deck_clean.setMinimumSize(QSize(80, 30))
        self.frame_deck_clean.setMaximumSize(QSize(80, 30))
        self.frame_deck_clean.setFrameShape(QFrame.NoFrame)
        self.frame_deck_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_deck_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_deck_clean = QPushButton(self.frame_deck_clean)
        self.bn_deck_clean.setObjectName(u"bn_deck_clean")
        self.bn_deck_clean.setMinimumSize(QSize(80, 30))
        self.bn_deck_clean.setMaximumSize(QSize(80, 30))
        self.bn_deck_clean.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/bugAsset 47.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_deck_clean.setIcon(icon8)
        self.bn_deck_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.bn_deck_clean)


        self.horizontalLayout_20.addWidget(self.frame_deck_clean)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_deck_menu)

        self.stackedWidget_deck = QStackedWidget(self.page_deck)
        self.stackedWidget_deck.setObjectName(u"stackedWidget_deck")
        self.stackedWidget_deck.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_deck_event = QWidget()
        self.page_deck_event.setObjectName(u"page_deck_event")
        self.page_deck_event.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_deck_event)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.label_event_title = QLabel(self.page_deck_event)
        self.label_event_title.setObjectName(u"label_event_title")
        self.label_event_title.setMinimumSize(QSize(0, 55))
        self.label_event_title.setMaximumSize(QSize(16777215, 55))
        self.label_event_title.setFont(font3)
        self.label_event_title.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.label_event_title)

        self.frame_event_bottom = QFrame(self.page_deck_event)
        self.frame_event_bottom.setObjectName(u"frame_event_bottom")
        self.frame_event_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_event_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_event_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_event_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/placeholder.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_event_field = QFrame(self.frame_event_bottom)
        self.frame_event_field.setObjectName(u"frame_event_field")
        self.frame_event_field.setFrameShape(QFrame.NoFrame)
        self.frame_event_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_event_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.combo_event_type = QComboBox(self.frame_event_field)
        self.combo_event_type.addItem("")
        self.combo_event_type.addItem("")
        self.combo_event_type.addItem("")
        self.combo_event_type.setObjectName(u"combo_event_type")
        font8 = QFont()
        font8.setPointSize(15)
        self.combo_event_type.setFont(font8)
        self.combo_event_type.setEditable(True)

        self.gridLayout_4.addWidget(self.combo_event_type, 6, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 8, 8, 1, 1)

        self.line_event_location = QLineEdit(self.frame_event_field)
        self.line_event_location.setObjectName(u"line_event_location")
        self.line_event_location.setEnabled(True)
        self.line_event_location.setMinimumSize(QSize(300, 25))
        self.line_event_location.setMaximumSize(QSize(400, 16777215))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(20)
        self.line_event_location.setFont(font9)
        self.line_event_location.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_event_location, 1, 3, 1, 1)

        self.label_event_since = QLabel(self.frame_event_field)
        self.label_event_since.setObjectName(u"label_event_since")
        self.label_event_since.setFont(font9)
        self.label_event_since.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_event_since, 3, 0, 1, 3)

        self.label_event_type = QLabel(self.frame_event_field)
        self.label_event_type.setObjectName(u"label_event_type")
        self.label_event_type.setFont(font9)
        self.label_event_type.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_event_type, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 9, 3, 1, 1)

        self.date_event_since = QDateTimeEdit(self.frame_event_field)
        self.date_event_since.setObjectName(u"date_event_since")
        self.date_event_since.setMinimumSize(QSize(0, 0))
        self.date_event_since.setFont(font8)

        self.gridLayout_4.addWidget(self.date_event_since, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 6, 8, 1, 1)

        self.label_event_location = QLabel(self.frame_event_field)
        self.label_event_location.setObjectName(u"label_event_location")
        self.label_event_location.setFont(font9)
        self.label_event_location.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_event_location, 1, 0, 1, 3)

        self.frame_event_bottom_btns = QFrame(self.frame_event_field)
        self.frame_event_bottom_btns.setObjectName(u"frame_event_bottom_btns")
        self.frame_event_bottom_btns.setFrameShape(QFrame.NoFrame)
        self.frame_event_bottom_btns.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_event_bottom_btns)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.bn_deck_event_edit = QPushButton(self.frame_event_bottom_btns)
        self.bn_deck_event_edit.setObjectName(u"bn_deck_event_edit")
        self.bn_deck_event_edit.setMinimumSize(QSize(69, 25))
        self.bn_deck_event_edit.setMaximumSize(QSize(69, 25))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(15)
        self.bn_deck_event_edit.setFont(font10)
        self.bn_deck_event_edit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_deck_event_edit)

        self.bn_deck_event_delete = QPushButton(self.frame_event_bottom_btns)
        self.bn_deck_event_delete.setObjectName(u"bn_deck_event_delete")
        self.bn_deck_event_delete.setMinimumSize(QSize(69, 25))
        self.bn_deck_event_delete.setMaximumSize(QSize(69, 25))
        self.bn_deck_event_delete.setFont(font10)
        self.bn_deck_event_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_deck_event_delete)

        self.bn_deck_event_save = QPushButton(self.frame_event_bottom_btns)
        self.bn_deck_event_save.setObjectName(u"bn_deck_event_save")
        self.bn_deck_event_save.setEnabled(True)
        self.bn_deck_event_save.setMinimumSize(QSize(69, 25))
        self.bn_deck_event_save.setMaximumSize(QSize(69, 25))
        self.bn_deck_event_save.setFont(font10)
        self.bn_deck_event_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_deck_event_save)


        self.gridLayout_4.addWidget(self.frame_event_bottom_btns, 8, 0, 1, 7)

        self.label_event_till = QLabel(self.frame_event_field)
        self.label_event_till.setObjectName(u"label_event_till")
        font11 = QFont()
        font11.setPointSize(20)
        self.label_event_till.setFont(font11)
        self.label_event_till.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_event_till, 4, 0, 1, 1)

        self.date_event_till = QDateTimeEdit(self.frame_event_field)
        self.date_event_till.setObjectName(u"date_event_till")
        self.date_event_till.setFont(font8)

        self.gridLayout_4.addWidget(self.date_event_till, 4, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_event_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_event_bottom)

        self.stackedWidget_deck.addWidget(self.page_deck_event)
        self.page_deck_query = QWidget()
        self.page_deck_query.setObjectName(u"page_deck_query")
        self.page_deck_query.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_deck_query)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_query = QFrame(self.page_deck_query)
        self.frame_query.setObjectName(u"frame_query")
        self.frame_query.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_query.setFrameShape(QFrame.StyledPanel)
        self.frame_query.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_query)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.frame_query_0 = QFrame(self.frame_query)
        self.frame_query_0.setObjectName(u"frame_query_0")
        self.verticalLayout_15 = QVBoxLayout(self.frame_query_0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_query_0_search = QFrame(self.frame_query_0)
        self.frame_query_0_search.setObjectName(u"frame_query_0_search")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_query_0_search)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_query_0 = QLabel(self.frame_query_0_search)
        self.label_query_0.setObjectName(u"label_query_0")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_query_0.sizePolicy().hasHeightForWidth())
        self.label_query_0.setSizePolicy(sizePolicy)
        font12 = QFont()
        font12.setPointSize(20)
        font12.setBold(False)
        self.label_query_0.setFont(font12)
        self.label_query_0.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.label_query_0)

        self.line_query_0 = QLineEdit(self.frame_query_0_search)
        self.line_query_0.setObjectName(u"line_query_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_query_0.sizePolicy().hasHeightForWidth())
        self.line_query_0.setSizePolicy(sizePolicy1)
        self.line_query_0.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.line_query_0)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_9)

        self.bn_query_0_enter = QPushButton(self.frame_query_0_search)
        self.bn_query_0_enter.setObjectName(u"bn_query_0_enter")
        sizePolicy1.setHeightForWidth(self.bn_query_0_enter.sizePolicy().hasHeightForWidth())
        self.bn_query_0_enter.setSizePolicy(sizePolicy1)
        self.bn_query_0_enter.setMaximumSize(QSize(50, 16777215))
        self.bn_query_0_enter.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.bn_query_0_enter)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer)

        self.bn_query_0_advance = QToolButton(self.frame_query_0_search)
        self.bn_query_0_advance.setObjectName(u"bn_query_0_advance")
        self.bn_query_0_advance.setStyleSheet(u"background:rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.bn_query_0_advance)


        self.verticalLayout_15.addWidget(self.frame_query_0_search)

        self.scrollArea_query_0_tweets = QScrollArea(self.frame_query_0)
        self.scrollArea_query_0_tweets.setObjectName(u"scrollArea_query_0_tweets")
        self.scrollArea_query_0_tweets.setStyleSheet(u"")
        self.scrollArea_query_0_tweets.setWidgetResizable(True)
        self.scrollAreaWidget_query_0_tweets = QWidget()
        self.scrollAreaWidget_query_0_tweets.setObjectName(u"scrollAreaWidget_query_0_tweets")
        self.scrollAreaWidget_query_0_tweets.setGeometry(QRect(0, 0, 331, 480))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidget_query_0_tweets)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.text__query_0_tweets0 = QTextEdit(self.scrollAreaWidget_query_0_tweets)
        self.text__query_0_tweets0.setObjectName(u"text__query_0_tweets0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text__query_0_tweets0.sizePolicy().hasHeightForWidth())
        self.text__query_0_tweets0.setSizePolicy(sizePolicy2)
        self.text__query_0_tweets0.setMinimumSize(QSize(300, 150))
        self.text__query_0_tweets0.setMaximumSize(QSize(16777215, 16777215))
        self.text__query_0_tweets0.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.text__query_0_tweets0)

        self.text__query_0_tweets1 = QTextEdit(self.scrollAreaWidget_query_0_tweets)
        self.text__query_0_tweets1.setObjectName(u"text__query_0_tweets1")
        sizePolicy2.setHeightForWidth(self.text__query_0_tweets1.sizePolicy().hasHeightForWidth())
        self.text__query_0_tweets1.setSizePolicy(sizePolicy2)
        self.text__query_0_tweets1.setMinimumSize(QSize(300, 150))
        self.text__query_0_tweets1.setMaximumSize(QSize(16777215, 16777215))
        self.text__query_0_tweets1.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.text__query_0_tweets1)

        self.text__query_0_tweets2 = QTextEdit(self.scrollAreaWidget_query_0_tweets)
        self.text__query_0_tweets2.setObjectName(u"text__query_0_tweets2")
        sizePolicy2.setHeightForWidth(self.text__query_0_tweets2.sizePolicy().hasHeightForWidth())
        self.text__query_0_tweets2.setSizePolicy(sizePolicy2)
        self.text__query_0_tweets2.setMinimumSize(QSize(300, 150))
        self.text__query_0_tweets2.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.text__query_0_tweets2)

        self.scrollArea_query_0_tweets.setWidget(self.scrollAreaWidget_query_0_tweets)

        self.verticalLayout_15.addWidget(self.scrollArea_query_0_tweets)


        self.horizontalLayout_26.addWidget(self.frame_query_0)

        self.frame_query_1 = QFrame(self.frame_query)
        self.frame_query_1.setObjectName(u"frame_query_1")
        self.verticalLayout_17 = QVBoxLayout(self.frame_query_1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_query_1_search = QFrame(self.frame_query_1)
        self.frame_query_1_search.setObjectName(u"frame_query_1_search")
        self.horizontalLayout_31 = QHBoxLayout(self.frame_query_1_search)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_query_1 = QLabel(self.frame_query_1_search)
        self.label_query_1.setObjectName(u"label_query_1")
        self.label_query_1.setFont(font11)
        self.label_query_1.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.label_query_1)

        self.line_query_1 = QLineEdit(self.frame_query_1_search)
        self.line_query_1.setObjectName(u"line_query_1")
        self.line_query_1.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.line_query_1)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_10)

        self.bn_query_1_enter = QPushButton(self.frame_query_1_search)
        self.bn_query_1_enter.setObjectName(u"bn_query_1_enter")
        sizePolicy1.setHeightForWidth(self.bn_query_1_enter.sizePolicy().hasHeightForWidth())
        self.bn_query_1_enter.setSizePolicy(sizePolicy1)
        self.bn_query_1_enter.setMaximumSize(QSize(50, 16777215))
        self.bn_query_1_enter.setStyleSheet(u"background:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.bn_query_1_enter)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_8)

        self.bn_query_1_advance = QToolButton(self.frame_query_1_search)
        self.bn_query_1_advance.setObjectName(u"bn_query_1_advance")
        self.bn_query_1_advance.setStyleSheet(u"background:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.bn_query_1_advance)


        self.verticalLayout_17.addWidget(self.frame_query_1_search)

        self.scrollArea_query_1_tweets = QScrollArea(self.frame_query_1)
        self.scrollArea_query_1_tweets.setObjectName(u"scrollArea_query_1_tweets")
        self.scrollArea_query_1_tweets.setWidgetResizable(True)
        self.scrollAreaWidget_query_1_tweets = QWidget()
        self.scrollAreaWidget_query_1_tweets.setObjectName(u"scrollAreaWidget_query_1_tweets")
        self.scrollAreaWidget_query_1_tweets.setGeometry(QRect(0, 0, 347, 385))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidget_query_1_tweets)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.text__query_1_tweets0 = QTextEdit(self.scrollAreaWidget_query_1_tweets)
        self.text__query_1_tweets0.setObjectName(u"text__query_1_tweets0")
        sizePolicy2.setHeightForWidth(self.text__query_1_tweets0.sizePolicy().hasHeightForWidth())
        self.text__query_1_tweets0.setSizePolicy(sizePolicy2)
        self.text__query_1_tweets0.setMinimumSize(QSize(300, 0))
        self.text__query_1_tweets0.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_16.addWidget(self.text__query_1_tweets0)

        self.text__query_1_tweets1 = QTextEdit(self.scrollAreaWidget_query_1_tweets)
        self.text__query_1_tweets1.setObjectName(u"text__query_1_tweets1")
        sizePolicy2.setHeightForWidth(self.text__query_1_tweets1.sizePolicy().hasHeightForWidth())
        self.text__query_1_tweets1.setSizePolicy(sizePolicy2)
        self.text__query_1_tweets1.setMinimumSize(QSize(300, 0))
        self.text__query_1_tweets1.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_16.addWidget(self.text__query_1_tweets1)

        self.scrollArea_query_1_tweets.setWidget(self.scrollAreaWidget_query_1_tweets)

        self.verticalLayout_17.addWidget(self.scrollArea_query_1_tweets)


        self.horizontalLayout_26.addWidget(self.frame_query_1)


        self.verticalLayout_11.addWidget(self.frame_query)

        self.stackedWidget_deck.addWidget(self.page_deck_query)
        self.page_deck_clean = QWidget()
        self.page_deck_clean.setObjectName(u"page_deck_clean")
        self.page_deck_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_deck_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.groupBox_clean = QGroupBox(self.page_deck_clean)
        self.groupBox_clean.setObjectName(u"groupBox_clean")
        self.groupBox_clean.setMinimumSize(QSize(250, 300))
        self.groupBox_clean.setMaximumSize(QSize(250, 300))
        self.groupBox_clean.setSizeIncrement(QSize(0, 0))
        self.groupBox_clean.setFont(font2)
        self.groupBox_clean.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_clean.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_clean.setFlat(False)
        self.groupBox_clean.setCheckable(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_clean)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton = QRadioButton(self.groupBox_clean)
        self.radioButton.setObjectName(u"radioButton")
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(9)
        self.radioButton.setFont(font13)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_clean)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font13)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_clean)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font13)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_3.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_clean)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font13)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_4.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_4)

        self.checkBox = QCheckBox(self.groupBox_clean)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font13)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.groupBox_clean)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font13)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox_4.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.checkBox_2 = QCheckBox(self.groupBox_clean)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font13)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_clean)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font13)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_3)


        self.gridLayout_5.addWidget(self.groupBox_clean, 0, 0, 1, 1)

        self.lab_clean = QLabel(self.page_deck_clean)
        self.lab_clean.setObjectName(u"lab_clean")
        self.lab_clean.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lab_clean, 0, 1, 2, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 2, 1)

        self.groupBox = QGroupBox(self.page_deck_clean)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 300))
        self.groupBox.setMaximumSize(QSize(250, 300))
        self.groupBox.setFont(font13)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(0,143,170);\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 0, 0, 1, 1)

        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: red;\n"
"    width:5px\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background:rgb(0,143,170);\n"
"	margin:0 -8px\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_6.addWidget(self.verticalSlider, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 3, 1, 1)

        self.stackedWidget_deck.addWidget(self.page_deck_clean)
        self.page_deck_advance = QWidget()
        self.page_deck_advance.setObjectName(u"page_deck_advance")
        self.page_deck_advance.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_deck_advance)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_advance_display = QFrame(self.page_deck_advance)
        self.frame_advance_display.setObjectName(u"frame_advance_display")
        self.verticalLayout_18 = QVBoxLayout(self.frame_advance_display)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_advance_display_search = QFrame(self.frame_advance_display)
        self.frame_advance_display_search.setObjectName(u"frame_advance_display_search")
        self.layout_deck_advance_display_query = QHBoxLayout(self.frame_advance_display_search)
        self.layout_deck_advance_display_query.setObjectName(u"layout_deck_advance_display_query")
        self.label_advance_display_search = QLabel(self.frame_advance_display_search)
        self.label_advance_display_search.setObjectName(u"label_advance_display_search")
        self.label_advance_display_search.setFont(font11)
        self.label_advance_display_search.setStyleSheet(u"color:rgb(255,255,255);")

        self.layout_deck_advance_display_query.addWidget(self.label_advance_display_search)

        self.line_advance_display_search = QLineEdit(self.frame_advance_display_search)
        self.line_advance_display_search.setObjectName(u"line_advance_display_search")
        self.line_advance_display_search.setStyleSheet(u"color:rgb(255,255,255);")

        self.layout_deck_advance_display_query.addWidget(self.line_advance_display_search)

        self.bn_advance_display_search = QPushButton(self.frame_advance_display_search)
        self.bn_advance_display_search.setObjectName(u"bn_advance_display_search")
        self.bn_advance_display_search.setMaximumSize(QSize(50, 16777215))
        self.bn_advance_display_search.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.layout_deck_advance_display_query.addWidget(self.bn_advance_display_search)


        self.verticalLayout_18.addWidget(self.frame_advance_display_search)

        self.scrollArea_advance_display_tweets = QScrollArea(self.frame_advance_display)
        self.scrollArea_advance_display_tweets.setObjectName(u"scrollArea_advance_display_tweets")
        self.scrollArea_advance_display_tweets.setWidgetResizable(True)
        self.scrollAreaWidgetContents_advance_display_query_tweets = QWidget()
        self.scrollAreaWidgetContents_advance_display_query_tweets.setObjectName(u"scrollAreaWidgetContents_advance_display_query_tweets")
        self.scrollAreaWidgetContents_advance_display_query_tweets.setGeometry(QRect(0, 0, 440, 379))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_advance_display_query_tweets)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.text_advance_display_query_tweet0 = QTextEdit(self.scrollAreaWidgetContents_advance_display_query_tweets)
        self.text_advance_display_query_tweet0.setObjectName(u"text_advance_display_query_tweet0")
        sizePolicy2.setHeightForWidth(self.text_advance_display_query_tweet0.sizePolicy().hasHeightForWidth())
        self.text_advance_display_query_tweet0.setSizePolicy(sizePolicy2)
        self.text_advance_display_query_tweet0.setMinimumSize(QSize(300, 0))
        self.text_advance_display_query_tweet0.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_20.addWidget(self.text_advance_display_query_tweet0)

        self.text_advance_display_query_tweet1 = QTextEdit(self.scrollAreaWidgetContents_advance_display_query_tweets)
        self.text_advance_display_query_tweet1.setObjectName(u"text_advance_display_query_tweet1")
        sizePolicy2.setHeightForWidth(self.text_advance_display_query_tweet1.sizePolicy().hasHeightForWidth())
        self.text_advance_display_query_tweet1.setSizePolicy(sizePolicy2)
        self.text_advance_display_query_tweet1.setMinimumSize(QSize(300, 0))
        self.text_advance_display_query_tweet1.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_20.addWidget(self.text_advance_display_query_tweet1)

        self.scrollArea_advance_display_tweets.setWidget(self.scrollAreaWidgetContents_advance_display_query_tweets)

        self.verticalLayout_18.addWidget(self.scrollArea_advance_display_tweets, 0, Qt.AlignTop)


        self.horizontalLayout_27.addWidget(self.frame_advance_display)

        self.frame_advance_config = QFrame(self.page_deck_advance)
        self.frame_advance_config.setObjectName(u"frame_advance_config")
        self.verticalLayout = QVBoxLayout(self.frame_advance_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_deck_advance_content = QGroupBox(self.frame_advance_config)
        self.groupBox_deck_advance_content.setObjectName(u"groupBox_deck_advance_content")
        self.groupBox_deck_advance_content.setMinimumSize(QSize(250, 150))
        self.groupBox_deck_advance_content.setMaximumSize(QSize(250, 300))
        self.groupBox_deck_advance_content.setSizeIncrement(QSize(0, 0))
        self.groupBox_deck_advance_content.setFont(font2)
        self.groupBox_deck_advance_content.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_deck_advance_content.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_deck_advance_content.setFlat(False)
        self.groupBox_deck_advance_content.setCheckable(False)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_deck_advance_content)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_deck_advance_content_include = QHBoxLayout()
        self.frame_deck_advance_content_include.setObjectName(u"frame_deck_advance_content_include")
        self.frame_deck_advance_content_include.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_content_include = QLabel(self.groupBox_deck_advance_content)
        self.label_content_include.setObjectName(u"label_content_include")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_content_include.sizePolicy().hasHeightForWidth())
        self.label_content_include.setSizePolicy(sizePolicy3)
        self.label_content_include.setMinimumSize(QSize(50, 20))
        self.label_content_include.setMaximumSize(QSize(16777215, 20))
        self.label_content_include.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_deck_advance_content_include.addWidget(self.label_content_include)

        self.line_deck_advance_content_include = QLineEdit(self.groupBox_deck_advance_content)
        self.line_deck_advance_content_include.setObjectName(u"line_deck_advance_content_include")
        sizePolicy2.setHeightForWidth(self.line_deck_advance_content_include.sizePolicy().hasHeightForWidth())
        self.line_deck_advance_content_include.setSizePolicy(sizePolicy2)
        self.line_deck_advance_content_include.setMaximumSize(QSize(16777215, 20))
        self.line_deck_advance_content_include.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.frame_deck_advance_content_include.addWidget(self.line_deck_advance_content_include)


        self.verticalLayout_21.addLayout(self.frame_deck_advance_content_include)

        self.frame_deck_advance_content_exclude = QHBoxLayout()
        self.frame_deck_advance_content_exclude.setObjectName(u"frame_deck_advance_content_exclude")
        self.label_content_exclude = QLabel(self.groupBox_deck_advance_content)
        self.label_content_exclude.setObjectName(u"label_content_exclude")
        sizePolicy3.setHeightForWidth(self.label_content_exclude.sizePolicy().hasHeightForWidth())
        self.label_content_exclude.setSizePolicy(sizePolicy3)
        self.label_content_exclude.setMinimumSize(QSize(50, 20))
        self.label_content_exclude.setMaximumSize(QSize(16777215, 20))
        self.label_content_exclude.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_deck_advance_content_exclude.addWidget(self.label_content_exclude)

        self.line_deck_advance_content_exclude = QLineEdit(self.groupBox_deck_advance_content)
        self.line_deck_advance_content_exclude.setObjectName(u"line_deck_advance_content_exclude")
        sizePolicy2.setHeightForWidth(self.line_deck_advance_content_exclude.sizePolicy().hasHeightForWidth())
        self.line_deck_advance_content_exclude.setSizePolicy(sizePolicy2)
        self.line_deck_advance_content_exclude.setMaximumSize(QSize(16777215, 20))
        self.line_deck_advance_content_exclude.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.frame_deck_advance_content_exclude.addWidget(self.line_deck_advance_content_exclude)


        self.verticalLayout_21.addLayout(self.frame_deck_advance_content_exclude)

        self.radio_deck_advance_content_include = QRadioButton(self.groupBox_deck_advance_content)
        self.radio_deck_advance_content_include.setObjectName(u"radio_deck_advance_content_include")
        self.radio_deck_advance_content_include.setFont(font13)
        self.radio_deck_advance_content_include.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radio_deck_advance_content_include.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.radio_deck_advance_content_include)


        self.verticalLayout.addWidget(self.groupBox_deck_advance_content)

        self.groupBox_deck_advance_user = QGroupBox(self.frame_advance_config)
        self.groupBox_deck_advance_user.setObjectName(u"groupBox_deck_advance_user")
        self.groupBox_deck_advance_user.setMinimumSize(QSize(0, 150))
        self.groupBox_deck_advance_user.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_deck_advance_user)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_deck_advance_user_followRange = QHBoxLayout()
        self.frame_deck_advance_user_followRange.setObjectName(u"frame_deck_advance_user_followRange")
        self.frame_deck_advance_user_followRange.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_deck_advance_user_followRange = QLabel(self.groupBox_deck_advance_user)
        self.label_deck_advance_user_followRange.setObjectName(u"label_deck_advance_user_followRange")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_deck_advance_user_followRange.sizePolicy().hasHeightForWidth())
        self.label_deck_advance_user_followRange.setSizePolicy(sizePolicy4)
        self.label_deck_advance_user_followRange.setMinimumSize(QSize(50, 50))
        self.label_deck_advance_user_followRange.setMaximumSize(QSize(16777215, 50))
        font14 = QFont()
        font14.setPointSize(10)
        self.label_deck_advance_user_followRange.setFont(font14)
        self.label_deck_advance_user_followRange.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.frame_deck_advance_user_followRange.addWidget(self.label_deck_advance_user_followRange)

        self.spin_deck_advance_user_followRange_low = QSpinBox(self.groupBox_deck_advance_user)
        self.spin_deck_advance_user_followRange_low.setObjectName(u"spin_deck_advance_user_followRange_low")
        self.spin_deck_advance_user_followRange_low.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.frame_deck_advance_user_followRange.addWidget(self.spin_deck_advance_user_followRange_low)

        self.spin_deck_advance_user_followRange_hi = QSpinBox(self.groupBox_deck_advance_user)
        self.spin_deck_advance_user_followRange_hi.setObjectName(u"spin_deck_advance_user_followRange_hi")
        self.spin_deck_advance_user_followRange_hi.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.frame_deck_advance_user_followRange.addWidget(self.spin_deck_advance_user_followRange_hi)


        self.verticalLayout_24.addLayout(self.frame_deck_advance_user_followRange)

        self.frame_deck_advance_user_id = QFrame(self.groupBox_deck_advance_user)
        self.frame_deck_advance_user_id.setObjectName(u"frame_deck_advance_user_id")
        self.layout_deck_advance_user_id = QHBoxLayout(self.frame_deck_advance_user_id)
        self.layout_deck_advance_user_id.setObjectName(u"layout_deck_advance_user_id")
        self.label_deck_advance_user_id = QLabel(self.frame_deck_advance_user_id)
        self.label_deck_advance_user_id.setObjectName(u"label_deck_advance_user_id")
        sizePolicy3.setHeightForWidth(self.label_deck_advance_user_id.sizePolicy().hasHeightForWidth())
        self.label_deck_advance_user_id.setSizePolicy(sizePolicy3)
        self.label_deck_advance_user_id.setMinimumSize(QSize(50, 20))
        self.label_deck_advance_user_id.setMaximumSize(QSize(16777215, 20))
        self.label_deck_advance_user_id.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.layout_deck_advance_user_id.addWidget(self.label_deck_advance_user_id)

        self.line_deck_advance_user_id = QLineEdit(self.frame_deck_advance_user_id)
        self.line_deck_advance_user_id.setObjectName(u"line_deck_advance_user_id")
        sizePolicy2.setHeightForWidth(self.line_deck_advance_user_id.sizePolicy().hasHeightForWidth())
        self.line_deck_advance_user_id.setSizePolicy(sizePolicy2)
        self.line_deck_advance_user_id.setMaximumSize(QSize(16777215, 20))
        self.line_deck_advance_user_id.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.layout_deck_advance_user_id.addWidget(self.line_deck_advance_user_id)


        self.verticalLayout_24.addWidget(self.frame_deck_advance_user_id)


        self.verticalLayout.addWidget(self.groupBox_deck_advance_user)

        self.bn_deck_advance_filter = QPushButton(self.frame_advance_config)
        self.bn_deck_advance_filter.setObjectName(u"bn_deck_advance_filter")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bn_deck_advance_filter.sizePolicy().hasHeightForWidth())
        self.bn_deck_advance_filter.setSizePolicy(sizePolicy5)
        self.bn_deck_advance_filter.setFont(font8)
        self.bn_deck_advance_filter.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.bn_deck_advance_filter)

        self.bn_deck_advance_apply = QPushButton(self.frame_advance_config)
        self.bn_deck_advance_apply.setObjectName(u"bn_deck_advance_apply")
        sizePolicy5.setHeightForWidth(self.bn_deck_advance_apply.sizePolicy().hasHeightForWidth())
        self.bn_deck_advance_apply.setSizePolicy(sizePolicy5)
        self.bn_deck_advance_apply.setMinimumSize(QSize(10, 0))
        self.bn_deck_advance_apply.setFont(font8)
        self.bn_deck_advance_apply.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.bn_deck_advance_apply)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout_27.addWidget(self.frame_advance_config)

        self.stackedWidget_deck.addWidget(self.page_deck_advance)

        self.verticalLayout_9.addWidget(self.stackedWidget_deck)

        self.stackedWidget.addWidget(self.page_deck)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font15)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font16 = QFont()
        font16.setFamily(u"Segoe UI Light")
        font16.setPointSize(10)
        self.lab_tab.setFont(font16)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(20, 20))
        self.frame_drag.setMaximumSize(QSize(20, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout_23.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)
        self.stackedWidget_deck.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toodle.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Admin</span></p></body></html>", None))
        self.lab_person.setText("")
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.bn_max.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_news.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_news.setText("")
#if QT_CONFIG(tooltip)
        self.bn_login.setToolTip(QCoreApplication.translate("MainWindow", u"Cloud", None))
#endif // QT_CONFIG(tooltip)
        self.bn_login.setText("")
#if QT_CONFIG(tooltip)
        self.bn_deck.setToolTip(QCoreApplication.translate("MainWindow", u"Android", None))
#endif // QT_CONFIG(tooltip)
        self.bn_deck.setText("")
        self.btn_extend.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Profile</span></p></body></html>", None))
        self.lab_home_main_disc.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Name:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Age:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /"
                        "></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Adress:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Managememt :Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum i"
                        "ure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</span></p></body></html>", None))
        self.lab_home_stat_hed.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stat </span></p></body></html>", None))
        self.lab_home_stat_disc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Weather: Rainy<br/>Skys: Cloudy<br/>Wind: blowing Fast<br/>Temperature: 32 Degree Celcious</span></p></body></html>", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.lab_Bug.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Bugs Found</span></p></body></html>", None))
        self.comboBox_news.setItemText(0, QCoreApplication.translate("MainWindow", u"100000", None))
        self.comboBox_news.setItemText(1, QCoreApplication.translate("MainWindow", u"1000000", None))
        self.comboBox_news.setItemText(2, QCoreApplication.translate("MainWindow", u"10000000", None))
        self.comboBox_news.setItemText(3, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.bn_news_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lab_login_main.setText(QCoreApplication.translate("MainWindow", u"Login Page", None))
        self.bn_login_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_login_id.setText(QCoreApplication.translate("MainWindow", u"ID :", None))
        self.label_login_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.bn_login_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.bn_login_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
#if QT_CONFIG(tooltip)
        self.bn_deck_event.setToolTip(QCoreApplication.translate("MainWindow", u"Contact", None))
#endif // QT_CONFIG(tooltip)
        self.bn_deck_event.setText("")
#if QT_CONFIG(tooltip)
        self.bn_deck_query.setToolTip(QCoreApplication.translate("MainWindow", u"GamePad", None))
#endif // QT_CONFIG(tooltip)
        self.bn_deck_query.setText("")
#if QT_CONFIG(tooltip)
        self.bn_deck_advance.setToolTip(QCoreApplication.translate("MainWindow", u"World", None))
#endif // QT_CONFIG(tooltip)
        self.bn_deck_advance.setText("")
#if QT_CONFIG(tooltip)
        self.bn_deck_clean.setToolTip(QCoreApplication.translate("MainWindow", u"Clean", None))
#endif // QT_CONFIG(tooltip)
        self.bn_deck_clean.setText("")
        self.label_event_title.setText(QCoreApplication.translate("MainWindow", u" Crisis Event", None))
        self.lab_person_icon.setText("")
        self.combo_event_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Earthquake", None))
        self.combo_event_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Volcano", None))
        self.combo_event_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Floods", None))

        self.line_event_location.setText(QCoreApplication.translate("MainWindow", u"California, USA", None))
        self.label_event_since.setText(QCoreApplication.translate("MainWindow", u"Since", None))
        self.label_event_type.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_event_location.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.bn_deck_event_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_deck_event_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_deck_event_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_event_till.setText(QCoreApplication.translate("MainWindow", u"Till", None))
        self.label_query_0.setText(QCoreApplication.translate("MainWindow", u"Query:", None))
        self.line_query_0.setText(QCoreApplication.translate("MainWindow", u"FOOD AND RESOURCE", None))
        self.bn_query_0_enter.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.bn_query_0_advance.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.text__query_0_tweets0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">@9NewsAUS</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">JUST IN: Tsunami warning has been dropped for all countries, except </span><span style=\" font-size:14px; color:#1da1f2;\">#Chil"
                        "e</span><span style=\" font-size:14px;\"> and </span><span style=\" font-size:14px; color:#1da1f2;\">#Peru</span><span style=\" font-size:14px;\">. </span><span style=\" font-size:14px; color:#1da1f2;\">#9News</span><span style=\" font-size:14px;\"> huh? Terribly written tweet? </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color:#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.text__query_0_tweets1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">User</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Sending and surrounding the beings of </span><span style=\" font-size:14px; color:#1da1f2;\">#Chile</span><span style=\" font-size:14"
                        "px;\"> with an abundance of love, light and prayers... May all be safe. </span><span style=\" font-size:14px; color:#1da1f2;\">#earthquake</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#tsunami</span><span style=\" font-size:14px;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color:#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.text__query_0_tweets2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">User</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Sending and surrounding the beings of </span><span style=\" font-size:14px; color:#1da1f2;\">#Chile</span><span style=\" font-size:14"
                        "px;\"> with an abundance of love, light and prayers... May all be safe. </span><span style=\" font-size:14px; color:#1da1f2;\">#earthquake</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#tsunami</span><span style=\" font-size:14px;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color:#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.label_query_1.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.line_query_1.setText(QCoreApplication.translate("MainWindow", u"MISSING PEOPLE", None))
        self.bn_query_1_enter.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.bn_query_1_advance.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.text__query_1_tweets0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">@Vallie</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" f"
                        "ont-size:14px; text-decoration: underline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:14px;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color:#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.text__query_1_tweets1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">@Euphorian54</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">RT </span><span style=\" font-size:14px; font-weight:700;\">@debbiegibson</span><span style=\" font-size:14px;\"> &amp; </spa"
                        "n><span style=\" font-size:14px; color:#1da1f2;\">#TeamDeb</span><span style=\" font-size:14px;\"> for </span><span style=\" font-size:14px; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:14px;\"> &amp; </span><span style=\" font-size:14px; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:14px;\"> ! </span><span style=\" font-size:14px; color:#1da1f2;\">#chile</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#santiago</span><span style=\" font-size:14px;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:14px; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:14px;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color"
                        ":#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.groupBox_clean.setTitle(QCoreApplication.translate("MainWindow", u"Review", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Clean History", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Clean Password", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Clean Chache", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Clean Bookmarks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Did you liked the UI", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Did you like the Color Scheme", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Did you like Custome Buttons", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Did you like the Stacked Window", None))
        self.lab_clean.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sliders", None))
        self.label_advance_display_search.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.bn_advance_display_search.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.text_advance_display_query_tweet0.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">@Vallie</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" f"
                        "ont-size:14px; text-decoration: underline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:14px;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color:#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.text_advance_display_query_tweet1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" alt=\"User Avatar\" /> <span style=\" font-weight:700;\">@Euphorian54</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">RT </span><span style=\" font-size:14px; font-weight:700;\">@debbiegibson</span><span style=\" font-size:14px;\"> &amp; </spa"
                        "n><span style=\" font-size:14px; color:#1da1f2;\">#TeamDeb</span><span style=\" font-size:14px;\"> for </span><span style=\" font-size:14px; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:14px;\"> &amp; </span><span style=\" font-size:14px; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:14px;\"> ! </span><span style=\" font-size:14px; color:#1da1f2;\">#chile</span><span style=\" font-size:14px;\"> </span><span style=\" font-size:14px; color:#1da1f2;\">#santiago</span><span style=\" font-size:14px;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:14px; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:14px;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#1da1f2;\">Like</span> <span style=\" color"
                        ":#1da1f2;\">Retweet</span> </p></body></html>", None))
        self.groupBox_deck_advance_content.setTitle(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_content_include.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_content_exclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.radio_deck_advance_content_include.setText(QCoreApplication.translate("MainWindow", u"Retweet", None))
        self.groupBox_deck_advance_user.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_deck_advance_user_followRange.setText(QCoreApplication.translate("MainWindow", u"Follwers \n"
" Range", None))
        self.label_deck_advance_user_id.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.bn_deck_advance_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.bn_deck_advance_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

