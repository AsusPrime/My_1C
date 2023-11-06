import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView

class ProductManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Управление продуктами")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        # Создание виджетов
        self.product_name_label = QLabel("Наименование продукта:")
        self.product_name_input = QLineEdit()
        self.add_button = QPushButton("Добавить")
        self.update_button = QPushButton("Изменить")
        self.delete_button = QPushButton("Удалить")
        self.product_table = QTableWidget()

        # Настройка таблицы продуктов
        self.product_table.setColumnCount(2)
        self.product_table.setHorizontalHeaderLabels(["ID", "Наименование продукта"])
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Создание макета
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.product_name_label)
        input_layout.addWidget(self.product_name_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.product_table)

        self.central_widget.setLayout(main_layout)

        # Подключение сигналов к слотам
        self.add_button.clicked.connect(self.add_product)
        self.update_button.clicked.connect(self.update_product)
        self.delete_button.clicked.connect(self.delete_product)
        self.product_table.itemClicked.connect(self.load_selected_product)

        # Инициализация базы данных
        self.init_database()

        # Загрузка данных из базы данных
        self.load_products()

    def init_database(self):
        self.conn = sqlite3.connect("products.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.commit()

    def load_products(self):
        self.product_table.setRowCount(0)
        self.cur.execute("SELECT * FROM products")
        products = self.cur.fetchall()
        for row_num, (product_id, product_name) in enumerate(products):
            self.product_table.insertRow(row_num)
            self.product_table.setItem(row_num, 0, QTableWidgetItem(str(product_id)))
            self.product_table.setItem(row_num, 1, QTableWidgetItem(product_name))

    def add_product(self):
        product_name = self.product_name_input.text()
        if product_name:
            self.cur.execute("INSERT INTO products (name) VALUES (?)", (product_name,))
            self.conn.commit()
            self.load_products()
            self.product_name_input.clear()

    def update_product(self):
        selected_items = self.product_table.selectedItems()
        if selected_items:
            product_id = selected_items[0].text()
            product_name = self.product_name_input.text()
            if product_name:
                self.cur.execute("UPDATE products SET name = ? WHERE id = ?", (product_name, product_id))
                self.conn.commit()
                self.load_products()
                self.product_name_input.clear()

    def delete_product(self):
        selected_items = self.product_table.selectedItems()
        if selected_items:
            product_id = selected_items[0].text()
            self.cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
            self.conn.commit()
            self.load_products()
            self.product_name_input.clear()

    def load_selected_product(self, item):
        self.product_name_input.setText(item.text())

def main():
    app = QApplication(sys.argv)
    window = ProductManagerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
