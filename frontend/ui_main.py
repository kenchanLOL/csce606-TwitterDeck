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

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_bug = QPushButton(self.frame_bug)
        self.bn_bug.setObjectName(u"bn_bug")
        self.bn_bug.setMinimumSize(QSize(80, 55))
        self.bn_bug.setMaximumSize(QSize(160, 55))
        self.bn_bug.setStyleSheet(u"QPushButton {\n"
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
        self.bn_bug.setIcon(icon5)
        self.bn_bug.setIconSize(QSize(22, 22))
        self.bn_bug.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_bug)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bn_cloud = QPushButton(self.frame_cloud)
        self.bn_cloud.setObjectName(u"bn_cloud")
        self.bn_cloud.setMinimumSize(QSize(80, 55))
        self.bn_cloud.setMaximumSize(QSize(160, 55))
        self.bn_cloud.setStyleSheet(u"QPushButton {\n"
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
        self.bn_cloud.setIcon(icon6)
        self.bn_cloud.setIconSize(QSize(22, 12))
        self.bn_cloud.setFlat(True)

        self.horizontalLayout_17.addWidget(self.bn_cloud)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_android = QFrame(self.frame_bottom_west)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_android)
        self.bn_android.setObjectName(u"bn_android")
        self.bn_android.setMinimumSize(QSize(80, 55))
        self.bn_android.setMaximumSize(QSize(160, 55))
        self.bn_android.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android.setIcon(icon5)
        self.bn_android.setIconSize(QSize(20, 22))
        self.bn_android.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_android)


        self.verticalLayout_3.addWidget(self.frame_android)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)


        self.verticalLayout_3.addWidget(self.frame_8)


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
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_cloud)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(30)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug = QWidget()
        self.page_bug.setObjectName(u"page_bug")
        self.page_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.lab_Bug = QLabel(self.page_bug)
        self.lab_Bug.setObjectName(u"lab_Bug")
        self.lab_Bug.setMinimumSize(QSize(0, 55))
        self.lab_Bug.setMaximumSize(QSize(16777215, 55))
        self.lab_Bug.setFont(font1)
        self.lab_Bug.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_7.addWidget(self.lab_Bug)

        self.frame_bug_main = QFrame(self.page_bug)
        self.frame_bug_main.setObjectName(u"frame_bug_main")
        self.frame_bug_main.setMinimumSize(QSize(0, 200))
        self.frame_bug_main.setMaximumSize(QSize(16777215, 200))
        self.frame_bug_main.setFrameShape(QFrame.NoFrame)
        self.frame_bug_main.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_bug_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(421, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 7, 1, 1)

        self.lab_bullet = QLabel(self.frame_bug_main)
        self.lab_bullet.setObjectName(u"lab_bullet")
        self.lab_bullet.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))
        self.lab_bullet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_bullet, 0, 0, 1, 1)

        self.lab_bullet3 = QLabel(self.frame_bug_main)
        self.lab_bullet3.setObjectName(u"lab_bullet3")
        self.lab_bullet3.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet3.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet3, 2, 0, 1, 1)

        self.lab_bug2 = QLabel(self.frame_bug_main)
        self.lab_bug2.setObjectName(u"lab_bug2")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        self.lab_bug2.setFont(font5)
        self.lab_bug2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout.addWidget(self.lab_bug2, 1, 1, 1, 1)

        self.lab_bug3 = QLabel(self.frame_bug_main)
        self.lab_bug3.setObjectName(u"lab_bug3")
        self.lab_bug3.setFont(font5)

        self.gridLayout.addWidget(self.lab_bug3, 2, 1, 1, 1)

        self.comboBox_bug = QComboBox(self.frame_bug_main)
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.addItem("")
        self.comboBox_bug.setObjectName(u"comboBox_bug")
        self.comboBox_bug.setMaximumSize(QSize(16777215, 25))
        self.comboBox_bug.setFont(font2)
        self.comboBox_bug.setStyleSheet(u"QComboBox {\n"
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
        self.comboBox_bug.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_bug.setFrame(False)
        self.comboBox_bug.setModelColumn(0)

        self.gridLayout.addWidget(self.comboBox_bug, 3, 8, 1, 1)

        self.lab_bug1 = QLabel(self.frame_bug_main)
        self.lab_bug1.setObjectName(u"lab_bug1")
        self.lab_bug1.setMinimumSize(QSize(0, 0))
        self.lab_bug1.setMaximumSize(QSize(16777215, 16777215))
        self.lab_bug1.setFont(font5)
        self.lab_bug1.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_bug1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lab_bug1, 0, 1, 1, 1)

        self.lab_bullet2 = QLabel(self.frame_bug_main)
        self.lab_bullet2.setObjectName(u"lab_bullet2")
        self.lab_bullet2.setMaximumSize(QSize(5, 16777215))
        self.lab_bullet2.setPixmap(QPixmap(u"icons/1x/bulletAsset 54.png"))

        self.gridLayout.addWidget(self.lab_bullet2, 1, 0, 1, 1)

        self.bn_bug_start = QPushButton(self.frame_bug_main)
        self.bn_bug_start.setObjectName(u"bn_bug_start")
        self.bn_bug_start.setMinimumSize(QSize(69, 25))
        self.bn_bug_start.setMaximumSize(QSize(69, 25))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        self.bn_bug_start.setFont(font6)
        self.bn_bug_start.setStyleSheet(u"QPushButton {\n"
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
        self.bn_bug_start.setCheckable(False)
        self.bn_bug_start.setFlat(True)

        self.gridLayout.addWidget(self.bn_bug_start, 3, 9, 1, 1)

        self.progressBar_bug = QProgressBar(self.frame_bug_main)
        self.progressBar_bug.setObjectName(u"progressBar_bug")
        self.progressBar_bug.setEnabled(True)
        self.progressBar_bug.setStyleSheet(u"QProgressBar\n"
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
        self.progressBar_bug.setValue(0)
        self.progressBar_bug.setAlignment(Qt.AlignCenter)
        self.progressBar_bug.setTextVisible(True)
        self.progressBar_bug.setOrientation(Qt.Horizontal)
        self.progressBar_bug.setInvertedAppearance(False)
        self.progressBar_bug.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar_bug, 4, 7, 1, 3)

        self.lab_bug_action = QLabel(self.frame_bug_main)
        self.lab_bug_action.setObjectName(u"lab_bug_action")
        self.lab_bug_action.setMinimumSize(QSize(0, 20))
        self.lab_bug_action.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(16)
        self.lab_bug_action.setFont(font7)
        self.lab_bug_action.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_bug_action.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lab_bug_action, 3, 7, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_bug_main)

        self.verticalSpacer = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_bug)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.page_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.lab_cloud_main = QLabel(self.page_cloud)
        self.lab_cloud_main.setObjectName(u"lab_cloud_main")
        self.lab_cloud_main.setMinimumSize(QSize(0, 55))
        self.lab_cloud_main.setMaximumSize(QSize(16777215, 55))
        self.lab_cloud_main.setFont(font3)
        self.lab_cloud_main.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")

        self.verticalLayout_8.addWidget(self.lab_cloud_main)

        self.frame_2 = QFrame(self.page_cloud)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 235))
        self.frame_2.setMaximumSize(QSize(16777215, 235))
        self.frame_2.setFont(font6)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 2)

        self.bn_cloud_connect = QPushButton(self.frame_2)
        self.bn_cloud_connect.setObjectName(u"bn_cloud_connect")
        self.bn_cloud_connect.setMinimumSize(QSize(69, 25))
        self.bn_cloud_connect.setMaximumSize(QSize(69, 25))
        self.bn_cloud_connect.setFont(font6)
        self.bn_cloud_connect.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.bn_cloud_connect, 2, 4, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.line_cloud_id = QLineEdit(self.frame_2)
        self.line_cloud_id.setObjectName(u"line_cloud_id")
        self.line_cloud_id.setEnabled(True)
        self.line_cloud_id.setMinimumSize(QSize(400, 25))
        self.line_cloud_id.setMaximumSize(QSize(500, 25))
        self.line_cloud_id.setFont(font6)
        self.line_cloud_id.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.line_cloud_id, 0, 1, 1, 4)

        self.bn_cloud_clear = QPushButton(self.frame_2)
        self.bn_cloud_clear.setObjectName(u"bn_cloud_clear")
        self.bn_cloud_clear.setEnabled(True)
        self.bn_cloud_clear.setMinimumSize(QSize(69, 25))
        self.bn_cloud_clear.setMaximumSize(QSize(69, 25))
        self.bn_cloud_clear.setFont(font6)
        self.bn_cloud_clear.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.bn_cloud_clear, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 6, 1, 1)

        self.line_cloud_adress = QLineEdit(self.frame_2)
        self.line_cloud_adress.setObjectName(u"line_cloud_adress")
        self.line_cloud_adress.setMinimumSize(QSize(400, 25))
        self.line_cloud_adress.setMaximumSize(QSize(500, 25))
        self.line_cloud_adress.setFont(font6)
        self.line_cloud_adress.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_2.addWidget(self.line_cloud_adress, 1, 1, 1, 4)

        self.bn_cloud_register = QPushButton(self.frame_2)
        self.bn_cloud_register.setObjectName(u"bn_cloud_register")
        self.bn_cloud_register.setMinimumSize(QSize(69, 25))
        self.bn_cloud_register.setMaximumSize(QSize(69, 25))
        font8 = QFont()
        font8.setPointSize(12)
        self.bn_cloud_register.setFont(font8)
        self.bn_cloud_register.setMouseTracking(True)
        self.bn_cloud_register.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.bn_cloud_register, 2, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 162, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_deck = QWidget()
        self.page_deck.setObjectName(u"page_deck")
        self.page_deck.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_deck)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_android_menu = QFrame(self.page_deck)
        self.frame_android_menu.setObjectName(u"frame_android_menu")
        self.frame_android_menu.setMinimumSize(QSize(0, 30))
        self.frame_android_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_android_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_android_menu.setFrameShape(QFrame.NoFrame)
        self.frame_android_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_android_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_android_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_android_contact = QPushButton(self.frame_android_contact)
        self.bn_android_contact.setObjectName(u"bn_android_contact")
        self.bn_android_contact.setMinimumSize(QSize(80, 30))
        self.bn_android_contact.setMaximumSize(QSize(80, 30))
        self.bn_android_contact.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_contact.setIcon(icon5)
        self.bn_android_contact.setIconSize(QSize(13, 16))
        self.bn_android_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_android_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_android_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_android_game = QPushButton(self.frame_android_game)
        self.bn_android_game.setObjectName(u"bn_android_game")
        self.bn_android_game.setMinimumSize(QSize(80, 30))
        self.bn_android_game.setMaximumSize(QSize(80, 30))
        self.bn_android_game.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_game.setIcon(icon5)
        self.bn_android_game.setIconSize(QSize(20, 13))
        self.bn_android_game.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_android_game)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.frame_android_world = QFrame(self.frame_android_menu)
        self.frame_android_world.setObjectName(u"frame_android_world")
        self.frame_android_world.setMinimumSize(QSize(80, 30))
        self.frame_android_world.setMaximumSize(QSize(80, 30))
        self.frame_android_world.setFrameShape(QFrame.NoFrame)
        self.frame_android_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_android_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_android_world = QPushButton(self.frame_android_world)
        self.bn_android_world.setObjectName(u"bn_android_world")
        self.bn_android_world.setMinimumSize(QSize(80, 30))
        self.bn_android_world.setMaximumSize(QSize(80, 30))
        self.bn_android_world.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_world.setIcon(icon5)
        self.bn_android_world.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_android_world)


        self.horizontalLayout_20.addWidget(self.frame_android_world)

        self.frame_android_clean = QFrame(self.frame_android_menu)
        self.frame_android_clean.setObjectName(u"frame_android_clean")
        self.frame_android_clean.setMinimumSize(QSize(80, 30))
        self.frame_android_clean.setMaximumSize(QSize(80, 30))
        self.frame_android_clean.setFrameShape(QFrame.NoFrame)
        self.frame_android_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_android_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_android_clean = QPushButton(self.frame_android_clean)
        self.bn_android_clean.setObjectName(u"bn_android_clean")
        self.bn_android_clean.setMinimumSize(QSize(80, 30))
        self.bn_android_clean.setMaximumSize(QSize(80, 30))
        self.bn_android_clean.setStyleSheet(u"QPushButton {\n"
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
        icon7.addFile(u"icons/1x/bugAsset 47.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_clean.setIcon(icon7)
        self.bn_android_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.bn_android_clean)


        self.horizontalLayout_20.addWidget(self.frame_android_clean)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_android_menu)

        self.stackedWidget_android = QStackedWidget(self.page_deck)
        self.stackedWidget_android.setObjectName(u"stackedWidget_android")
        self.stackedWidget_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font3)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/placeholder.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.comboBox = QComboBox(self.frame_android_field)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font9 = QFont()
        font9.setPointSize(15)
        self.comboBox.setFont(font9)

        self.gridLayout_4.addWidget(self.comboBox, 6, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 8, 8, 1, 1)

        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")
        self.line_android_name.setEnabled(False)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 16777215))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(20)
        self.line_android_name.setFont(font10)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_4.addWidget(self.line_android_name, 1, 3, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font10)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font10)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 9, 3, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.frame_android_field)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(0, 0))
        self.dateTimeEdit.setFont(font9)

        self.gridLayout_4.addWidget(self.dateTimeEdit, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 6, 8, 1, 1)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font10)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.bn_android_contact_edit = QPushButton(self.frame_3)
        self.bn_android_contact_edit.setObjectName(u"bn_android_contact_edit")
        self.bn_android_contact_edit.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_edit.setMaximumSize(QSize(69, 25))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(15)
        self.bn_android_contact_edit.setFont(font11)
        self.bn_android_contact_edit.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_edit)

        self.bn_android_contact_share = QPushButton(self.frame_3)
        self.bn_android_contact_share.setObjectName(u"bn_android_contact_share")
        self.bn_android_contact_share.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_share.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_share.setFont(font11)
        self.bn_android_contact_share.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_share)

        self.bn_android_contact_delete = QPushButton(self.frame_3)
        self.bn_android_contact_delete.setObjectName(u"bn_android_contact_delete")
        self.bn_android_contact_delete.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_delete.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_delete.setFont(font11)
        self.bn_android_contact_delete.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_delete)

        self.bn_android_contact_save = QPushButton(self.frame_3)
        self.bn_android_contact_save.setObjectName(u"bn_android_contact_save")
        self.bn_android_contact_save.setEnabled(False)
        self.bn_android_contact_save.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_save.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_save.setFont(font11)
        self.bn_android_contact_save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_25.addWidget(self.bn_android_contact_save)


        self.gridLayout_4.addWidget(self.frame_3, 8, 0, 1, 7)

        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        font12 = QFont()
        font12.setPointSize(20)
        self.label_8.setFont(font12)
        self.label_8.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_android_field)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setFont(font9)

        self.gridLayout_4.addWidget(self.dateTimeEdit_2, 4, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_4 = QLabel(self.frame_textbar)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font13 = QFont()
        font13.setPointSize(20)
        font13.setBold(False)
        self.label_4.setFont(font13)
        self.label_4.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.frame_textbar)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_30.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_textbar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.pushButton)

        self.toolButton = QToolButton(self.frame_textbar)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_30.addWidget(self.toolButton)


        self.verticalLayout_15.addLayout(self.horizontalLayout_30)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_15.addLayout(self.verticalLayout_19)

        self.scrollArea = QScrollArea(self.frame_textbar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 331, 480))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(300, 150))
        self.textEdit.setMaximumSize(QSize(350, 16777215))
        self.textEdit.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.textEdit)

        self.textEdit_5 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_5.setObjectName(u"textEdit_5")
        sizePolicy1.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy1)
        self.textEdit_5.setMinimumSize(QSize(300, 150))
        self.textEdit_5.setMaximumSize(QSize(350, 16777215))
        self.textEdit_5.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.textEdit_5)

        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMinimumSize(QSize(300, 150))
        self.textEdit_2.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_14.addWidget(self.textEdit_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea)


        self.horizontalLayout_26.addLayout(self.verticalLayout_15)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_7 = QLabel(self.frame_textbar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font12)
        self.label_7.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.frame_textbar)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_31.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.frame_textbar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_31.addWidget(self.pushButton_2)

        self.toolButton_2 = QToolButton(self.frame_textbar)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_31.addWidget(self.toolButton_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_31)

        self.scrollArea_2 = QScrollArea(self.frame_textbar)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 330, 408))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy2)
        self.textEdit_3.setMinimumSize(QSize(300, 0))
        self.textEdit_3.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_16.addWidget(self.textEdit_3)

        self.textEdit_4 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy2.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy2)
        self.textEdit_4.setMinimumSize(QSize(300, 0))
        self.textEdit_4.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_16.addWidget(self.textEdit_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_17.addWidget(self.scrollArea_2)


        self.horizontalLayout_26.addLayout(self.verticalLayout_17)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_android.addWidget(self.page_android_game)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName(u"page_android_clean")
        self.page_android_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.groupBox_clean = QGroupBox(self.page_android_clean)
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
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(9)
        self.radioButton.setFont(font14)
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
        self.radioButton_2.setFont(font14)
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
        self.radioButton_3.setFont(font14)
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
        self.radioButton_4.setFont(font14)
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
        self.checkBox.setFont(font14)
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
        self.checkBox_4.setFont(font14)
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
        self.checkBox_2.setFont(font14)
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
        self.checkBox_3.setFont(font14)
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

        self.lab_clean = QLabel(self.page_android_clean)
        self.lab_clean.setObjectName(u"lab_clean")
        self.lab_clean.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lab_clean, 0, 1, 2, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 2, 1)

        self.groupBox = QGroupBox(self.page_android_clean)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 300))
        self.groupBox.setMaximumSize(QSize(250, 300))
        self.groupBox.setFont(font14)
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

        self.stackedWidget_android.addWidget(self.page_android_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName(u"page_android_world")
        self.page_android_world.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_9 = QLabel(self.page_android_world)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font12)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_32.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.page_android_world)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_32.addWidget(self.lineEdit_3)

        self.pushButton_3 = QPushButton(self.page_android_world)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_32.addWidget(self.pushButton_3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_32)

        self.scrollArea_3 = QScrollArea(self.page_android_world)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 423, 408))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy2.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy2)
        self.textEdit_6.setMinimumSize(QSize(300, 0))
        self.textEdit_6.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_20.addWidget(self.textEdit_6)

        self.textEdit_7 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_7.setObjectName(u"textEdit_7")
        sizePolicy2.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy2)
        self.textEdit_7.setMinimumSize(QSize(300, 0))
        self.textEdit_7.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_20.addWidget(self.textEdit_7)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_18.addWidget(self.scrollArea_3)


        self.horizontalLayout_27.addLayout(self.verticalLayout_18)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_clean_2 = QGroupBox(self.page_android_world)
        self.groupBox_clean_2.setObjectName(u"groupBox_clean_2")
        self.groupBox_clean_2.setMinimumSize(QSize(250, 150))
        self.groupBox_clean_2.setMaximumSize(QSize(250, 300))
        self.groupBox_clean_2.setSizeIncrement(QSize(0, 0))
        self.groupBox_clean_2.setFont(font2)
        self.groupBox_clean_2.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_clean_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_clean_2.setFlat(False)
        self.groupBox_clean_2.setCheckable(False)
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_clean_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_11 = QLabel(self.groupBox_clean_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(50, 20))
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_33.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.groupBox_clean_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy4)
        self.lineEdit_4.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_33.addWidget(self.lineEdit_4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_12 = QLabel(self.groupBox_clean_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(50, 20))
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_34.addWidget(self.label_12)

        self.lineEdit_5 = QLineEdit(self.groupBox_clean_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy4.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy4)
        self.lineEdit_5.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_34.addWidget(self.lineEdit_5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_34)

        self.radioButton_8 = QRadioButton(self.groupBox_clean_2)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font14)
        self.radioButton_8.setStyleSheet(u"QRadioButton {\n"
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
        self.radioButton_8.setAutoExclusive(True)

        self.verticalLayout_21.addWidget(self.radioButton_8)


        self.verticalLayout.addWidget(self.groupBox_clean_2)

        self.groupBox_2 = QGroupBox(self.page_android_world)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)
        self.label_13.setMinimumSize(QSize(50, 50))
        self.label_13.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setPointSize(10)
        self.label_13.setFont(font15)

        self.horizontalLayout_35.addWidget(self.label_13)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_35.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_35.addWidget(self.spinBox_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(50, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_36.addWidget(self.label_14)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy4.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy4)
        self.lineEdit_7.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_36.addWidget(self.lineEdit_7)


        self.verticalLayout_24.addLayout(self.horizontalLayout_36)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.pushButton_4 = QPushButton(self.page_android_world)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy6)
        self.pushButton_4.setFont(font9)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout_27.addLayout(self.verticalLayout)

        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

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
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font16)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        font17 = QFont()
        font17.setFamily(u"Segoe UI Light")
        font17.setPointSize(10)
        self.lab_tab.setFont(font17)
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

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_android.setCurrentIndex(2)


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
        self.bn_bug.setToolTip(QCoreApplication.translate("MainWindow", u"Bug", None))
