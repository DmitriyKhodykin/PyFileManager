"""
Contains a FileExplorer class that displays the file system tree.
Each tab contains a different file system tree.
"""

from PyQt6.QtCore import (
    QDir,                  # Provides access to directory structures and their contents.
    QModelIndex,           # Is used to locate data in a data model.
    Qt,                    #
    QSize,                 #
)
from PyQt6.QtGui import (
    QFileSystemModel,      # Provides a data model for the local filesystem.
    QStandardItemModel,    # Provides a generic model for storing custom data.
    QStandardItem,         # Provides an item for use with the QStandardItemModel class.
)
from PyQt6.QtWidgets import (
    QTreeView,             # Provides a default model/view implementation of a tree view.
    QListView,             # 
    QTabWidget,            # Provides a stack of tabbed widgets.
    QWidget,               # Is the base class of all user interface objects.
    QVBoxLayout,           # Lines up widgets vertically.
    QHBoxLayout,           # Lines up widgets horizontally.
    QLabel,                # Provides a text or image display.
    QApplication,          #
    QMainWindow,           #
    QSplitter,             #
    QPushButton,           #
)
import sys


class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Просмотр файлов")
        # self.showMaximized()

        hbox_layout = QHBoxLayout()
        vbox_layout = QVBoxLayout()

        button = QPushButton(self)

        for b in range(15):
            button = QPushButton(self)
            vbox_layout.addWidget(button)

        hbox_layout.addLayout(vbox_layout)

        model = QFileSystemModel()
        model.setRootPath(QDir.rootPath())

        tree_view1 = QTreeView(self)
        tree_view2 = QTreeView(self)

        for view in [tree_view1, tree_view2]:
            view.setModel(model)
            view.setRootIndex(model.index(''))
            view.setSortingEnabled(True)
            view.setColumnWidth(0, 250)
            view.setIconSize(QSize(50, 50))
            hbox_layout.addWidget(view)

        widget = QWidget()
        widget.setLayout(hbox_layout)

        self.setCentralWidget(widget)
        
    def handle_new_button_clicked(self):
        print("New button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_explorer = FileExplorer()
    file_explorer.show()
    app.exec()
