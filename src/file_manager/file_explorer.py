"""
Содержит класс FileExplorer, который отображает дерево файловой системы.

Класс FileExplorer наследуется от QTabWidget, чтобы позволить создавать 
несколько вкладок в одном окне. Каждая вкладка содержит свое дерево 
файловой системы.

Метод initUI() создает две вкладки, каждая из которых создается с помощью 
метода createTab(). Метод createTab() создает модель QStandardItemModel 
и связывает ее с виджетом QTreeView. 

Затем он добавляет обработчики событий expanded и doubleClicked, 
чтобы реагировать на раскрытие узла и двойной щелчок на файле или папке.

Методы onExpanded() и onDoubleClicked() обновляют содержимое дерева в соответствии 
с выбранным путем. Если выбранный путь является папкой, метод onDoubleClicked() очищает
"""

from PyQt6.QtCore import QDir, QModelIndex, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QTreeView,
    QTabWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QApplication,
)
import sys


class FileExplorer(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Explorer")
        self.treeviews = []
        self.initUI()

    def initUI(self):
        self.addTab(self.createTab(), "Tab 1")
        self.addTab(self.createTab(), "Tab 2")

    def createTab(self):
        model = QStandardItemModel()
        model.setRootPath(QDir.rootPath())

        treeview = QTreeView()
        treeview.setModel(model)
        treeview.setRootIndex(model.index(QDir.rootPath()))
        treeview.setHeaderHidden(True)

        treeview.expanded.connect(self.onExpanded)
        treeview.doubleClicked.connect(self.onDoubleClicked)

        self.treeviews.append(treeview)

        vbox = QVBoxLayout()
        vbox.addWidget(treeview)

        label = QLabel("Selected file: ")
        vbox.addWidget(label)

        widget = QWidget()
        widget.setLayout(vbox)

        return widget

    def onExpanded(self, index: QModelIndex):
        model = index.model()
        path = model.filePath(index)

        if model.rowCount(index) == 0:
            for info in QDir(path).entryInfoList(
                QDir.Files | QDir.Directories | QDir.NoDotAndDotDot
            ):
                item = QStandardItem(info.fileName())
                item.setIcon(self.style().standardIcon(QTreeView.iconsVisible()))
                item.setData(info.filePath(), Qt.UserRole)
                model.appendRow(item)

    def onDoubleClicked(self, index: QModelIndex):
        model = index.model()
        path = model.filePath(index)

        if QDir(path).exists():
            model.removeRows(0, model.rowCount())

            for info in QDir(path).entryInfoList(
                QDir.Files | QDir.Directories | QDir.NoDotAndDotDot
            ):
                item = QStandardItem(info.fileName())
                item.setIcon(self.style().standardIcon(QTreeView.iconsVisible()))
                item.setData(info.filePath(), Qt.UserRole)
                model.appendRow(item)
        else:
            widget = self.currentWidget()
            label = widget.findChild(QLabel)

            if label is not None:
                label.setText(f"Selected file: {path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_explorer = FileExplorer()
    file_explorer.show()
    sys.exit(app.exec())
