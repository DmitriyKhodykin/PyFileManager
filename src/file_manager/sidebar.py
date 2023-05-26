"""
File manager sidebar.
"""

from PyQt6.QtWidgets import (
    QVBoxLayout,           # Lines up widgets vertically.
    QPushButton,           #
)


def sedebar():
    vbox_layout = QVBoxLayout()

    button = QPushButton()

    for b in range(15):
        button = QPushButton()
        vbox_layout.addWidget(button)
    
    return vbox_layout
