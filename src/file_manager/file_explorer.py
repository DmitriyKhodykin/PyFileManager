"""
Contains a FileExplorer class that displays the file system tree.

The FileExplorer class inherits from QTabWidget to allow you 
to create multiple tabs in one window. 
Each tab contains a different file system tree.

The initUI() method creates two tabs, each of which is created using 
the createTab() method. The createTab() method creates a QStandardItemModel 
and connects it to the QTreeView widget. 

It then adds the expanded and doubleClicked event handlers to respond 
to an expanded node and a double-clicked file or folder.

The onExpanded() and onDoubleClicked() methods update the contents of 
the tree according to the selected path. If the selected path is a folder, 
the onDoubleClicked() method clears.
"""

from PyQt6.QtCore import (
    QDir,                  # Provides access to directory structures and their contents.
    QModelIndex,           # Is used to locate data in a data model.
    Qt                     # 
)
from PyQt6.QtGui import (
    QFileSystemModel,      # Provides a data model for the local filesystem.
    QStandardItemModel,    # Provides a generic model for storing custom data.
    QStandardItem          # Provides an item for use with the QStandardItemModel class.
)
from PyQt6.QtWidgets import (
    QTreeView,             # Provides a default model/view implementation of a tree view.
    QTabWidget,            # Provides a stack of tabbed widgets.
    QWidget,               # Is the base class of all user interface objects.
    QVBoxLayout,           # Lines up widgets vertically.
    QHBoxLayout,           # Lines up widgets horizontally.
    QLabel,                # Provides a text or image display.
    QApplication,          #
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
        # model = QStandardItemModel()
        model = QFileSystemModel()
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
