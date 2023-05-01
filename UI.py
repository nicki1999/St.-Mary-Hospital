import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Example')
        self.setGeometry(100, 100, 500, 300)

        # Create a table
        table = QTableWidget(self)
        table.setGeometry(50, 50, 700, 400)
        table.setRowCount(3)  # increase row count to 6 to accommodate the new cells
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Name", "Age", "City"])

        # Add some sample data to the table
        data = [["Alice", "25", "New York"],
                ["Bob", "30", "London"],
                ["Charlie", "35", "Paris"],
                ["Dave", "40", "Tokyo"]]
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table.setItem(i+2, j, QTableWidgetItem(item))  # shift row index by 2 to make room for new cells

        # Add new cells on top
        header_cell1 = QTableWidgetItem("Header 1")
        header_cell1.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 0, header_cell1)
        table.setSpan(0, 0, 1, table.columnCount())  # span the cell across all columns

        header_cell2 = QTableWidgetItem("Header 2")
        header_cell2.setTextAlignment(Qt.AlignCenter)
        table.setItem(1, 0, header_cell2)
        table.setSpan(1, 0, 1, table.columnCount())  # span the cell across all columns


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create two instances of MyWindow and show them
    win1 = MyWindow()
    win1.show()
    win2 = MyWindow()
    win2.show()

    sys.exit(app.exec_())
