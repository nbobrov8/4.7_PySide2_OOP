#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QTextEdit, QHBoxLayout, QPushButton

"""
Напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок "Открыть" и "Сохранить". 
При клике на первую должен открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
должно загружаться в поле типа Text .
При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен сохраняться в файле под именем, 
которое пользователь указал в однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task4")
        self.setGeometry(470, 390, 470, 390)
        self.text_edit = QTextEdit()
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        grid = QHBoxLayout()
        vbox.addLayout(grid)
        btn1 = QPushButton("Сохранить")
        btn1.clicked.connect(self.save)
        btn2 = QPushButton("Открыть")
        btn2.clicked.connect(self.open)
        grid.addWidget(btn1)
        grid.addWidget(btn2)
        vbox.addWidget(self.text_edit)
        self.setLayout(vbox)

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Save File As',
            '',
            "Text Files (*.txt)"
        )
        if filename:
            text = self.text_edit.toPlainText()
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(text)

    def open(self):
        self.text_edit.clear()
        name = QFileDialog.getOpenFileName()
        with open(name[0], 'r', encoding="utf-8") as f:
            data = f.read()
        self.text_edit.setText(str(data))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())