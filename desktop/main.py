import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from panels.b33_panel import B33Panel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KI Trading Desktop")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(B33Panel())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
