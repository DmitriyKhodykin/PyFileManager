"""
Содержит вспомогательные функции, которые могут быть полезны в разных частях приложения.
"""

import os
from PyQt6.QtWidgets import QMessageBox


def show_message_box(title, message, icon=QMessageBox.Information):
    # Создаем диалоговое окно сообщения
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setIcon(icon)

    # Отображаем диалоговое окно
    msg_box.exec()


def get_file_extension(file_name):
    # Получаем расширение файла
    _, ext = os.path.splitext(file_name)
    return ext.lower()


def is_image_file(file_name):
    # Проверяем, является ли файл изображением по расширению
    ext = get_file_extension(file_name)
    return ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]


def is_text_file(file_name):
    # Проверяем, является ли файл текстовым по расширению
    ext = get_file_extension(file_name)
    return ext in [".txt", ".md", ".py", ".cpp", ".h", ".html", ".css", ".js", ".json"]
