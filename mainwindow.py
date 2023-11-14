# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
                               QMessageBox, QTableWidgetItem, QHeaderView, QPushButton)
from PySide6.QtCore import QCoreApplication

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow, Ui_OneLabelWindow, Ui_TwoLabelWindow
import pymysql

#AUXILIARY WINDOWS
#ADD WINDOW
class AddWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TwoLabelWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('ADD Window')

        self.ui.label_1.setText(QCoreApplication.translate("Ui_TwoLabelWindow", u"ID", None))
        self.ui.label_2.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"COUNT", None))
        self.ui.pushButton.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"ADD", None))

        self.ui.pushButton.clicked.connect(self.add)

    def add(self):
        if (self.ui.lineEdit_1.text() == '') or (self.ui.lineEdit_2.text() == ''):
            msg = QMessageBox(self)
            msg.setWindowTitle('Notification')
            msg.setText('Field values cannot be empty!')
            msg.exec()
            return
        
        db.add(int(self.ui.lineEdit_1.text()), int(self.ui.lineEdit_2.text()))

        self.close()

#REMOVE WINDOW
class RemoveWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TwoLabelWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('REMOVE Window')

        self.ui.label_1.setText(QCoreApplication.translate("Ui_TwoLabelWindow", u"ID", None))
        self.ui.label_2.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"COUNT", None))
        self.ui.pushButton.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"REMOVE", None))

        self.ui.pushButton.clicked.connect(self.remove)

    def remove(self):
        if (self.ui.lineEdit_1.text() == '') or (self.ui.lineEdit_2.text() == ''):
            msg = QMessageBox(self)
            msg.setWindowTitle('Notification')
            msg.setText('Field values cannot be empty!')
            msg.exec()
            return
        
        db.remove(int(self.ui.lineEdit_1.text()), int(self.ui.lineEdit_2.text()))

        self.close()

#CHANGE WINDOW
class ChangePriceWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TwoLabelWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('CHANGE Window')

        self.ui.label_1.setText(QCoreApplication.translate("Ui_TwoLabelWindow", u"ID", None))
        self.ui.label_2.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"PRICE", None))
        self.ui.pushButton.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"CHANGE", None))

        self.ui.pushButton.clicked.connect(self.change)

    def change(self):
        if (self.ui.lineEdit_1.text() == '') or (self.ui.lineEdit_2.text() == ''):
            msg = QMessageBox(self)
            msg.setWindowTitle('Notification')
            msg.setText('Field values cannot be empty!')
            msg.exec()
            return
        
        db.setPrice(int(self.ui.lineEdit_1.text()), int(self.ui.lineEdit_2.text()))

        self.close()

#
class FindWindow(QWidget):
    def __init__(self, table, parent=None):
        super().__init__(parent)
        self.ui = Ui_OneLabelWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('FIND Window')

        self.table = table

        self.ui.pushButton.clicked.connect(self.find)
        self.ui.label.setText(QCoreApplication.translate("Ui_OneLabelWindow", u"Name", None))

    def find(self):
        if self.ui.lineEdit.text() == '':
            msg = QMessageBox(self)
            msg.setWindowTitle('Notification')
            msg.setText('Field values cannot be empty!')
            msg.exec()
            return

        data = db.find(self.ui.lineEdit.text())
        if(len(data) == 0):
            msg = QMessageBox(self)
            msg.setWindowTitle('Notification')
            msg.setText('There are no goods with the specified Name!')
            msg.exec()
            return
        self.table.setRowCount(1)
        self.table.setColumnCount(3)

        column_names = ['ID', 'Name', 'Quantity']
        self.table.setHorizontalHeaderLabels(column_names)#Задаем имена столбцам
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)#Растягиваем столбцы по размеру содержимого

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table.setItem(row_num, col_num, item)

        self.close()

#MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #AUXILIARY VARIABLES
        self.anotherWin = None

        #WINDOW SETTINGS
        self.setFixedSize(800, 600)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #UPDATE DATA FROM DB
        self.ui.updateDBButton.clicked.connect(self.updateDB)

        self.ui.findButton.clicked.connect(self.find)

        #WINDOW BUTTONS
        self.ui.addButton.clicked.connect(self.add)
        self.ui.removeButton.clicked.connect(self.remove)
        self.ui.changeButton.clicked.connect(self.changePrice)

        #ACTION BUTTONS
        self.ui.actionLog_out.triggered.connect(self.log_out)

        #DB
        global db
        db = DataBase()

    #BUTTONS ACTIVES
    def log_out(self):
        print('bye')

    def updateDB(self):
        data = db.getData()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))

        column_names = ['ID', 'Name', 'Category', 'Exparation Date', 'Price', 'Departament', 'Brand', 'Quantity']
        self.ui.tableWidget.setHorizontalHeaderLabels(column_names)#Задаем имена столбцам
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)#Растягиваем столбцы по размеру содержимого

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.ui.tableWidget.setItem(row_num, col_num, item)

    #WINDOWS
    def find(self):
        self.anotherWin = FindWindow(self.ui.tableWidget)
        self.anotherWin.show()

    def add(self):
        self.anotherWin = AddWindow()
        self.anotherWin.show()

    def remove(self):
        self.anotherWin = RemoveWindow()
        self.anotherWin.show()

    def changePrice(self):
        self.anotherWin = ChangePriceWindow()
        self.anotherWin.show()

    #CLOSE EVENT
    def closeEvent(self, event):
        if self.anotherWin is not None:
            self.anotherWin.close()
        event.accept()


#DATA BASE CLASS
class DataBase:
    def __init__(self):
        try:#TRY TO CONNECT
            db = pymysql.connect(
                host="localhost",
                user="root",
                password="Supy1011",
                database="mydb")
            self.cursor = db.cursor()
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Check your internet connection!")
            dlg.exec()
            sys.exit(-1)

    def getData(self):#RETURN DATA FROM DB
        try:
            sql = """
            SELECT
            goods.ID,
            goods.Name,
            category.Name,
            goods.Price,
            department.Name,
            brand.Name,
            goods.Quantity
            FROM goods
            LEFT JOIN category ON goods.CategoryID = category.ID
            LEFT JOIN department ON goods.DepartnemtID = department.ID
            LEFT JOIN brand ON goods.BrandID = brand.ID;
            """
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            #result = "\n".join([str(row) for row in data])
            return data
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Error connecting to DB")
            dlg.exec()
            print(ex)
            return -1

    def add(self, ID, changes):
        sql = f'UPDATE goods SET Quantity = Quantity + {changes} WHERE ID = {ID}'
        try:
            self.cursor.execute(sql)
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Error connecting to DB")
            dlg.exec()
            print(ex)
            return -1

    def remove(self, ID, changes):
        sql = f'UPDATE goods SET Quantity = Quantity - {changes} WHERE ID = {ID}'
        try:
            self.cursor.execute(sql)
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Error connecting to DB")
            dlg.exec()
            print(ex)
            return -1

    def setPrice(self, ID, Price):
        sql = f'UPDATE goods SET Price = {Price} WHERE ID = {ID}'
        try:
            self.cursor.execute(sql)
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Error connecting to DB")
            dlg.exec()
            print(ex)
            return -1

    def find(self, Name):
        sql = f'SELECT goods.ID, goods.Name, goods.Quantity FROM goods WHERE goods.Name = {Name}'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as ex:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Connection error!")
            dlg.setText("Error connecting to DB")
            dlg.exec()
            print(ex)
            return -1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
