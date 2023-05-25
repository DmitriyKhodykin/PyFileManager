"""
Содержит вспомогательные функции, которые могут быть полезны в разных частях приложения.
"""

import os
import shutil
import mimetypes
from PyQt6.QtWidgets import QMessageBox, QTreeWidgetItem
from PyQt6.QtCore import QFileInfo, QFile, QIODevice
from PyQt6.QtWidgets import QErrorMessage, QApplication
from PyQt6.QtGui import QIcon


def load_project_structure(start_path, tree):
    """
    Load Project structure tree
    :param startpath: 
    :param tree: 
    :return: 
    """
    for element in os.listdir(start_path):
        path_info = start_path + "/" + element
        parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
        if os.path.isdir(path_info):
            load_project_structure(path_info, parent_itm)
            parent_itm.setIcon(0, QIcon('assets/folder.ico'))
        else:
            parent_itm.setIcon(0, QIcon('assets/file.ico'))


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


def get_file_size(file_path):
    # Получаем размер файла в байтах
    return os.path.getsize(file_path)


def get_file_last_modified_time(file_path):
    # Получаем время последней модификации файла
    return os.path.getmtime(file_path)


def copy_file(src_path, dst_path):
    # Копируем файл
    try:
        shutil.copy2(src_path, dst_path)
    except Exception as e:
        error_message = f"Error copying file from {src_path} to {dst_path}: {e}"
        show_error_message_box("Error", error_message)


def delete_file(file_path):
    # Удаляем файл
    try:
        os.remove(file_path)
    except Exception as e:
        error_message = f"Error deleting file {file_path}: {e}"
        show_error_message_box("Error", error_message)


def is_binary_file(file_path):
    # Проверяем, является ли файл бинарным
    if not os.path.isfile(file_path):
        return False

    with open(file_path, "rb") as f:
        CHUNKSIZE = 1024
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
            if b"\0" in chunk:
                return True

    return False


def get_mime_type(file_path):
    # Получаем MIME-тип файла
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type


def read_file(file_path):
    # Читаем содержимое файла
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        error_message = f"Error reading file {file_path}: {e}"
        show_error_message_box("Error", error_message)


def write_file(file_path, text):
    # Записываем содержимое в файл
    try:
        with open(file_path, "w") as f:
            f.write(text)
    except Exception as e:
        error_message = f"Error writing to file {file_path}: {e}"
        show_error_message_box("Error", error_message)


def show_error_message_box(title, message):
    # Отображаем диалоговое окно ошибки
    error_dialog = QErrorMessage()
    error_dialog.setWindowTitle(title)
    error_dialog.showMessage(message)
    error_dialog.exec()
