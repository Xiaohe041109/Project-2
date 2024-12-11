# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 677)
        MainWindow.setStyleSheet(u"#MainWindow, #centralwidget, #main_body {\n"
"	background-color: #00223D;\n"
"}\n"
"\n"
"#header, #hidden, #main, #shown{\n"
"	background-color: #052641;\n"
"}\n"
"\n"
"#header {\n"
"	border-radius: 50px\n"
"}\n"
"\n"
"/*\n"
"#frame_14, #frame_13 {\n"
"	background-color: #052641;\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(5, 38, 65, 255), stop:1 rgba(0, 34, 61, 255));\n"
"	border: 5px solid #00223D;\n"
"	border-radius: 25px;\n"
"}\n"
"*/\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"\n"
"#home, #tracker, #prep {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
"QPushButton:hover {\n"
"    background-color: #202020;\n"
"    color: white;\n"
"	border: 5px solid white;\n"
"	border-radius: 10px;\n"
"}\n"
"*/")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionGitHub = QAction(MainWindow)
        self.actionGitHub.setObjectName(u"actionGitHub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"\n"
"#header {\n"
"	/*border: 2px solid black;*/\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"#pushButton:hover {\n"
"    background-color: #202020;\n"
"    color: white;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/waffleMenu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(35)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #202020;\n"
"    color: white;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(50, 50))
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.main_body)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hidden = QWidget(self.main_body)
        self.hidden.setObjectName(u"hidden")
        self.hidden.setStyleSheet(u"#hidden {\n"
"	/*border: 2px solid black;*/\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #202020;\n"
"    color: white;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.hidden)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.hidden)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/images/homeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/images/tracker.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon4 = QIcon()
        icon4.addFile(u":/images/rulerPencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.hidden)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/images/gitHub.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon6 = QIcon()
        icon6.addFile(u":/images/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.hidden)

        self.shown = QWidget(self.main_body)
        self.shown.setObjectName(u"shown")
        self.shown.setStyleSheet(u"#shown {\n"
"	/*border: 2px solid black;*/\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #202020;\n"
"    color: white;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.shown)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.shown)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton_8.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QSize(25, 25))
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(25, 25))
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.shown)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_11 = QPushButton(self.frame_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QSize(25, 25))
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_7.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setIconSize(QSize(25, 25))
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_7.addWidget(self.pushButton_12)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.shown)

        self.main = QWidget(self.main_body)
        self.main.setObjectName(u"main")
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet(u"#main {\n"
"	/*border: 2px solid black;*/\n"
"    border-radius: 25px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.main)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pages = QStackedWidget(self.main)
        self.pages.setObjectName(u"pages")
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_9 = QVBoxLayout(self.home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_13 = QPushButton(self.frame_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(40)
        font2.setBold(True)
        self.pushButton_13.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/images/clouds.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.pushButton_13)


        self.horizontalLayout_7.addWidget(self.frame_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_9.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_13 = QFrame(self.widget_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(135)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_6)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setLineWidth(1)
        self.label_7.setMidLineWidth(0)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_12.addWidget(self.frame_18)


        self.gridLayout.addWidget(self.frame_13, 0, 0, 2, 1)

        self.frame_15 = QFrame(self.widget_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_15, 1, 2, 1, 1)

        self.frame_14 = QFrame(self.widget_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_8)


        self.verticalLayout_13.addWidget(self.frame_19, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_20 = QFrame(self.frame_14)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_10 = QLabel(self.frame_22)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_10)


        self.verticalLayout_15.addWidget(self.frame_22, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_15.addWidget(self.frame_21)


        self.verticalLayout_13.addWidget(self.frame_20)


        self.gridLayout.addWidget(self.frame_14, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.pages.addWidget(self.home)
        self.tracker = QWidget()
        self.tracker.setObjectName(u"tracker")
        self.verticalLayout_10 = QVBoxLayout(self.tracker)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_4 = QWidget(self.tracker)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.widget_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_14 = QPushButton(self.frame_9)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QSize(50, 50))

        self.horizontalLayout_9.addWidget(self.pushButton_14)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.frame_10 = QFrame(self.widget_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.tracker)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_23 = QFrame(self.widget_3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_16 = QPushButton(self.frame_26)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font1)

        self.horizontalLayout_21.addWidget(self.pushButton_16)


        self.verticalLayout_14.addWidget(self.frame_26, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_11 = QLabel(self.frame_27)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setBold(True)
        self.label_11.setFont(font4)

        self.horizontalLayout_22.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_27)


        self.gridLayout_2.addWidget(self.frame_23, 0, 0, 2, 1)

        self.frame_25 = QFrame(self.widget_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_25, 1, 2, 1, 1)

        self.frame_24 = QFrame(self.widget_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame_24, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.pages.addWidget(self.tracker)
        self.prep = QWidget()
        self.prep.setObjectName(u"prep")
        self.verticalLayout_11 = QVBoxLayout(self.prep)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_5 = QWidget(self.prep)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_11 = QFrame(self.widget_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_15 = QPushButton(self.frame_11)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QSize(50, 50))

        self.horizontalLayout_11.addWidget(self.pushButton_15)


        self.horizontalLayout_13.addWidget(self.frame_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.frame_12 = QFrame(self.widget_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.frame_12)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)


        self.horizontalLayout_13.addWidget(self.frame_12)


        self.verticalLayout_11.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_6 = QWidget(self.prep)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_28 = QFrame(self.widget_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_28)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(50)
        font5.setBold(True)
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_12)


        self.verticalLayout_16.addWidget(self.frame_28)


        self.verticalLayout_11.addWidget(self.widget_6)

        self.pages.addWidget(self.prep)

        self.verticalLayout_8.addWidget(self.pages)


        self.horizontalLayout_4.addWidget(self.main)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuGitHub = QMenu(self.menubar)
        self.menuGitHub.setObjectName(u"menuGitHub")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuGitHub.menuAction())
        self.menuAbout.addAction(self.actionAbout)
        self.menuGitHub.addAction(self.actionGitHub)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.shown.setHidden)
        self.pushButton.toggled.connect(self.hidden.setVisible)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionGitHub.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"HURRICANE GAURD", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Hurricane Tracker", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Prep", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"FORECAST", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Current Weather", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tommorow's Weather", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"TRACKER", None))
        self.label_3.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Active Hurricane Information Will Be Displayed Below.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Prep", None))
        self.label_4.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"COMING SOON!", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuGitHub.setTitle(QCoreApplication.translate("MainWindow", u"GitHub", None))
    # retranslateUi

