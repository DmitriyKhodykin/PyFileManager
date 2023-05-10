"""
Содержит основной код приложения и точку входа в программу.
"""

import sys
from PyQt6.QtWidgets import QApplication
from file_manager.file_explorer import FileExplorer


def main():
    app = QApplication(sys.argv)
    file_explorer = FileExplorer()
    file_explorer.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
