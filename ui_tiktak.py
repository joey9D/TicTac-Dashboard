# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TikTak.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from animatedtoggle import AnimatedToggle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 419)
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.actionVersion_2 = QAction(MainWindow)
        self.actionVersion_2.setObjectName(u"actionVersion_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 20, 681, 351))
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.gridLayoutWidget = QWidget(self.tab_general)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(170, 10, 501, 311))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_Button6 = QLabel(self.gridLayoutWidget)
        self.lbl_Button6.setObjectName(u"lbl_Button6")
        self.lbl_Button6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button6, 2, 1, 1, 1)

        self.vL_Led6 = QVBoxLayout()
        self.vL_Led6.setObjectName(u"vL_Led6")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lbl_OutputLed6 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed6.setObjectName(u"lbl_OutputLed6")
        self.lbl_OutputLed6.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed6.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed6.setAutoFillBackground(False)
        self.lbl_OutputLed6.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_29.addWidget(self.lbl_OutputLed6)

        self.lbl_OutputCnt6 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt6.setObjectName(u"lbl_OutputCnt6")
        self.lbl_OutputCnt6.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.lbl_OutputCnt6)


        self.vL_Led6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbl_InputLed6 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed6.setObjectName(u"lbl_InputLed6")
        self.lbl_InputLed6.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed6.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed6.setAutoFillBackground(False)
        self.lbl_InputLed6.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_30.addWidget(self.lbl_InputLed6)

        self.lbl_InputCnt6 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt6.setObjectName(u"lbl_InputCnt6")
        self.lbl_InputCnt6.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_30.addWidget(self.lbl_InputCnt6)


        self.vL_Led6.addLayout(self.horizontalLayout_30)

        self.pB_ButtonSettings6 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings6.setObjectName(u"pB_ButtonSettings6")

        self.vL_Led6.addWidget(self.pB_ButtonSettings6)


        self.gridLayout.addLayout(self.vL_Led6, 3, 1, 1, 1)

        self.lbl_Button5 = QLabel(self.gridLayoutWidget)
        self.lbl_Button5.setObjectName(u"lbl_Button5")
        self.lbl_Button5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button5, 2, 0, 1, 1)

        self.lbl_Button8 = QLabel(self.gridLayoutWidget)
        self.lbl_Button8.setObjectName(u"lbl_Button8")
        self.lbl_Button8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button8, 2, 3, 1, 1)

        self.vL_Led5 = QVBoxLayout()
        self.vL_Led5.setObjectName(u"vL_Led5")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lbl_OutputLed5 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed5.setObjectName(u"lbl_OutputLed5")
        self.lbl_OutputLed5.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed5.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed5.setAutoFillBackground(False)
        self.lbl_OutputLed5.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_25.addWidget(self.lbl_OutputLed5)

        self.lbl_OutputCnt5 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt5.setObjectName(u"lbl_OutputCnt5")
        self.lbl_OutputCnt5.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lbl_OutputCnt5)


        self.vL_Led5.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_InputLed5 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed5.setObjectName(u"lbl_InputLed5")
        self.lbl_InputLed5.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed5.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed5.setAutoFillBackground(False)
        self.lbl_InputLed5.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_26.addWidget(self.lbl_InputLed5)

        self.lbl_InputCnt5 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt5.setObjectName(u"lbl_InputCnt5")
        self.lbl_InputCnt5.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.lbl_InputCnt5)


        self.vL_Led5.addLayout(self.horizontalLayout_26)

        self.pB_ButtonSettings5 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings5.setObjectName(u"pB_ButtonSettings5")

        self.vL_Led5.addWidget(self.pB_ButtonSettings5)


        self.gridLayout.addLayout(self.vL_Led5, 3, 0, 1, 1)

        self.lbl_Button7 = QLabel(self.gridLayoutWidget)
        self.lbl_Button7.setObjectName(u"lbl_Button7")
        self.lbl_Button7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_Button7.setWordWrap(False)

        self.gridLayout.addWidget(self.lbl_Button7, 2, 2, 1, 1)

        self.vL_Led4 = QVBoxLayout()
        self.vL_Led4.setObjectName(u"vL_Led4")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_OutputLed4 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed4.setObjectName(u"lbl_OutputLed4")
        self.lbl_OutputLed4.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed4.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed4.setAutoFillBackground(False)
        self.lbl_OutputLed4.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_15.addWidget(self.lbl_OutputLed4)

        self.lbl_OutputCnt4 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt4.setObjectName(u"lbl_OutputCnt4")
        self.lbl_OutputCnt4.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lbl_OutputCnt4)


        self.vL_Led4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_InputLed4 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed4.setObjectName(u"lbl_InputLed4")
        self.lbl_InputLed4.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed4.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed4.setAutoFillBackground(False)
        self.lbl_InputLed4.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_16.addWidget(self.lbl_InputLed4)

        self.lbl_InputCnt4 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt4.setObjectName(u"lbl_InputCnt4")
        self.lbl_InputCnt4.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lbl_InputCnt4)


        self.vL_Led4.addLayout(self.horizontalLayout_16)

        self.pB_ButtonSettings4 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings4.setObjectName(u"pB_ButtonSettings4")

        self.vL_Led4.addWidget(self.pB_ButtonSettings4)


        self.gridLayout.addLayout(self.vL_Led4, 1, 3, 1, 1)

        self.lbl_Button4 = QLabel(self.gridLayoutWidget)
        self.lbl_Button4.setObjectName(u"lbl_Button4")
        self.lbl_Button4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button4, 0, 3, 1, 1)

        self.vL_Led7 = QVBoxLayout()
        self.vL_Led7.setObjectName(u"vL_Led7")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lbl_OutputLed7 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed7.setObjectName(u"lbl_OutputLed7")
        self.lbl_OutputLed7.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed7.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed7.setAutoFillBackground(False)
        self.lbl_OutputLed7.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_31.addWidget(self.lbl_OutputLed7)

        self.lbl_OutputCnt7 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt7.setObjectName(u"lbl_OutputCnt7")
        self.lbl_OutputCnt7.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lbl_OutputCnt7)


        self.vL_Led7.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lbl_InputLed7 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed7.setObjectName(u"lbl_InputLed7")
        self.lbl_InputLed7.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed7.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed7.setAutoFillBackground(False)
        self.lbl_InputLed7.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_32.addWidget(self.lbl_InputLed7)

        self.lbl_InputCnt7 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt7.setObjectName(u"lbl_InputCnt7")
        self.lbl_InputCnt7.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lbl_InputCnt7)


        self.vL_Led7.addLayout(self.horizontalLayout_32)

        self.pB_ButtonSettings7 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings7.setObjectName(u"pB_ButtonSettings7")

        self.vL_Led7.addWidget(self.pB_ButtonSettings7)


        self.gridLayout.addLayout(self.vL_Led7, 3, 2, 1, 1)

        self.lbl_Button1 = QLabel(self.gridLayoutWidget)
        self.lbl_Button1.setObjectName(u"lbl_Button1")
        self.lbl_Button1.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_Button1.setFrameShadow(QFrame.Shadow.Plain)
        self.lbl_Button1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button1, 0, 0, 1, 1)

        self.lbl_Button3 = QLabel(self.gridLayoutWidget)
        self.lbl_Button3.setObjectName(u"lbl_Button3")
        self.lbl_Button3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button3, 0, 2, 1, 1)

        self.vL_Led2 = QVBoxLayout()
        self.vL_Led2.setObjectName(u"vL_Led2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_OutputLed2 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed2.setObjectName(u"lbl_OutputLed2")
        self.lbl_OutputLed2.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed2.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed2.setAutoFillBackground(False)
        self.lbl_OutputLed2.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_11.addWidget(self.lbl_OutputLed2)

        self.lbl_OutputCnt2 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt2.setObjectName(u"lbl_OutputCnt2")
        self.lbl_OutputCnt2.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lbl_OutputCnt2)


        self.vL_Led2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_InputLed2 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed2.setObjectName(u"lbl_InputLed2")
        self.lbl_InputLed2.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed2.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed2.setAutoFillBackground(False)
        self.lbl_InputLed2.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_12.addWidget(self.lbl_InputLed2)

        self.lbl_InputCnt2 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt2.setObjectName(u"lbl_InputCnt2")
        self.lbl_InputCnt2.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lbl_InputCnt2)


        self.vL_Led2.addLayout(self.horizontalLayout_12)

        self.pB_ButtonSettings2 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings2.setObjectName(u"pB_ButtonSettings2")

        self.vL_Led2.addWidget(self.pB_ButtonSettings2)


        self.gridLayout.addLayout(self.vL_Led2, 1, 1, 1, 1)

        self.vL_Led1 = QVBoxLayout()
        self.vL_Led1.setObjectName(u"vL_Led1")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_OutputLed1 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed1.setObjectName(u"lbl_OutputLed1")
        self.lbl_OutputLed1.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed1.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed1.setAutoFillBackground(False)
        self.lbl_OutputLed1.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_9.addWidget(self.lbl_OutputLed1)

        self.lbl_OutputCnt1 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt1.setObjectName(u"lbl_OutputCnt1")
        self.lbl_OutputCnt1.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lbl_OutputCnt1)


        self.vL_Led1.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_InputLed1 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed1.setObjectName(u"lbl_InputLed1")
        self.lbl_InputLed1.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed1.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed1.setAutoFillBackground(False)
        self.lbl_InputLed1.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_10.addWidget(self.lbl_InputLed1)

        self.lbl_InputCnt1 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt1.setObjectName(u"lbl_InputCnt1")
        self.lbl_InputCnt1.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lbl_InputCnt1)


        self.vL_Led1.addLayout(self.horizontalLayout_10)

        self.pB_ButtonSettings1 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings1.setObjectName(u"pB_ButtonSettings1")

        self.vL_Led1.addWidget(self.pB_ButtonSettings1)


        self.gridLayout.addLayout(self.vL_Led1, 1, 0, 1, 1)

        self.lbl_Button2 = QLabel(self.gridLayoutWidget)
        self.lbl_Button2.setObjectName(u"lbl_Button2")
        self.lbl_Button2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_Button2, 0, 1, 1, 1)

        self.vL_Led3 = QVBoxLayout()
        self.vL_Led3.setObjectName(u"vL_Led3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_OutputLed3 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed3.setObjectName(u"lbl_OutputLed3")
        self.lbl_OutputLed3.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed3.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed3.setAutoFillBackground(False)
        self.lbl_OutputLed3.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_13.addWidget(self.lbl_OutputLed3)

        self.lbl_OutputCnt3 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt3.setObjectName(u"lbl_OutputCnt3")
        self.lbl_OutputCnt3.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lbl_OutputCnt3)


        self.vL_Led3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_InputLed3 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed3.setObjectName(u"lbl_InputLed3")
        self.lbl_InputLed3.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed3.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed3.setAutoFillBackground(False)
        self.lbl_InputLed3.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_14.addWidget(self.lbl_InputLed3)

        self.lbl_InputCnt3 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt3.setObjectName(u"lbl_InputCnt3")
        self.lbl_InputCnt3.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lbl_InputCnt3)


        self.vL_Led3.addLayout(self.horizontalLayout_14)

        self.pB_ButtonSettings3 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings3.setObjectName(u"pB_ButtonSettings3")

        self.vL_Led3.addWidget(self.pB_ButtonSettings3)


        self.gridLayout.addLayout(self.vL_Led3, 1, 2, 1, 1)

        self.vL_Led8 = QVBoxLayout()
        self.vL_Led8.setObjectName(u"vL_Led8")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lbl_OutputLed8 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputLed8.setObjectName(u"lbl_OutputLed8")
        self.lbl_OutputLed8.setMinimumSize(QSize(31, 31))
        self.lbl_OutputLed8.setMaximumSize(QSize(31, 31))
        self.lbl_OutputLed8.setAutoFillBackground(False)
        self.lbl_OutputLed8.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_27.addWidget(self.lbl_OutputLed8)

        self.lbl_OutputCnt8 = QLabel(self.gridLayoutWidget)
        self.lbl_OutputCnt8.setObjectName(u"lbl_OutputCnt8")
        self.lbl_OutputCnt8.setFrameShape(QFrame.Shape.Box)
        self.lbl_OutputCnt8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.lbl_OutputCnt8)


        self.vL_Led8.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lbl_InputLed8 = QLabel(self.gridLayoutWidget)
        self.lbl_InputLed8.setObjectName(u"lbl_InputLed8")
        self.lbl_InputLed8.setMinimumSize(QSize(31, 31))
        self.lbl_InputLed8.setMaximumSize(QSize(31, 31))
        self.lbl_InputLed8.setAutoFillBackground(False)
        self.lbl_InputLed8.setStyleSheet(u"background-color: green;")

        self.horizontalLayout_28.addWidget(self.lbl_InputLed8)

        self.lbl_InputCnt8 = QLabel(self.gridLayoutWidget)
        self.lbl_InputCnt8.setObjectName(u"lbl_InputCnt8")
        self.lbl_InputCnt8.setFrameShape(QFrame.Shape.Box)
        self.lbl_InputCnt8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lbl_InputCnt8)


        self.vL_Led8.addLayout(self.horizontalLayout_28)

        self.pB_ButtonSettings8 = QPushButton(self.gridLayoutWidget)
        self.pB_ButtonSettings8.setObjectName(u"pB_ButtonSettings8")

        self.vL_Led8.addWidget(self.pB_ButtonSettings8)


        self.gridLayout.addLayout(self.vL_Led8, 3, 3, 1, 1)

        self.verticalLayoutWidget = QWidget(self.tab_general)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 91, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pB_StartAll = QPushButton(self.verticalLayoutWidget)
        self.pB_StartAll.setObjectName(u"pB_StartAll")

        self.verticalLayout.addWidget(self.pB_StartAll)

        self.pB_StopAll = QPushButton(self.verticalLayoutWidget)
        self.pB_StopAll.setObjectName(u"pB_StopAll")

        self.verticalLayout.addWidget(self.pB_StopAll)

        self.pB_ClearAll = QPushButton(self.verticalLayoutWidget)
        self.pB_ClearAll.setObjectName(u"pB_ClearAll")

        self.verticalLayout.addWidget(self.pB_ClearAll)

        self.layoutWidget = QWidget(self.tab_general)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 40, 51, 121))
        self.vL_Led1_5 = QVBoxLayout(self.layoutWidget)
        self.vL_Led1_5.setObjectName(u"vL_Led1_5")
        self.vL_Led1_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_Output_Active = QLabel(self.layoutWidget)
        self.lbl_Output_Active.setObjectName(u"lbl_Output_Active")
        self.lbl_Output_Active.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vL_Led1_5.addWidget(self.lbl_Output_Active)

        self.lbl_Input_active = QLabel(self.layoutWidget)
        self.lbl_Input_active.setObjectName(u"lbl_Input_active")
        self.lbl_Input_active.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vL_Led1_5.addWidget(self.lbl_Input_active)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.vL_Led1_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_B1 = QWidget()
        self.tab_B1.setObjectName(u"tab_B1")
        self.horizontalLayoutWidget = QWidget(self.tab_B1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.hL_Logic1.setObjectName(u"hL_Logic1")
        self.hL_Logic1.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic1 = QFormLayout()
        self.fL_Logic1.setObjectName(u"fL_Logic1")
        self.pB_Start1 = QPushButton(self.horizontalLayoutWidget)
        self.pB_Start1.setObjectName(u"pB_Start1")

        self.fL_Logic1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start1)

        self.pB_Stop1 = QPushButton(self.horizontalLayoutWidget)
        self.pB_Stop1.setObjectName(u"pB_Stop1")

        self.fL_Logic1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop1)

        self.pB_Clear1 = QPushButton(self.horizontalLayoutWidget)
        self.pB_Clear1.setObjectName(u"pB_Clear1")

        self.fL_Logic1.setWidget(5, QFormLayout.ItemRole.LabelRole, self.pB_Clear1)

        self.l_RunState1 = QLabel(self.horizontalLayoutWidget)
        self.l_RunState1.setObjectName(u"l_RunState1")
        self.l_RunState1.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic1.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState1)

        self.vS_LogicButtons1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic1.setItem(4, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons1)


        self.hL_Logic1.addLayout(self.fL_Logic1)

        self.vL_Parameter1 = QVBoxLayout()
        self.vL_Parameter1.setObjectName(u"vL_Parameter1")
        self.fL_OnOffTime1 = QFormLayout()
        self.fL_OnOffTime1.setObjectName(u"fL_OnOffTime1")
        self.fL_OnOffTime1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime1 = QLabel(self.horizontalLayoutWidget)
        self.l_OnTime1.setObjectName(u"l_OnTime1")

        self.fL_OnOffTime1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime1)

        self.sB_OnTime1 = QSpinBox(self.horizontalLayoutWidget)
        self.sB_OnTime1.setObjectName(u"sB_OnTime1")
        self.sB_OnTime1.setMaximum(1000)
        self.sB_OnTime1.setValue(500)

        self.fL_OnOffTime1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime1)

        self.sB_OffTime1 = QSpinBox(self.horizontalLayoutWidget)
        self.sB_OffTime1.setObjectName(u"sB_OffTime1")
        self.sB_OffTime1.setMaximum(1000)
        self.sB_OffTime1.setValue(500)

        self.fL_OnOffTime1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime1)

        self.l_OffTime1 = QLabel(self.horizontalLayoutWidget)
        self.l_OffTime1.setObjectName(u"l_OffTime1")

        self.fL_OnOffTime1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime1)


        self.vL_Parameter1.addLayout(self.fL_OnOffTime1)

        self.vS_Parameter1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter1.addItem(self.vS_Parameter1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_DiffAbort1 = QLabel(self.horizontalLayoutWidget)
        self.l_DiffAbort1.setObjectName(u"l_DiffAbort1")

        self.horizontalLayout.addWidget(self.l_DiffAbort1)

        self.sB_DiffAbort1 = QSpinBox(self.horizontalLayoutWidget)
        self.sB_DiffAbort1.setObjectName(u"sB_DiffAbort1")

        self.horizontalLayout.addWidget(self.sB_DiffAbort1)


        self.vL_Parameter1.addLayout(self.horizontalLayout)

        self.fL_Cnt1 = QFormLayout()
        self.fL_Cnt1.setObjectName(u"fL_Cnt1")
        self.fL_Cnt1.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut1 = QLabel(self.horizontalLayoutWidget)
        self.l_CntOut1.setObjectName(u"l_CntOut1")

        self.fL_Cnt1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut1)

        self.l_CntIn1 = QLabel(self.horizontalLayoutWidget)
        self.l_CntIn1.setObjectName(u"l_CntIn1")

        self.fL_Cnt1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn1)

        self.l_CntOutVal1 = QLabel(self.horizontalLayoutWidget)
        self.l_CntOutVal1.setObjectName(u"l_CntOutVal1")

        self.fL_Cnt1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal1)

        self.l_CntInVal1 = QLabel(self.horizontalLayoutWidget)
        self.l_CntInVal1.setObjectName(u"l_CntInVal1")

        self.fL_Cnt1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal1)


        self.vL_Parameter1.addLayout(self.fL_Cnt1)


        self.hL_Logic1.addLayout(self.vL_Parameter1)

        self.tabWidget.addTab(self.tab_B1, "")
        self.tab_B2 = QWidget()
        self.tab_B2.setObjectName(u"tab_B2")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_B2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hL_Logic2.setObjectName(u"hL_Logic2")
        self.hL_Logic2.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic2 = QFormLayout()
        self.fL_Logic2.setObjectName(u"fL_Logic2")
        self.pB_Start2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pB_Start2.setObjectName(u"pB_Start2")

        self.fL_Logic2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start2)

        self.pB_Stop2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pB_Stop2.setObjectName(u"pB_Stop2")

        self.fL_Logic2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop2)

        self.vS_LogicButtons2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic2.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons2)

        self.pB_Clear2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pB_Clear2.setObjectName(u"pB_Clear2")

        self.fL_Logic2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear2)

        self.l_RunState2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_RunState2.setObjectName(u"l_RunState2")
        self.l_RunState2.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l_RunState2)


        self.hL_Logic2.addLayout(self.fL_Logic2)

        self.vL_Parameter2 = QVBoxLayout()
        self.vL_Parameter2.setObjectName(u"vL_Parameter2")
        self.fL_OnOffTime2 = QFormLayout()
        self.fL_OnOffTime2.setObjectName(u"fL_OnOffTime2")
        self.fL_OnOffTime2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_OnTime2.setObjectName(u"l_OnTime2")

        self.fL_OnOffTime2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime2)

        self.sB_OnTime2 = QSpinBox(self.horizontalLayoutWidget_2)
        self.sB_OnTime2.setObjectName(u"sB_OnTime2")
        self.sB_OnTime2.setMaximum(1000)
        self.sB_OnTime2.setValue(500)

        self.fL_OnOffTime2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime2)

        self.sB_OffTime2 = QSpinBox(self.horizontalLayoutWidget_2)
        self.sB_OffTime2.setObjectName(u"sB_OffTime2")
        self.sB_OffTime2.setMaximum(1000)
        self.sB_OffTime2.setValue(500)

        self.fL_OnOffTime2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime2)

        self.l_OffTime2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_OffTime2.setObjectName(u"l_OffTime2")

        self.fL_OnOffTime2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime2)


        self.vL_Parameter2.addLayout(self.fL_OnOffTime2)

        self.vS_Parameter2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter2.addItem(self.vS_Parameter2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_DiffAbort2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_DiffAbort2.setObjectName(u"l_DiffAbort2")

        self.horizontalLayout_2.addWidget(self.l_DiffAbort2)

        self.sB_DiffAbort2 = QSpinBox(self.horizontalLayoutWidget_2)
        self.sB_DiffAbort2.setObjectName(u"sB_DiffAbort2")

        self.horizontalLayout_2.addWidget(self.sB_DiffAbort2)


        self.vL_Parameter2.addLayout(self.horizontalLayout_2)

        self.fL_Cnt2 = QFormLayout()
        self.fL_Cnt2.setObjectName(u"fL_Cnt2")
        self.fL_Cnt2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_CntOut2.setObjectName(u"l_CntOut2")

        self.fL_Cnt2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut2)

        self.l_CntIn2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_CntIn2.setObjectName(u"l_CntIn2")

        self.fL_Cnt2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn2)

        self.l_CntOutVal2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_CntOutVal2.setObjectName(u"l_CntOutVal2")

        self.fL_Cnt2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal2)

        self.l_CntInVal2 = QLabel(self.horizontalLayoutWidget_2)
        self.l_CntInVal2.setObjectName(u"l_CntInVal2")

        self.fL_Cnt2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal2)


        self.vL_Parameter2.addLayout(self.fL_Cnt2)


        self.hL_Logic2.addLayout(self.vL_Parameter2)

        self.tabWidget.addTab(self.tab_B2, "")
        self.tab_B3 = QWidget()
        self.tab_B3.setObjectName(u"tab_B3")
        self.horizontalLayoutWidget_3 = QWidget(self.tab_B3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.hL_Logic3.setObjectName(u"hL_Logic3")
        self.hL_Logic3.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic3 = QFormLayout()
        self.fL_Logic3.setObjectName(u"fL_Logic3")
        self.pB_Start3 = QPushButton(self.horizontalLayoutWidget_3)
        self.pB_Start3.setObjectName(u"pB_Start3")

        self.fL_Logic3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start3)

        self.pB_Stop3 = QPushButton(self.horizontalLayoutWidget_3)
        self.pB_Stop3.setObjectName(u"pB_Stop3")

        self.fL_Logic3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop3)

        self.vS_LogicButtons3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic3.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons3)

        self.pB_Clear3 = QPushButton(self.horizontalLayoutWidget_3)
        self.pB_Clear3.setObjectName(u"pB_Clear3")

        self.fL_Logic3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear3)

        self.toggle_Button_settings3 = AnimatedToggle(self.horizontalLayoutWidget_3)
        self.toggle_Button_settings3.setObjectName(u"toggle_Button_settings3")

        self.fL_Logic3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings3)

        self.l_RunState3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_RunState3.setObjectName(u"l_RunState3")
        self.l_RunState3.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState3)


        self.hL_Logic3.addLayout(self.fL_Logic3)

        self.vL_Parameter3 = QVBoxLayout()
        self.vL_Parameter3.setObjectName(u"vL_Parameter3")
        self.fL_OnOffTime3 = QFormLayout()
        self.fL_OnOffTime3.setObjectName(u"fL_OnOffTime3")
        self.fL_OnOffTime3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_OnTime3.setObjectName(u"l_OnTime3")

        self.fL_OnOffTime3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime3)

        self.sB_OnTime3 = QSpinBox(self.horizontalLayoutWidget_3)
        self.sB_OnTime3.setObjectName(u"sB_OnTime3")
        self.sB_OnTime3.setMaximum(1000)
        self.sB_OnTime3.setValue(500)

        self.fL_OnOffTime3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime3)

        self.sB_OffTime3 = QSpinBox(self.horizontalLayoutWidget_3)
        self.sB_OffTime3.setObjectName(u"sB_OffTime3")
        self.sB_OffTime3.setMaximum(1000)
        self.sB_OffTime3.setValue(500)

        self.fL_OnOffTime3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime3)

        self.l_OffTime3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_OffTime3.setObjectName(u"l_OffTime3")

        self.fL_OnOffTime3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime3)


        self.vL_Parameter3.addLayout(self.fL_OnOffTime3)

        self.vS_Parameter3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter3.addItem(self.vS_Parameter3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_DiffAbort3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_DiffAbort3.setObjectName(u"l_DiffAbort3")

        self.horizontalLayout_3.addWidget(self.l_DiffAbort3)

        self.sB_DiffAbort3 = QSpinBox(self.horizontalLayoutWidget_3)
        self.sB_DiffAbort3.setObjectName(u"sB_DiffAbort3")

        self.horizontalLayout_3.addWidget(self.sB_DiffAbort3)


        self.vL_Parameter3.addLayout(self.horizontalLayout_3)

        self.fL_Cnt3 = QFormLayout()
        self.fL_Cnt3.setObjectName(u"fL_Cnt3")
        self.fL_Cnt3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_CntOut3.setObjectName(u"l_CntOut3")

        self.fL_Cnt3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut3)

        self.l_CntIn3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_CntIn3.setObjectName(u"l_CntIn3")

        self.fL_Cnt3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn3)

        self.l_CntOutVal3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_CntOutVal3.setObjectName(u"l_CntOutVal3")

        self.fL_Cnt3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal3)

        self.l_CntInVal3 = QLabel(self.horizontalLayoutWidget_3)
        self.l_CntInVal3.setObjectName(u"l_CntInVal3")

        self.fL_Cnt3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal3)


        self.vL_Parameter3.addLayout(self.fL_Cnt3)


        self.hL_Logic3.addLayout(self.vL_Parameter3)

        self.tabWidget.addTab(self.tab_B3, "")
        self.tab_B4 = QWidget()
        self.tab_B4.setObjectName(u"tab_B4")
        self.horizontalLayoutWidget_4 = QWidget(self.tab_B4)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.hL_Logic4.setObjectName(u"hL_Logic4")
        self.hL_Logic4.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic4 = QFormLayout()
        self.fL_Logic4.setObjectName(u"fL_Logic4")
        self.pB_Start4 = QPushButton(self.horizontalLayoutWidget_4)
        self.pB_Start4.setObjectName(u"pB_Start4")

        self.fL_Logic4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start4)

        self.pB_Stop4 = QPushButton(self.horizontalLayoutWidget_4)
        self.pB_Stop4.setObjectName(u"pB_Stop4")

        self.fL_Logic4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop4)

        self.vS_LogicButtons4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic4.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons4)

        self.pB_Clear4 = QPushButton(self.horizontalLayoutWidget_4)
        self.pB_Clear4.setObjectName(u"pB_Clear4")

        self.fL_Logic4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear4)

        self.toggle_Button_settings4 = AnimatedToggle(self.horizontalLayoutWidget_4)
        self.toggle_Button_settings4.setObjectName(u"toggle_Button_settings4")

        self.fL_Logic4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings4)

        self.l_RunState4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_RunState4.setObjectName(u"l_RunState4")
        self.l_RunState4.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState4)


        self.hL_Logic4.addLayout(self.fL_Logic4)

        self.vL_Parameter4 = QVBoxLayout()
        self.vL_Parameter4.setObjectName(u"vL_Parameter4")
        self.fL_OnOffTime4 = QFormLayout()
        self.fL_OnOffTime4.setObjectName(u"fL_OnOffTime4")
        self.fL_OnOffTime4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_OnTime4.setObjectName(u"l_OnTime4")

        self.fL_OnOffTime4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime4)

        self.sB_OnTime4 = QSpinBox(self.horizontalLayoutWidget_4)
        self.sB_OnTime4.setObjectName(u"sB_OnTime4")
        self.sB_OnTime4.setMaximum(1000)
        self.sB_OnTime4.setValue(500)

        self.fL_OnOffTime4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime4)

        self.sB_OffTime4 = QSpinBox(self.horizontalLayoutWidget_4)
        self.sB_OffTime4.setObjectName(u"sB_OffTime4")
        self.sB_OffTime4.setMaximum(1000)
        self.sB_OffTime4.setValue(500)

        self.fL_OnOffTime4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime4)

        self.l_OffTime4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_OffTime4.setObjectName(u"l_OffTime4")

        self.fL_OnOffTime4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime4)


        self.vL_Parameter4.addLayout(self.fL_OnOffTime4)

        self.vS_Parameter4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter4.addItem(self.vS_Parameter4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.l_DiffAbort4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_DiffAbort4.setObjectName(u"l_DiffAbort4")

        self.horizontalLayout_4.addWidget(self.l_DiffAbort4)

        self.sB_DiffAbort4 = QSpinBox(self.horizontalLayoutWidget_4)
        self.sB_DiffAbort4.setObjectName(u"sB_DiffAbort4")

        self.horizontalLayout_4.addWidget(self.sB_DiffAbort4)


        self.vL_Parameter4.addLayout(self.horizontalLayout_4)

        self.fL_Cnt4 = QFormLayout()
        self.fL_Cnt4.setObjectName(u"fL_Cnt4")
        self.fL_Cnt4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_CntOut4.setObjectName(u"l_CntOut4")

        self.fL_Cnt4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut4)

        self.l_CntIn4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_CntIn4.setObjectName(u"l_CntIn4")

        self.fL_Cnt4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn4)

        self.l_CntOutVal4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_CntOutVal4.setObjectName(u"l_CntOutVal4")

        self.fL_Cnt4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal4)

        self.l_CntInVal4 = QLabel(self.horizontalLayoutWidget_4)
        self.l_CntInVal4.setObjectName(u"l_CntInVal4")

        self.fL_Cnt4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal4)


        self.vL_Parameter4.addLayout(self.fL_Cnt4)


        self.hL_Logic4.addLayout(self.vL_Parameter4)

        self.tabWidget.addTab(self.tab_B4, "")
        self.tab_B5 = QWidget()
        self.tab_B5.setObjectName(u"tab_B5")
        self.horizontalLayoutWidget_5 = QWidget(self.tab_B5)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.hL_Logic5.setObjectName(u"hL_Logic5")
        self.hL_Logic5.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic5 = QFormLayout()
        self.fL_Logic5.setObjectName(u"fL_Logic5")
        self.pB_Start5 = QPushButton(self.horizontalLayoutWidget_5)
        self.pB_Start5.setObjectName(u"pB_Start5")

        self.fL_Logic5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start5)

        self.pB_Stop5 = QPushButton(self.horizontalLayoutWidget_5)
        self.pB_Stop5.setObjectName(u"pB_Stop5")

        self.fL_Logic5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop5)

        self.vS_LogicButtons5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic5.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons5)

        self.pB_Clear5 = QPushButton(self.horizontalLayoutWidget_5)
        self.pB_Clear5.setObjectName(u"pB_Clear5")

        self.fL_Logic5.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear5)

        self.toggle_Button_settings5 = AnimatedToggle(self.horizontalLayoutWidget_5)
        self.toggle_Button_settings5.setObjectName(u"toggle_Button_settings5")

        self.fL_Logic5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings5)

        self.l_RunState5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_RunState5.setObjectName(u"l_RunState5")
        self.l_RunState5.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState5)


        self.hL_Logic5.addLayout(self.fL_Logic5)

        self.vL_Parameter5 = QVBoxLayout()
        self.vL_Parameter5.setObjectName(u"vL_Parameter5")
        self.fL_OnOffTime5 = QFormLayout()
        self.fL_OnOffTime5.setObjectName(u"fL_OnOffTime5")
        self.fL_OnOffTime5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_OnTime5.setObjectName(u"l_OnTime5")

        self.fL_OnOffTime5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime5)

        self.sB_OnTime5 = QSpinBox(self.horizontalLayoutWidget_5)
        self.sB_OnTime5.setObjectName(u"sB_OnTime5")
        self.sB_OnTime5.setMaximum(1000)
        self.sB_OnTime5.setValue(500)

        self.fL_OnOffTime5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime5)

        self.sB_OffTime5 = QSpinBox(self.horizontalLayoutWidget_5)
        self.sB_OffTime5.setObjectName(u"sB_OffTime5")
        self.sB_OffTime5.setMaximum(1000)
        self.sB_OffTime5.setValue(500)

        self.fL_OnOffTime5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime5)

        self.l_OffTime5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_OffTime5.setObjectName(u"l_OffTime5")

        self.fL_OnOffTime5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime5)


        self.vL_Parameter5.addLayout(self.fL_OnOffTime5)

        self.vS_Parameter5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter5.addItem(self.vS_Parameter5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.l_DiffAbort5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_DiffAbort5.setObjectName(u"l_DiffAbort5")

        self.horizontalLayout_5.addWidget(self.l_DiffAbort5)

        self.sB_DiffAbort5 = QSpinBox(self.horizontalLayoutWidget_5)
        self.sB_DiffAbort5.setObjectName(u"sB_DiffAbort5")

        self.horizontalLayout_5.addWidget(self.sB_DiffAbort5)


        self.vL_Parameter5.addLayout(self.horizontalLayout_5)

        self.fL_Cnt5 = QFormLayout()
        self.fL_Cnt5.setObjectName(u"fL_Cnt5")
        self.fL_Cnt5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_CntOut5.setObjectName(u"l_CntOut5")

        self.fL_Cnt5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut5)

        self.l_CntIn5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_CntIn5.setObjectName(u"l_CntIn5")

        self.fL_Cnt5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn5)

        self.l_CntOutVal5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_CntOutVal5.setObjectName(u"l_CntOutVal5")

        self.fL_Cnt5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal5)

        self.l_CntInVal5 = QLabel(self.horizontalLayoutWidget_5)
        self.l_CntInVal5.setObjectName(u"l_CntInVal5")

        self.fL_Cnt5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal5)


        self.vL_Parameter5.addLayout(self.fL_Cnt5)


        self.hL_Logic5.addLayout(self.vL_Parameter5)

        self.tabWidget.addTab(self.tab_B5, "")
        self.tab_B6 = QWidget()
        self.tab_B6.setObjectName(u"tab_B6")
        self.horizontalLayoutWidget_6 = QWidget(self.tab_B6)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.hL_Logic6.setObjectName(u"hL_Logic6")
        self.hL_Logic6.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic6 = QFormLayout()
        self.fL_Logic6.setObjectName(u"fL_Logic6")
        self.pB_Start6 = QPushButton(self.horizontalLayoutWidget_6)
        self.pB_Start6.setObjectName(u"pB_Start6")

        self.fL_Logic6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start6)

        self.pB_Stop6 = QPushButton(self.horizontalLayoutWidget_6)
        self.pB_Stop6.setObjectName(u"pB_Stop6")

        self.fL_Logic6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop6)

        self.vS_LogicButtons6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic6.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons6)

        self.pB_Clear6 = QPushButton(self.horizontalLayoutWidget_6)
        self.pB_Clear6.setObjectName(u"pB_Clear6")

        self.fL_Logic6.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear6)

        self.toggle_Button_settings6 = AnimatedToggle(self.horizontalLayoutWidget_6)
        self.toggle_Button_settings6.setObjectName(u"toggle_Button_settings6")

        self.fL_Logic6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings6)

        self.l_RunState6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_RunState6.setObjectName(u"l_RunState6")
        self.l_RunState6.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState6)


        self.hL_Logic6.addLayout(self.fL_Logic6)

        self.vL_Parameter6 = QVBoxLayout()
        self.vL_Parameter6.setObjectName(u"vL_Parameter6")
        self.fL_OnOffTime6 = QFormLayout()
        self.fL_OnOffTime6.setObjectName(u"fL_OnOffTime6")
        self.fL_OnOffTime6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_OnTime6.setObjectName(u"l_OnTime6")

        self.fL_OnOffTime6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime6)

        self.sB_OnTime6 = QSpinBox(self.horizontalLayoutWidget_6)
        self.sB_OnTime6.setObjectName(u"sB_OnTime6")
        self.sB_OnTime6.setMaximum(1000)
        self.sB_OnTime6.setValue(500)

        self.fL_OnOffTime6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime6)

        self.sB_OffTime6 = QSpinBox(self.horizontalLayoutWidget_6)
        self.sB_OffTime6.setObjectName(u"sB_OffTime6")
        self.sB_OffTime6.setMaximum(1000)
        self.sB_OffTime6.setValue(500)

        self.fL_OnOffTime6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime6)

        self.l_OffTime6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_OffTime6.setObjectName(u"l_OffTime6")

        self.fL_OnOffTime6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime6)


        self.vL_Parameter6.addLayout(self.fL_OnOffTime6)

        self.vS_Parameter6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter6.addItem(self.vS_Parameter6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.l_DiffAbort6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_DiffAbort6.setObjectName(u"l_DiffAbort6")

        self.horizontalLayout_6.addWidget(self.l_DiffAbort6)

        self.sB_DiffAbort6 = QSpinBox(self.horizontalLayoutWidget_6)
        self.sB_DiffAbort6.setObjectName(u"sB_DiffAbort6")

        self.horizontalLayout_6.addWidget(self.sB_DiffAbort6)


        self.vL_Parameter6.addLayout(self.horizontalLayout_6)

        self.fL_Cnt6 = QFormLayout()
        self.fL_Cnt6.setObjectName(u"fL_Cnt6")
        self.fL_Cnt6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_CntOut6.setObjectName(u"l_CntOut6")

        self.fL_Cnt6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut6)

        self.l_CntIn6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_CntIn6.setObjectName(u"l_CntIn6")

        self.fL_Cnt6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn6)

        self.l_CntOutVal6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_CntOutVal6.setObjectName(u"l_CntOutVal6")

        self.fL_Cnt6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal6)

        self.l_CntInVal6 = QLabel(self.horizontalLayoutWidget_6)
        self.l_CntInVal6.setObjectName(u"l_CntInVal6")

        self.fL_Cnt6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal6)


        self.vL_Parameter6.addLayout(self.fL_Cnt6)


        self.hL_Logic6.addLayout(self.vL_Parameter6)

        self.tabWidget.addTab(self.tab_B6, "")
        self.tab_B7 = QWidget()
        self.tab_B7.setObjectName(u"tab_B7")
        self.horizontalLayoutWidget_7 = QWidget(self.tab_B7)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.hL_Logic7.setObjectName(u"hL_Logic7")
        self.hL_Logic7.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic7 = QFormLayout()
        self.fL_Logic7.setObjectName(u"fL_Logic7")
        self.pB_Start7 = QPushButton(self.horizontalLayoutWidget_7)
        self.pB_Start7.setObjectName(u"pB_Start7")

        self.fL_Logic7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start7)

        self.pB_Stop7 = QPushButton(self.horizontalLayoutWidget_7)
        self.pB_Stop7.setObjectName(u"pB_Stop7")

        self.fL_Logic7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop7)

        self.vS_LogicButtons7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic7.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons7)

        self.pB_Clear7 = QPushButton(self.horizontalLayoutWidget_7)
        self.pB_Clear7.setObjectName(u"pB_Clear7")

        self.fL_Logic7.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear7)

        self.toggle_Button_settings7 = AnimatedToggle(self.horizontalLayoutWidget_7)
        self.toggle_Button_settings7.setObjectName(u"toggle_Button_settings7")

        self.fL_Logic7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings7)

        self.l_RunState7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_RunState7.setObjectName(u"l_RunState7")
        self.l_RunState7.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState7)


        self.hL_Logic7.addLayout(self.fL_Logic7)

        self.vL_Parameter7 = QVBoxLayout()
        self.vL_Parameter7.setObjectName(u"vL_Parameter7")
        self.fL_OnOffTime7 = QFormLayout()
        self.fL_OnOffTime7.setObjectName(u"fL_OnOffTime7")
        self.fL_OnOffTime7.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_OnTime7.setObjectName(u"l_OnTime7")

        self.fL_OnOffTime7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime7)

        self.sB_OnTime7 = QSpinBox(self.horizontalLayoutWidget_7)
        self.sB_OnTime7.setObjectName(u"sB_OnTime7")
        self.sB_OnTime7.setMaximum(1000)
        self.sB_OnTime7.setValue(500)

        self.fL_OnOffTime7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime7)

        self.sB_OffTime7 = QSpinBox(self.horizontalLayoutWidget_7)
        self.sB_OffTime7.setObjectName(u"sB_OffTime7")
        self.sB_OffTime7.setMaximum(1000)
        self.sB_OffTime7.setValue(500)

        self.fL_OnOffTime7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime7)

        self.l_OffTime7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_OffTime7.setObjectName(u"l_OffTime7")

        self.fL_OnOffTime7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime7)


        self.vL_Parameter7.addLayout(self.fL_OnOffTime7)

        self.vS_Parameter7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter7.addItem(self.vS_Parameter7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.l_DiffAbort7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_DiffAbort7.setObjectName(u"l_DiffAbort7")

        self.horizontalLayout_7.addWidget(self.l_DiffAbort7)

        self.sB_DiffAbort7 = QSpinBox(self.horizontalLayoutWidget_7)
        self.sB_DiffAbort7.setObjectName(u"sB_DiffAbort7")

        self.horizontalLayout_7.addWidget(self.sB_DiffAbort7)


        self.vL_Parameter7.addLayout(self.horizontalLayout_7)

        self.fL_Cnt7 = QFormLayout()
        self.fL_Cnt7.setObjectName(u"fL_Cnt7")
        self.fL_Cnt7.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_CntOut7.setObjectName(u"l_CntOut7")

        self.fL_Cnt7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut7)

        self.l_CntIn7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_CntIn7.setObjectName(u"l_CntIn7")

        self.fL_Cnt7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn7)

        self.l_CntOutVal7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_CntOutVal7.setObjectName(u"l_CntOutVal7")

        self.fL_Cnt7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal7)

        self.l_CntInVal7 = QLabel(self.horizontalLayoutWidget_7)
        self.l_CntInVal7.setObjectName(u"l_CntInVal7")

        self.fL_Cnt7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal7)


        self.vL_Parameter7.addLayout(self.fL_Cnt7)


        self.hL_Logic7.addLayout(self.vL_Parameter7)

        self.tabWidget.addTab(self.tab_B7, "")
        self.tab_B8 = QWidget()
        self.tab_B8.setObjectName(u"tab_B8")
        self.horizontalLayoutWidget_8 = QWidget(self.tab_B8)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(20, 20, 411, 291))
        self.hL_Logic8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.hL_Logic8.setObjectName(u"hL_Logic8")
        self.hL_Logic8.setContentsMargins(0, 0, 0, 0)
        self.fL_Logic8 = QFormLayout()
        self.fL_Logic8.setObjectName(u"fL_Logic8")
        self.pB_Start8 = QPushButton(self.horizontalLayoutWidget_8)
        self.pB_Start8.setObjectName(u"pB_Start8")

        self.fL_Logic8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pB_Start8)

        self.pB_Stop8 = QPushButton(self.horizontalLayoutWidget_8)
        self.pB_Stop8.setObjectName(u"pB_Stop8")

        self.fL_Logic8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.pB_Stop8)

        self.vS_LogicButtons8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fL_Logic8.setItem(3, QFormLayout.ItemRole.LabelRole, self.vS_LogicButtons8)

        self.pB_Clear8 = QPushButton(self.horizontalLayoutWidget_8)
        self.pB_Clear8.setObjectName(u"pB_Clear8")

        self.fL_Logic8.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pB_Clear8)

        self.toggle_Button_settings8 = AnimatedToggle(self.horizontalLayoutWidget_8)
        self.toggle_Button_settings8.setObjectName(u"toggle_Button_settings8")

        self.fL_Logic8.setWidget(2, QFormLayout.ItemRole.LabelRole, self.toggle_Button_settings8)

        self.l_RunState8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_RunState8.setObjectName(u"l_RunState8")
        self.l_RunState8.setStyleSheet(u"background-color: green; color: black")
        self.l_RunState8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fL_Logic8.setWidget(2, QFormLayout.ItemRole.FieldRole, self.l_RunState8)


        self.hL_Logic8.addLayout(self.fL_Logic8)

        self.vL_Parameter8 = QVBoxLayout()
        self.vL_Parameter8.setObjectName(u"vL_Parameter8")
        self.fL_OnOffTime8 = QFormLayout()
        self.fL_OnOffTime8.setObjectName(u"fL_OnOffTime8")
        self.fL_OnOffTime8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_OnTime8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_OnTime8.setObjectName(u"l_OnTime8")

        self.fL_OnOffTime8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_OnTime8)

        self.sB_OnTime8 = QSpinBox(self.horizontalLayoutWidget_8)
        self.sB_OnTime8.setObjectName(u"sB_OnTime8")
        self.sB_OnTime8.setMaximum(1000)
        self.sB_OnTime8.setValue(500)

        self.fL_OnOffTime8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.sB_OnTime8)

        self.sB_OffTime8 = QSpinBox(self.horizontalLayoutWidget_8)
        self.sB_OffTime8.setObjectName(u"sB_OffTime8")
        self.sB_OffTime8.setMaximum(1000)
        self.sB_OffTime8.setValue(500)

        self.fL_OnOffTime8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sB_OffTime8)

        self.l_OffTime8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_OffTime8.setObjectName(u"l_OffTime8")

        self.fL_OnOffTime8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_OffTime8)


        self.vL_Parameter8.addLayout(self.fL_OnOffTime8)

        self.vS_Parameter8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vL_Parameter8.addItem(self.vS_Parameter8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.l_DiffAbort8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_DiffAbort8.setObjectName(u"l_DiffAbort8")

        self.horizontalLayout_8.addWidget(self.l_DiffAbort8)

        self.sB_DiffAbort8 = QSpinBox(self.horizontalLayoutWidget_8)
        self.sB_DiffAbort8.setObjectName(u"sB_DiffAbort8")

        self.horizontalLayout_8.addWidget(self.sB_DiffAbort8)


        self.vL_Parameter8.addLayout(self.horizontalLayout_8)

        self.fL_Cnt8 = QFormLayout()
        self.fL_Cnt8.setObjectName(u"fL_Cnt8")
        self.fL_Cnt8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.l_CntOut8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_CntOut8.setObjectName(u"l_CntOut8")

        self.fL_Cnt8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l_CntOut8)

        self.l_CntIn8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_CntIn8.setObjectName(u"l_CntIn8")

        self.fL_Cnt8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l_CntIn8)

        self.l_CntOutVal8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_CntOutVal8.setObjectName(u"l_CntOutVal8")

        self.fL_Cnt8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.l_CntOutVal8)

        self.l_CntInVal8 = QLabel(self.horizontalLayoutWidget_8)
        self.l_CntInVal8.setObjectName(u"l_CntInVal8")

        self.fL_Cnt8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.l_CntInVal8)


        self.vL_Parameter8.addLayout(self.fL_Cnt8)


        self.hL_Logic8.addLayout(self.vL_Parameter8)

        self.tabWidget.addTab(self.tab_B8, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 371, 319))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_Button3 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button3.setObjectName(u"toggle_Button3")

        self.gridLayout_2.addWidget(self.toggle_Button3, 3, 1, 1, 1)

        self.lbl_toggleAll = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleAll.setObjectName(u"lbl_toggleAll")
        self.lbl_toggleAll.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleAll, 0, 0, 1, 1)

        self.toggle_Button6 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button6.setObjectName(u"toggle_Button6")

        self.gridLayout_2.addWidget(self.toggle_Button6, 6, 1, 1, 1)

        self.lbl_Button8_3 = QLabel(self.gridLayoutWidget_2)
        self.lbl_Button8_3.setObjectName(u"lbl_Button8_3")
        self.lbl_Button8_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_Button8_3, 7, 0, 1, 1)

        self.lbl_Button8_2 = QLabel(self.gridLayoutWidget_2)
        self.lbl_Button8_2.setObjectName(u"lbl_Button8_2")
        self.lbl_Button8_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_Button8_2, 8, 0, 1, 1)

        self.lbl_ManualLed_Out6 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out6.setObjectName(u"lbl_ManualLed_Out6")
        self.lbl_ManualLed_Out6.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out6.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out6.setAutoFillBackground(False)
        self.lbl_ManualLed_Out6.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out6, 6, 3, 1, 1)

        self.toggle_Button2 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button2.setObjectName(u"toggle_Button2")

        self.gridLayout_2.addWidget(self.toggle_Button2, 2, 1, 1, 1)

        self.toggle_Button8 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button8.setObjectName(u"toggle_Button8")

        self.gridLayout_2.addWidget(self.toggle_Button8, 8, 1, 1, 1)

        self.lbl_toggleButton3 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton3.setObjectName(u"lbl_toggleButton3")
        self.lbl_toggleButton3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton3, 3, 0, 1, 1)

        self.lbl_ManualLed_Out4 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out4.setObjectName(u"lbl_ManualLed_Out4")
        self.lbl_ManualLed_Out4.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out4.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out4.setAutoFillBackground(False)
        self.lbl_ManualLed_Out4.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out4, 4, 3, 1, 1)

        self.lbl_ManualLed_Out3 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out3.setObjectName(u"lbl_ManualLed_Out3")
        self.lbl_ManualLed_Out3.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out3.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out3.setAutoFillBackground(False)
        self.lbl_ManualLed_Out3.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out3, 3, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.lbl_ManualLed_Out2 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out2.setObjectName(u"lbl_ManualLed_Out2")
        self.lbl_ManualLed_Out2.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out2.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out2.setAutoFillBackground(False)
        self.lbl_ManualLed_Out2.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out2, 2, 3, 1, 1)

        self.lbl_ManualLed_Out1 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out1.setObjectName(u"lbl_ManualLed_Out1")
        self.lbl_ManualLed_Out1.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out1.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out1.setAutoFillBackground(False)
        self.lbl_ManualLed_Out1.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out1, 1, 3, 1, 1)

        self.lbl_ManualLed_Out7 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out7.setObjectName(u"lbl_ManualLed_Out7")
        self.lbl_ManualLed_Out7.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out7.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out7.setAutoFillBackground(False)
        self.lbl_ManualLed_Out7.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out7, 7, 3, 1, 1)

        self.lbl_toggleButton6 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton6.setObjectName(u"lbl_toggleButton6")
        self.lbl_toggleButton6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton6, 6, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)

        self.lbl_ManualLed_Out5 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out5.setObjectName(u"lbl_ManualLed_Out5")
        self.lbl_ManualLed_Out5.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out5.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out5.setAutoFillBackground(False)
        self.lbl_ManualLed_Out5.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out5, 5, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.lbl_toggleButton2 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton2.setObjectName(u"lbl_toggleButton2")
        self.lbl_toggleButton2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton2, 2, 0, 1, 1)

        self.lbl_toggleButton5 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton5.setObjectName(u"lbl_toggleButton5")
        self.lbl_toggleButton5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton5, 5, 0, 1, 1)

        self.toggle_Button4 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button4.setObjectName(u"toggle_Button4")

        self.gridLayout_2.addWidget(self.toggle_Button4, 4, 1, 1, 1)

        self.toggle_Button7 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button7.setObjectName(u"toggle_Button7")

        self.gridLayout_2.addWidget(self.toggle_Button7, 7, 1, 1, 1)

        self.lbl_toggleButton1 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton1.setObjectName(u"lbl_toggleButton1")
        self.lbl_toggleButton1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton1, 1, 0, 1, 1)

        self.toggle_All = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_All.setObjectName(u"toggle_All")

        self.gridLayout_2.addWidget(self.toggle_All, 0, 1, 1, 1)

        self.toggle_Button1 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button1.setObjectName(u"toggle_Button1")

        self.gridLayout_2.addWidget(self.toggle_Button1, 1, 1, 1, 1)

        self.toggle_Button5 = AnimatedToggle(self.gridLayoutWidget_2)
        self.toggle_Button5.setObjectName(u"toggle_Button5")

        self.gridLayout_2.addWidget(self.toggle_Button5, 5, 1, 1, 1)

        self.lbl_toggleButton4 = QLabel(self.gridLayoutWidget_2)
        self.lbl_toggleButton4.setObjectName(u"lbl_toggleButton4")
        self.lbl_toggleButton4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_toggleButton4, 4, 0, 1, 1)

        self.lbl_ManualLed_Out8 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_Out8.setObjectName(u"lbl_ManualLed_Out8")
        self.lbl_ManualLed_Out8.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_Out8.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_Out8.setAutoFillBackground(False)
        self.lbl_ManualLed_Out8.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_Out8, 8, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Shape.NoFrame)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 5, 1, 1)

        self.lbl_ManualLed_In1 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In1.setObjectName(u"lbl_ManualLed_In1")
        self.lbl_ManualLed_In1.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In1.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In1.setAutoFillBackground(False)
        self.lbl_ManualLed_In1.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In1, 1, 5, 1, 1)

        self.lbl_ManualLed_In2 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In2.setObjectName(u"lbl_ManualLed_In2")
        self.lbl_ManualLed_In2.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In2.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In2.setAutoFillBackground(False)
        self.lbl_ManualLed_In2.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In2, 2, 5, 1, 1)

        self.lbl_ManualLed_In3 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In3.setObjectName(u"lbl_ManualLed_In3")
        self.lbl_ManualLed_In3.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In3.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In3.setAutoFillBackground(False)
        self.lbl_ManualLed_In3.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In3, 3, 5, 1, 1)

        self.lbl_ManualLed_In4 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In4.setObjectName(u"lbl_ManualLed_In4")
        self.lbl_ManualLed_In4.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In4.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In4.setAutoFillBackground(False)
        self.lbl_ManualLed_In4.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In4, 4, 5, 1, 1)

        self.lbl_ManualLed_In5 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In5.setObjectName(u"lbl_ManualLed_In5")
        self.lbl_ManualLed_In5.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In5.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In5.setAutoFillBackground(False)
        self.lbl_ManualLed_In5.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In5, 5, 5, 1, 1)

        self.lbl_ManualLed_In6 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In6.setObjectName(u"lbl_ManualLed_In6")
        self.lbl_ManualLed_In6.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In6.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In6.setAutoFillBackground(False)
        self.lbl_ManualLed_In6.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In6, 6, 5, 1, 1)

        self.lbl_ManualLed_In7 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In7.setObjectName(u"lbl_ManualLed_In7")
        self.lbl_ManualLed_In7.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In7.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In7.setAutoFillBackground(False)
        self.lbl_ManualLed_In7.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In7, 7, 5, 1, 1)

        self.lbl_ManualLed_In8 = QLabel(self.gridLayoutWidget_2)
        self.lbl_ManualLed_In8.setObjectName(u"lbl_ManualLed_In8")
        self.lbl_ManualLed_In8.setMinimumSize(QSize(31, 31))
        self.lbl_ManualLed_In8.setMaximumSize(QSize(31, 31))
        self.lbl_ManualLed_In8.setAutoFillBackground(False)
        self.lbl_ManualLed_In8.setStyleSheet(u"background-color: green;")

        self.gridLayout_2.addWidget(self.lbl_ManualLed_In8, 8, 5, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 21))
        self.menuAllgemein = QMenu(self.menubar)
        self.menuAllgemein.setObjectName(u"menuAllgemein")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAllgemein.menuAction())
        self.menuAllgemein.addAction(self.actionVersion_2)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TikTak", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.actionVersion_2.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.lbl_Button6.setText(QCoreApplication.translate("MainWindow", u"Taster 6", None))
        self.lbl_OutputLed6.setText("")
        self.lbl_OutputCnt6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed6.setText("")
        self.lbl_InputCnt6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings6.setText(QCoreApplication.translate("MainWindow", u"Taster 6\n"
"Einstellungen", None))
        self.lbl_Button5.setText(QCoreApplication.translate("MainWindow", u"Taster 5", None))
        self.lbl_Button8.setText(QCoreApplication.translate("MainWindow", u"Taster 8", None))
        self.lbl_OutputLed5.setText("")
        self.lbl_OutputCnt5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed5.setText("")
        self.lbl_InputCnt5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings5.setText(QCoreApplication.translate("MainWindow", u"Taster 5\n"
"Einstellungen", None))
        self.lbl_Button7.setText(QCoreApplication.translate("MainWindow", u"Taster 7", None))
        self.lbl_OutputLed4.setText("")
        self.lbl_OutputCnt4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed4.setText("")
        self.lbl_InputCnt4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings4.setText(QCoreApplication.translate("MainWindow", u"Taster 4\n"
"Einstellungen", None))
        self.lbl_Button4.setText(QCoreApplication.translate("MainWindow", u"Taster 4", None))
        self.lbl_OutputLed7.setText("")
        self.lbl_OutputCnt7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed7.setText("")
        self.lbl_InputCnt7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings7.setText(QCoreApplication.translate("MainWindow", u"Taster 7\n"
"Einstellungen", None))
        self.lbl_Button1.setText(QCoreApplication.translate("MainWindow", u"Taster 1", None))
        self.lbl_Button3.setText(QCoreApplication.translate("MainWindow", u"Taster 3", None))
        self.lbl_OutputLed2.setText("")
        self.lbl_OutputCnt2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed2.setText("")
        self.lbl_InputCnt2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings2.setText(QCoreApplication.translate("MainWindow", u"Taster 2\n"
"Einstellungen", None))
        self.lbl_OutputLed1.setText("")
        self.lbl_OutputCnt1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed1.setText("")
        self.lbl_InputCnt1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings1.setText(QCoreApplication.translate("MainWindow", u"Taster 1\n"
"Einstellungen", None))
        self.lbl_Button2.setText(QCoreApplication.translate("MainWindow", u"Taster 2", None))
        self.lbl_OutputLed3.setText("")
        self.lbl_OutputCnt3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed3.setText("")
        self.lbl_InputCnt3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings3.setText(QCoreApplication.translate("MainWindow", u"Taster 3\n"
"Einstellungen", None))
        self.lbl_OutputLed8.setText("")
        self.lbl_OutputCnt8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_InputLed8.setText("")
        self.lbl_InputCnt8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pB_ButtonSettings8.setText(QCoreApplication.translate("MainWindow", u"Taster 8\n"
"Einstellungen", None))
        self.pB_StartAll.setText(QCoreApplication.translate("MainWindow", u"Start All", None))
        self.pB_StopAll.setText(QCoreApplication.translate("MainWindow", u"Stop All", None))
        self.pB_ClearAll.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.lbl_Output_Active.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.lbl_Input_active.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pB_Start1.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop1.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear1.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.l_RunState1.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime1.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime1.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort1.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut1.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn1.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B1), QCoreApplication.translate("MainWindow", u"Taster 1", None))
        self.pB_Start2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.l_RunState2.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime2.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime2.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort2.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut2.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn2.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B2), QCoreApplication.translate("MainWindow", u"Taster 2", None))
        self.pB_Start3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear3.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings3.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 3", None))
        self.l_RunState3.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime3.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime3.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort3.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut3.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn3.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B3), QCoreApplication.translate("MainWindow", u"Taster 3", None))
        self.pB_Start4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop4.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear4.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings4.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 4", None))
        self.l_RunState4.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime4.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime4.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort4.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut4.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn4.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B4), QCoreApplication.translate("MainWindow", u"Taster 4", None))
        self.pB_Start5.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop5.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear5.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings5.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 5", None))
        self.l_RunState5.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime5.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime5.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort5.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut5.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn5.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B5), QCoreApplication.translate("MainWindow", u"Taster 5", None))
        self.pB_Start6.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop6.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear6.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings6.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 6", None))
        self.l_RunState6.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime6.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime6.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort6.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut6.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn6.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B6), QCoreApplication.translate("MainWindow", u"Taster 6", None))
        self.pB_Start7.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop7.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings7.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 7", None))
        self.l_RunState7.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime7.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime7.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort7.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut7.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn7.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B7), QCoreApplication.translate("MainWindow", u"Taster 7", None))
        self.pB_Start8.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pB_Stop8.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pB_Clear8.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.toggle_Button_settings8.setText(QCoreApplication.translate("MainWindow", u"toggle Button settings 8", None))
        self.l_RunState8.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.l_OnTime8.setText(QCoreApplication.translate("MainWindow", u"On Time (ms):", None))
        self.l_OffTime8.setText(QCoreApplication.translate("MainWindow", u"Off Time (ms):", None))
        self.l_DiffAbort8.setText(QCoreApplication.translate("MainWindow", u"max. Diff. Abort:", None))
        self.l_CntOut8.setText(QCoreApplication.translate("MainWindow", u"Counter Out:", None))
        self.l_CntIn8.setText(QCoreApplication.translate("MainWindow", u"Counter In:", None))
        self.l_CntOutVal8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_CntInVal8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_B8), QCoreApplication.translate("MainWindow", u"Taster 8", None))
        self.toggle_Button3.setText(QCoreApplication.translate("MainWindow", u"toggle Button3", None))
        self.lbl_toggleAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.toggle_Button6.setText(QCoreApplication.translate("MainWindow", u"toggle Button6", None))
        self.lbl_Button8_3.setText(QCoreApplication.translate("MainWindow", u"Taster 7", None))
        self.lbl_Button8_2.setText(QCoreApplication.translate("MainWindow", u"Taster 8", None))
        self.lbl_ManualLed_Out6.setText("")
        self.toggle_Button2.setText(QCoreApplication.translate("MainWindow", u"toggle Button2", None))
        self.toggle_Button8.setText(QCoreApplication.translate("MainWindow", u"toggle Button8", None))
        self.lbl_toggleButton3.setText(QCoreApplication.translate("MainWindow", u"Taster 3", None))
        self.lbl_ManualLed_Out4.setText("")
        self.lbl_ManualLed_Out3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.lbl_ManualLed_Out2.setText("")
        self.lbl_ManualLed_Out1.setText("")
        self.lbl_ManualLed_Out7.setText("")
        self.lbl_toggleButton6.setText(QCoreApplication.translate("MainWindow", u"Taster 6", None))
        self.label_3.setText("")
        self.lbl_ManualLed_Out5.setText("")
        self.label.setText("")
        self.lbl_toggleButton2.setText(QCoreApplication.translate("MainWindow", u"Taster 2", None))
        self.lbl_toggleButton5.setText(QCoreApplication.translate("MainWindow", u"Taster 5", None))
        self.toggle_Button4.setText(QCoreApplication.translate("MainWindow", u"toggle Button4", None))
        self.toggle_Button7.setText(QCoreApplication.translate("MainWindow", u"toggle Button7", None))
        self.lbl_toggleButton1.setText(QCoreApplication.translate("MainWindow", u"Taster 1", None))
        self.toggle_All.setText(QCoreApplication.translate("MainWindow", u"toggle All", None))
        self.toggle_Button1.setText(QCoreApplication.translate("MainWindow", u"toggle Button1", None))
        self.toggle_Button5.setText(QCoreApplication.translate("MainWindow", u"toggle Button5", None))
        self.lbl_toggleButton4.setText(QCoreApplication.translate("MainWindow", u"Taster 4", None))
        self.lbl_ManualLed_Out8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.lbl_ManualLed_In1.setText("")
        self.lbl_ManualLed_In2.setText("")
        self.lbl_ManualLed_In3.setText("")
        self.lbl_ManualLed_In4.setText("")
        self.lbl_ManualLed_In5.setText("")
        self.lbl_ManualLed_In6.setText("")
        self.lbl_ManualLed_In7.setText("")
        self.lbl_ManualLed_In8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Manuell", None))
        self.menuAllgemein.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

