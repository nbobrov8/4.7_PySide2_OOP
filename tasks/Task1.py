#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout

"""
Напишите простейший калькулятор, состоящий из двух текстовых полей, куда пользователь вводит числа, и четырех кнопок 
"+", "-", "*", "/". Результат вычисления должен отображаться в метке. Если арифметическое действие выполнить невозможно
(например, если были введены буквы, а не числа), то в метке должно появляться слово "ошибка".
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setGeometry(100, 100, 200, 250)
        self.setWindowTitle("Task1")
        self.label = QLabel("Введите два числа")
        self.label2 = QLabel("Результат")
        self.button1 = QPushButton("+", self)
        self.button2 = QPushButton("-", self)
        self.button3 = QPushButton("*", self)
        self.button4 = QPushButton("/", self)
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.initializeUI()

    def initializeUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit1)
        vbox.addWidget(self.line_edit2)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)

        self.button1.clicked.connect(self.add)
        self.button2.clicked.connect(self.sub)
        self.button3.clicked.connect(self.mul)
        self.button4.clicked.connect(self.div)

    def add(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            rez = str(float(a) + float(b))
            self.label2.setText(rez)
        except ValueError:
            self.label2.setText("Ошибка")

    def sub(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            rez = str(float(a) - float(b))
            self.label2.setText(rez)
        except ValueError:
            self.label2.setText("Ошибка")

    def mul(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            rez = str(float(a) * float(b))
            self.label2.setText(rez)
        except ValueError:
            self.label2.setText("Ошибка")

    def div(self):
        try:
            a = self.line_edit1.text()
            b = self.line_edit2.text()
            rez = str(float(a) / float(b))
            self.label2.setText(rez)
        except ValueError:
            self.label2.setText("Ошибка")
        except ZeroDivisionError:
            self.label2.setText("Деление на 0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
