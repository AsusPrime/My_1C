import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет таблицы для отображения данных
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 780, 580)

        # Вызываем метод для загрузки данных из базы и отображения их в таблице
        self.load_data_from_database()

    def load_data_from_database(self):
        data = (('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'),
            ('asda', 'awdaw'), ('awd', 'fasef'), ('dhtyh', 'ftyju'), ('kghyu', 'ygu'))

        # Устанавливаем количество строк и столбцов в таблице
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))

        # Заполняем таблицу данными из базы
        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_num, col_num, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseViewer()
    window.show()
    sys.exit(app.exec())