#endif // QT_CONFIG(tooltip)
        self.bn_bug.setText("")
#if QT_CONFIG(tooltip)
        self.bn_cloud.setToolTip(QCoreApplication.translate("MainWindow", u"Cloud", None))
#endif // QT_CONFIG(tooltip)
        self.bn_cloud.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android.setToolTip(QCoreApplication.translate("MainWindow", u"Android", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android.setText("")
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
        self.lab_bullet.setText("")
        self.lab_bullet3.setText("")
        self.lab_bug2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Simple TO</span></p></body></html>", None))
        self.lab_bug3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Sertilage</span></p></body></html>", None))
        self.comboBox_bug.setItemText(0, QCoreApplication.translate("MainWindow", u"100000", None))
        self.comboBox_bug.setItemText(1, QCoreApplication.translate("MainWindow", u"1000000", None))
        self.comboBox_bug.setItemText(2, QCoreApplication.translate("MainWindow", u"10000000", None))
        self.comboBox_bug.setItemText(3, QCoreApplication.translate("MainWindow", u"100000000", None))

        self.lab_bug1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Vore/Lore</span></p></body></html>", None))
        self.lab_bullet2.setText("")
        self.bn_bug_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lab_bug_action.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Action: </span></p></body></html>", None))
        self.lab_cloud_main.setText(QCoreApplication.translate("MainWindow", u"Login Page", None))
        self.bn_cloud_connect.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.bn_cloud_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.bn_cloud_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
#if QT_CONFIG(tooltip)
        self.bn_android_contact.setToolTip(QCoreApplication.translate("MainWindow", u"Contact", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_contact.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_game.setToolTip(QCoreApplication.translate("MainWindow", u"GamePad", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_game.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_world.setToolTip(QCoreApplication.translate("MainWindow", u"World", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_world.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_clean.setToolTip(QCoreApplication.translate("MainWindow", u"Clean", None))
#endif // QT_CONFIG(tooltip)
        self.bn_android_clean.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u" Crisis Event", None))
        self.lab_person_icon.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Earthquake", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Volcano", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Floods", None))

        self.line_android_name.setText(QCoreApplication.translate("MainWindow", u"California, USA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Since", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.bn_android_contact_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_android_contact_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.bn_android_contact_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Till", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Query:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.groupBox_clean_2.setTitle(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Retweet", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Follwers \n"
" Range", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

