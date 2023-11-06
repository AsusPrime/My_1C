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
    QMenuBar, QPushButton, QSizePolicy, QTableWidget,
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

