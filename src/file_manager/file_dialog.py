"""
Содержит класс FileDialog, который отображает диалоговые окна для открытия и сохранения файлов.
"""

import os
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QWidget


class FileDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def open_file_dialog(self, file_filter="", initial_dir="."):
        # Создаем диалоговое окно для открытия файла
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", initial_dir, file_filter
        )

        # Проверяем, выбран ли файл
        if file_name:
            # Возвращаем путь к выбранному файлу
            return file_name

        # Если файл не выбран, возвращаем пустую строку
        return ""

    def save_file_dialog(self, file_filter="", initial_dir="."):
        # Создаем диалоговое окно для сохранения файла
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", initial_dir, file_filter
        )

        # Проверяем, выбрано ли имя файла
        if file_name:
            # Возвращаем путь к выбранному файлу
            return file_name

        # Если имя файла не выбрано, возвращаем пустую строку
        return ""
