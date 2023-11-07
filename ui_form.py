# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTableWidget, QLineEdit, QLabel,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(u"MainWindow")
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setWindowFilePath(u"")
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.updateDBButton = QPushButton(self.centralwidget)
        self.updateDBButton.setObjectName(u"updateDBButton")
        self.updateDBButton.setGeometry(QRect(0, 0, 131, 61))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(0, 70, 131, 61))
        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(0, 140, 131, 61))
        self.changeButton = QPushButton(self.centralwidget)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setGeometry(QRect(0, 210, 131, 61))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 0, 601, 361))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuLog = QMenu(self.menubar)
        self.menuLog.setObjectName(u"menuLog")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuLog.menuAction())
        self.menuLog.addAction(self.actionLog_out)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.updateDBButton.setText(QCoreApplication.translate("MainWindow", u"UPDATE DB", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.changeButton.setText(QCoreApplication.translate("MainWindow", u"CHANGE", None))
        self.menuLog.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        pass
    # retranslateUi


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName(u"AddWindow")
        AddWindow.resize(300, 225)
        self.lineEdit = QLineEdit(AddWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 20, 211, 41))
        self.id = QLabel(AddWindow)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(10, 30, 49, 16))
        self.id.setTextFormat(Qt.AutoText)
        self.name_2 = QLabel(AddWindow)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setGeometry(QRect(10, 80, 49, 16))
        self.name_2.setTextFormat(Qt.AutoText)
        self.lineEdit_2 = QLineEdit(AddWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 70, 211, 41))
        self.name_3 = QLabel(AddWindow)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setGeometry(QRect(10, 130, 49, 16))
        self.name_3.setTextFormat(Qt.AutoText)
        self.lineEdit_3 = QLineEdit(AddWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(60, 120, 211, 41))
        self.pushButton = QPushButton(AddWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 170, 75, 24))

        self.retranslateUi(AddWindow)

        QMetaObject.connectSlotsByName(AddWindow)
    # setupUi

    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", u"AddWindow", None))
        self.id.setText(QCoreApplication.translate("AddWindow", u"ID", None))
        self.name_2.setText(QCoreApplication.translate("AddWindow", u"NAME", None))
        self.name_3.setText(QCoreApplication.translate("AddWindow", u"NAME", None))
        self.pushButton.setText(QCoreApplication.translate("AddWindow", u"PushButton", None))
    # retranslateUi


class Ui_RemoveWindow(object):
    def setupUi(self, RemoveWindow):
        if not RemoveWindow.objectName():
            RemoveWindow.setObjectName(u"RemoveWindow")
        RemoveWindow.resize(300, 100)
        self.lineEdit = QLineEdit(RemoveWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 20, 211, 41))
        self.id = QLabel(RemoveWindow)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(10, 30, 49, 16))
        self.id.setTextFormat(Qt.AutoText)
        self.pushButton = QPushButton(RemoveWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 70, 75, 24))

        self.retranslateUi(RemoveWindow)

        QMetaObject.connectSlotsByName(RemoveWindow)
    # setupUi

    def retranslateUi(self, RemoveWindow):
        RemoveWindow.setWindowTitle(QCoreApplication.translate("RemoveWindow", u"RemoveWindow", None))
        self.id.setText(QCoreApplication.translate("RemoveWindow", u"ID", None))
        self.pushButton.setText(QCoreApplication.translate("RemoveWindow", u"PushButton", None))
    # retranslateUi

