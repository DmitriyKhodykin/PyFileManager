"""
Содержит класс FileExplorer, который отображает дерево файловой системы.
"""

import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTreeView,
    QFileSystemModel,
    QVBoxLayout,
    QWidget,
)


class FileExplorer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создаем модель файловой системы
        self.model = QFileSystemModel()
        self.model.setRootPath("")

        # Создаем виджеты дерева и устанавливаем модель
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        # Устанавливаем корневой каталог
        self.tree.setRootIndex(self.model.index(""))

        # Создаем вертикальный макет и добавляем в него дерево
        layout = QVBoxLayout()
        layout.addWidget(self.tree)

        # Устанавливаем макет
        self.setLayout(layout)


class FileManager(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("File Manager")

        # Создаем экземпляр FileExplorer
        self.file_explorer = FileExplorer()

        # Устанавливаем центральный виджет
        self.setCentralWidget(self.file_explorer)

        # Устанавливаем размер окна
        self.setGeometry(100, 100, 800, 600)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    file_manager = FileManager()
    file_manager.show()
    sys.exit(app.exec())
