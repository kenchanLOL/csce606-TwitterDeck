# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QDateTimeEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

from widgets import TwitterDeck
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1203, 723)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt "
                        "\"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(25"
                        "5, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/ico"
                        "ns/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 24"
                        "9);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10"
                        "px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-c"
                        "olor: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: non"
                        "e;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScroll"
                        "Bar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background"
                        ": none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked "
                        "{\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding"
                        ": 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, "
                        "76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px sol"
                        "id rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"#login QLabel {\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_login = QPushButton(self.topMenu)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(0, 45))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.LeftToRight)
        self.btn_login.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);")

        self.verticalLayout_8.addWidget(self.btn_login)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_21 = QVBoxLayout(self.login)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)

        self.row_login_1 = QFrame(self.login)
        self.row_login_1.setObjectName(u"row_login_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.row_login_1.sizePolicy().hasHeightForWidth())
        self.row_login_1.setSizePolicy(sizePolicy3)
        self.horizontalLayout_6 = QHBoxLayout(self.row_login_1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.row_login_1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_2.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.text_username = QPlainTextEdit(self.row_login_1)
        self.text_username.setObjectName(u"text_username")
        self.text_username.setMaximumSize(QSize(16777215, 50))
        self.text_username.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.text_username)


        self.verticalLayout_21.addWidget(self.row_login_1)

        self.row_login_2 = QFrame(self.login)
        self.row_login_2.setObjectName(u"row_login_2")
        sizePolicy3.setHeightForWidth(self.row_login_2.sizePolicy().hasHeightForWidth())
        self.row_login_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_7 = QHBoxLayout(self.row_login_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.row_login_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.test_password = QPlainTextEdit(self.row_login_2)
        self.test_password.setObjectName(u"test_password")
        self.test_password.setMaximumSize(QSize(16777215, 50))
        self.test_password.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_7.addWidget(self.test_password)


        self.verticalLayout_21.addWidget(self.row_login_2)

        self.row_login_3 = QFrame(self.login)
        self.row_login_3.setObjectName(u"row_login_3")
        self.row_login_3.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.row_login_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(600, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.btn_login_login = QPushButton(self.row_login_3)
        self.btn_login_login.setObjectName(u"btn_login_login")
        sizePolicy3.setHeightForWidth(self.btn_login_login.sizePolicy().hasHeightForWidth())
        self.btn_login_login.setSizePolicy(sizePolicy3)
        self.btn_login_login.setMinimumSize(QSize(250, 0))
        self.btn_login_login.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	text-align:Center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_login_login)

        self.btn_login_register = QPushButton(self.row_login_3)
        self.btn_login_register.setObjectName(u"btn_login_register")
        sizePolicy3.setHeightForWidth(self.btn_login_register.sizePolicy().hasHeightForWidth())
        self.btn_login_register.setSizePolicy(sizePolicy3)
        self.btn_login_register.setMinimumSize(QSize(250, 0))
        self.btn_login_register.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_login_register)


        self.verticalLayout_21.addWidget(self.row_login_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.login)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 315, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.test = TwitterDeck()
        self.test.setObjectName(u"test")
        self.stackedWidget.addWidget(self.test)
        self.deck = QWidget()
        self.deck.setObjectName(u"deck")
        self.verticalLayout_20 = QVBoxLayout(self.deck)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stackedWidget_2 = QStackedWidget(self.deck)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.event = QWidget()
        self.event.setObjectName(u"event")
        self.frame_event = QFrame(self.event)
        self.frame_event.setObjectName(u"frame_event")
        self.frame_event.setGeometry(QRect(10, 17, 891, 501))
        self.gridLayout_3 = QGridLayout(self.frame_event)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.text_location = QPlainTextEdit(self.frame_event)
        self.text_location.setObjectName(u"text_location")
        self.text_location.setMaximumSize(QSize(16777215, 50))
        self.text_location.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.text_location, 1, 1, 1, 1)

        self.label_crisis_type = QLabel(self.frame_event)
        self.label_crisis_type.setObjectName(u"label_crisis_type")
        self.label_crisis_type.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.label_crisis_type, 5, 0, 1, 1)

        self.tine_till = QDateTimeEdit(self.frame_event)
        self.tine_till.setObjectName(u"tine_till")
        self.tine_till.setMinimumSize(QSize(0, 40))
        self.tine_till.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.tine_till, 4, 1, 1, 1)

        self.label_since = QLabel(self.frame_event)
        self.label_since.setObjectName(u"label_since")
        self.label_since.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.label_since, 3, 0, 1, 1)

        self.text_search = QPlainTextEdit(self.frame_event)
        self.text_search.setObjectName(u"text_search")
        self.text_search.setMaximumSize(QSize(16777215, 50))
        self.text_search.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.text_search, 2, 1, 1, 1)

        self.label_till = QLabel(self.frame_event)
        self.label_till.setObjectName(u"label_till")
        self.label_till.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.label_till, 4, 0, 1, 1)

        self.time_since = QDateTimeEdit(self.frame_event)
        self.time_since.setObjectName(u"time_since")
        self.time_since.setMinimumSize(QSize(0, 40))
        self.time_since.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.time_since, 3, 1, 1, 1)

        self.combo_type = QComboBox(self.frame_event)
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.setObjectName(u"combo_type")
        self.combo_type.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.combo_type, 5, 1, 1, 1)

        self.label_Search = QLabel(self.frame_event)
        self.label_Search.setObjectName(u"label_Search")
        self.label_Search.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.label_Search, 2, 0, 1, 1)

        self.label_title = QLabel(self.frame_event)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 100))
        self.label_title.setFont(font)

        self.gridLayout_3.addWidget(self.label_title, 0, 1, 1, 1)

        self.label_location = QLabel(self.frame_event)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setMinimumSize(QSize(300, 0))

        self.gridLayout_3.addWidget(self.label_location, 1, 0, 1, 1)

        self.btn_search = QPushButton(self.frame_event)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy5)
        self.btn_search.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamilies([u"22px"])
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setItalic(False)
        self.btn_search.setFont(font6)
        self.btn_search.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font:bold, 22px")

        self.gridLayout_3.addWidget(self.btn_search, 6, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.event)
        self.queries = QWidget()
        self.queries.setObjectName(u"queries")
        self.frame_6 = QFrame(self.queries)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 1061, 581))
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.query_1 = QFrame(self.frame_6)
        self.query_1.setObjectName(u"query_1")
        self.query_1.setMinimumSize(QSize(0, 0))
        self._1 = QVBoxLayout(self.query_1)
        self._1.setObjectName(u"_1")
        self.frame_q1 = QFrame(self.query_1)
        self.frame_q1.setObjectName(u"frame_q1")
        sizePolicy5.setHeightForWidth(self.frame_q1.sizePolicy().hasHeightForWidth())
        self.frame_q1.setSizePolicy(sizePolicy5)
        self.frame_q1.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_q1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.frame_q1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"font:bold 22px;")

        self.horizontalLayout_10.addWidget(self.label)

        self.plainTextEdit_4 = QPlainTextEdit(self.frame_q1)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setMinimumSize(QSize(0, 40))
        self.plainTextEdit_4.setMaximumSize(QSize(16777215, 40))
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.plainTextEdit_4)

        self.btn_query_1 = QPushButton(self.frame_q1)
        self.btn_query_1.setObjectName(u"btn_query_1")
        self.btn_query_1.setMinimumSize(QSize(70, 0))
        self.btn_query_1.setMaximumSize(QSize(16777215, 30))
        self.btn_query_1.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.btn_query_1)

        self.btn_filter_1 = QPushButton(self.frame_q1)
        self.btn_filter_1.setObjectName(u"btn_filter_1")
        self.btn_filter_1.setMinimumSize(QSize(50, 0))
        self.btn_filter_1.setMaximumSize(QSize(16777215, 30))
        self.btn_filter_1.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.btn_filter_1)


        self._1.addWidget(self.frame_q1)

        self.scrollArea_2 = QScrollArea(self.query_1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(450, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 316, 556))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 130))
        self.textEdit_2.setMaximumSize(QSize(435, 16777215))
        self.textEdit_2.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_22.addWidget(self.textEdit_2)

        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(0, 130))
        self.textEdit_3.setMaximumSize(QSize(435, 16777215))
        self.textEdit_3.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_22.addWidget(self.textEdit_3)

        self.textEdit_6 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMinimumSize(QSize(0, 130))
        self.textEdit_6.setMaximumSize(QSize(435, 16777215))
        self.textEdit_6.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_22.addWidget(self.textEdit_6)

        self.textEdit_7 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMinimumSize(QSize(0, 130))
        self.textEdit_7.setMaximumSize(QSize(435, 16777215))
        self.textEdit_7.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_22.addWidget(self.textEdit_7)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self._1.addWidget(self.scrollArea_2)


        self.horizontalLayout_14.addWidget(self.query_1)

        self.query_2 = QFrame(self.frame_6)
        self.query_2.setObjectName(u"query_2")
        self._2 = QVBoxLayout(self.query_2)
        self._2.setObjectName(u"_2")
        self.frame_q2 = QFrame(self.query_2)
        self.frame_q2.setObjectName(u"frame_q2")
        sizePolicy5.setHeightForWidth(self.frame_q2.sizePolicy().hasHeightForWidth())
        self.frame_q2.setSizePolicy(sizePolicy5)
        self.frame_q2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.frame_q2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.frame_q2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"font:bold 22px;")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.text_query_2 = QPlainTextEdit(self.frame_q2)
        self.text_query_2.setObjectName(u"text_query_2")
        self.text_query_2.setMinimumSize(QSize(0, 40))
        self.text_query_2.setMaximumSize(QSize(16777215, 16777215))
        self.text_query_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.text_query_2)

        self.btn_query_2 = QPushButton(self.frame_q2)
        self.btn_query_2.setObjectName(u"btn_query_2")
        self.btn_query_2.setMinimumSize(QSize(70, 0))
        self.btn_query_2.setMaximumSize(QSize(16777215, 30))
        self.btn_query_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.btn_query_2)

        self.btn_filter_2 = QPushButton(self.frame_q2)
        self.btn_filter_2.setObjectName(u"btn_filter_2")
        self.btn_filter_2.setMinimumSize(QSize(50, 0))
        self.btn_filter_2.setMaximumSize(QSize(16777215, 30))
        self.btn_filter_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.btn_filter_2)


        self._2.addWidget(self.frame_q2)

        self.scrollArea_4 = QScrollArea(self.query_2)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(450, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 315, 556))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.textEdit_8 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setMinimumSize(QSize(0, 130))
        self.textEdit_8.setMaximumSize(QSize(435, 16777215))
        self.textEdit_8.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_23.addWidget(self.textEdit_8)

        self.textEdit_9 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setMinimumSize(QSize(0, 130))
        self.textEdit_9.setMaximumSize(QSize(435, 16777215))
        self.textEdit_9.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_23.addWidget(self.textEdit_9)

        self.textEdit_10 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setMinimumSize(QSize(0, 130))
        self.textEdit_10.setMaximumSize(QSize(435, 16777215))
        self.textEdit_10.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_23.addWidget(self.textEdit_10)

        self.textEdit_11 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setMinimumSize(QSize(0, 130))
        self.textEdit_11.setMaximumSize(QSize(435, 16777215))
        self.textEdit_11.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_23.addWidget(self.textEdit_11)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self._2.addWidget(self.scrollArea_4)


        self.horizontalLayout_14.addWidget(self.query_2)

        self.query_3 = QFrame(self.frame_6)
        self.query_3.setObjectName(u"query_3")
        self.q_3 = QVBoxLayout(self.query_3)
        self.q_3.setObjectName(u"q_3")
        self.frame_q3 = QFrame(self.query_3)
        self.frame_q3.setObjectName(u"frame_q3")
        sizePolicy5.setHeightForWidth(self.frame_q3.sizePolicy().hasHeightForWidth())
        self.frame_q3.setSizePolicy(sizePolicy5)
        self.frame_q3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_16 = QHBoxLayout(self.frame_q3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.frame_q3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setStyleSheet(u"font:bold 22px;")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.text_query_3 = QPlainTextEdit(self.frame_q3)
        self.text_query_3.setObjectName(u"text_query_3")
        self.text_query_3.setMinimumSize(QSize(0, 40))
        self.text_query_3.setMaximumSize(QSize(16777215, 16777215))
        self.text_query_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_16.addWidget(self.text_query_3)

        self.btn_query_3 = QPushButton(self.frame_q3)
        self.btn_query_3.setObjectName(u"btn_query_3")
        self.btn_query_3.setMinimumSize(QSize(70, 0))
        self.btn_query_3.setMaximumSize(QSize(16777215, 30))
        self.btn_query_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_16.addWidget(self.btn_query_3)

        self.btn_filter_3 = QPushButton(self.frame_q3)
        self.btn_filter_3.setObjectName(u"btn_filter_3")
        self.btn_filter_3.setMinimumSize(QSize(50, 0))
        self.btn_filter_3.setMaximumSize(QSize(16777215, 30))
        self.btn_filter_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_16.addWidget(self.btn_filter_3)


        self.q_3.addWidget(self.frame_q3)

        self.scrollArea_6 = QScrollArea(self.query_3)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMaximumSize(QSize(450, 16777215))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 316, 556))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.textEdit_16 = QTextEdit(self.scrollAreaWidgetContents_6)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setMinimumSize(QSize(0, 130))
        self.textEdit_16.setMaximumSize(QSize(435, 16777215))
        self.textEdit_16.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_29.addWidget(self.textEdit_16)

        self.textEdit_17 = QTextEdit(self.scrollAreaWidgetContents_6)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setMinimumSize(QSize(0, 130))
        self.textEdit_17.setMaximumSize(QSize(435, 16777215))
        self.textEdit_17.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_29.addWidget(self.textEdit_17)

        self.textEdit_18 = QTextEdit(self.scrollAreaWidgetContents_6)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setMinimumSize(QSize(0, 130))
        self.textEdit_18.setMaximumSize(QSize(435, 16777215))
        self.textEdit_18.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_29.addWidget(self.textEdit_18)

        self.textEdit_19 = QTextEdit(self.scrollAreaWidgetContents_6)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setMinimumSize(QSize(0, 130))
        self.textEdit_19.setMaximumSize(QSize(435, 16777215))
        self.textEdit_19.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_29.addWidget(self.textEdit_19)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.q_3.addWidget(self.scrollArea_6)


        self.horizontalLayout_14.addWidget(self.query_3)

        self.stackedWidget_2.addWidget(self.queries)
        self.filter = QWidget()
        self.filter.setObjectName(u"filter")
        self.frame_filter = QFrame(self.filter)
        self.frame_filter.setObjectName(u"frame_filter")
        self.frame_filter.setGeometry(QRect(20, 0, 1081, 591))
        self.horizontalLayout_22 = QHBoxLayout(self.frame_filter)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.query_filter = QFrame(self.frame_filter)
        self.query_filter.setObjectName(u"query_filter")
        self.query_filter.setMinimumSize(QSize(0, 0))
        self._3 = QVBoxLayout(self.query_filter)
        self._3.setObjectName(u"_3")
        self.frame_4 = QFrame(self.query_filter)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"font:bold 22px;")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.plainTextEdit_8 = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_17.addWidget(self.plainTextEdit_8)


        self._3.addWidget(self.frame_4)

        self.scrollArea_3 = QScrollArea(self.query_filter)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(500, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 490, 556))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.textEdit_4 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 130))
        self.textEdit_4.setMaximumSize(QSize(435, 16777215))
        self.textEdit_4.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_24.addWidget(self.textEdit_4)

        self.textEdit_5 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(0, 130))
        self.textEdit_5.setMaximumSize(QSize(435, 16777215))
        self.textEdit_5.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_24.addWidget(self.textEdit_5)

        self.textEdit_20 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setMinimumSize(QSize(0, 130))
        self.textEdit_20.setMaximumSize(QSize(435, 16777215))
        self.textEdit_20.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_24.addWidget(self.textEdit_20)

        self.textEdit_21 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setMinimumSize(QSize(0, 130))
        self.textEdit_21.setMaximumSize(QSize(435, 16777215))
        self.textEdit_21.setStyleSheet(u"background-color:rgb(255,255,255);border-radius: 10px;padding-top: 10px;")

        self.verticalLayout_24.addWidget(self.textEdit_21)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self._3.addWidget(self.scrollArea_3)


        self.horizontalLayout_22.addWidget(self.query_filter)

        self.layout_filter = QVBoxLayout()
        self.layout_filter.setObjectName(u"layout_filter")
        self.group_content = QGroupBox(self.frame_filter)
        self.group_content.setObjectName(u"group_content")
        self.group_content.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_25 = QVBoxLayout(self.group_content)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(self.group_content)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: bold 20px")

        self.horizontalLayout_18.addWidget(self.label_14)

        self.text_filter_include = QPlainTextEdit(self.group_content)
        self.text_filter_include.setObjectName(u"text_filter_include")
        self.text_filter_include.setMaximumSize(QSize(16777215, 40))
        self.text_filter_include.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_18.addWidget(self.text_filter_include)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_15 = QLabel(self.group_content)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: bold 20px")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.text_filter_exclue = QPlainTextEdit(self.group_content)
        self.text_filter_exclue.setObjectName(u"text_filter_exclue")
        self.text_filter_exclue.setMaximumSize(QSize(16777215, 40))
        self.text_filter_exclue.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.text_filter_exclue)


        self.verticalLayout_25.addLayout(self.horizontalLayout_19)

        self.radio_filter_retweet = QRadioButton(self.group_content)
        self.radio_filter_retweet.setObjectName(u"radio_filter_retweet")
        self.radio_filter_retweet.setStyleSheet(u"font: bold 20px")

        self.verticalLayout_25.addWidget(self.radio_filter_retweet)


        self.layout_filter.addWidget(self.group_content)

        self.group_user = QGroupBox(self.frame_filter)
        self.group_user.setObjectName(u"group_user")
        self.group_user.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_28 = QVBoxLayout(self.group_user)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.group_user)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: bold 20px")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.spin_filter_follow_lo = QSpinBox(self.group_user)
        self.spin_filter_follow_lo.setObjectName(u"spin_filter_follow_lo")
        self.spin_filter_follow_lo.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_21.addWidget(self.spin_filter_follow_lo)

        self.spin_filter_follow_hi = QSpinBox(self.group_user)
        self.spin_filter_follow_hi.setObjectName(u"spin_filter_follow_hi")
        self.spin_filter_follow_hi.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_21.addWidget(self.spin_filter_follow_hi)


        self.verticalLayout_28.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_17 = QLabel(self.group_user)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: bold 20px")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.text_filter_tweet_id = QPlainTextEdit(self.group_user)
        self.text_filter_tweet_id.setObjectName(u"text_filter_tweet_id")
        self.text_filter_tweet_id.setMaximumSize(QSize(16777215, 40))
        self.text_filter_tweet_id.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_20.addWidget(self.text_filter_tweet_id)


        self.verticalLayout_28.addLayout(self.horizontalLayout_20)


        self.layout_filter.addWidget(self.group_user)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_filter.addItem(self.verticalSpacer_2)

        self.btn_filter = QPushButton(self.frame_filter)
        self.btn_filter.setObjectName(u"btn_filter")
        self.btn_filter.setMinimumSize(QSize(0, 30))
        self.btn_filter.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.layout_filter.addWidget(self.btn_filter)

        self.btn_apply = QPushButton(self.frame_filter)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setMinimumSize(QSize(0, 30))
        self.btn_apply.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.layout_filter.addWidget(self.btn_apply)


        self.horizontalLayout_22.addLayout(self.layout_filter)

        self.stackedWidget_2.addWidget(self.filter)

        self.verticalLayout_20.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.deck)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_26.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Crisis Deck- A twitter deck specific for crisis event", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_login_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_crisis_type.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Crisis Type:</span></p></body></html>", None))
        self.label_since.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Since:</span></p></body></html>", None))
        self.label_till.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Till:</span></p></body></html>", None))
        self.combo_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Earthquake", None))
        self.combo_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Fire", None))
        self.combo_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Typhoon", None))
        self.combo_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Volcanic Eruption", None))
        self.combo_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Flood", None))

        self.label_Search.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Crisis Event</span></p></body></html>", None))
        self.label_location.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Location:</span></p></body></html>", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.btn_query_1.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.btn_filter_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.btn_query_2.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.btn_filter_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.btn_query_3.setText(QCoreApplication.translate("MainWindow", u"\u21b5", None))
        self.btn_filter_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_19.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Query: ", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_20.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Euphorian54</span><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">RT </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@debbiegibson</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; co"
                        "lor:#1da1f2;\">#TeamDeb</span><span style=\" font-size:9pt; color:#000000;\"> for </span><span style=\" font-size:9pt; color:#1da1f2;\">@bizarro_chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#HITPARADE</span><span style=\" font-size:9pt; color:#000000;\"> &amp; </span><span style=\" font-size:9pt; color:#1da1f2;\">@Blondieclub</span><span style=\" font-size:9pt; color:#000000;\"> ! </span><span style=\" font-size:9pt; color:#1da1f2;\">#chile</span><span style=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">#santiago</span><span style=\" font-size:9pt;\"> </span><a href=\"http://t.co/A\u2026\"><span style=\" font-size:9pt; text-decoration: underline; color:#1da1f2;\">http://t.co/A\u2026</span></a><span style=\" font-size:9pt;\"> </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span sty"
                        "le=\" font-size:9pt;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt;\"> </span></p></body></html>", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><img src=\"twitter-avatar.jpg\" /><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; font-weight:696; color:#000000;\">@Vallie</span><span style=\" font-size:9pt; color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">WATCH LIVE: U.S. Geological Survey briefing on major Chilean earthquake </span><a href=\"http://t.co/6Kj1mkBCT3\"><span style=\" font-size:9pt; text-decoration: u"
                        "nderline; color:#1da1f2;\">http://t.co/6Kj1mkBCT3</span></a><span style=\" font-size:9pt; color:#1da1f2;\"> #ChileEarthquake </span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#1da1f2;\">Like</span><span style=\" font-size:9pt; color:#000000;\"> </span><span style=\" font-size:9pt; color:#1da1f2;\">Retweet</span><span style=\" font-size:9pt; color:#000000;\"> </span></p></body></html>", None))
        self.group_content.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.radio_filter_retweet.setText(QCoreApplication.translate("MainWindow", u"Retweet", None))
        self.group_user.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Follower Range", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.btn_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.btn_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Wanderson M. Pimenta", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

