#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QGridLayout, QLabel
from PySide2.QtCore import Qt

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок. Если какая-нибудь кнопка включается, 
то в метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть не должно.
"""

persons = {
    'Николай': '+7 933 446-50-25',
    'Дмитрий': '+7 934 447-00-10',
    'Игорь': '+7 935 448-20-20'
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task5")
        self.setGeometry(470, 390, 470, 390)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.radio_button_1 = QPushButton('Николай')
        self.radio_button_1.setCheckable(True)
        self.radio_button_2 = QPushButton('Дмитрий')
        self.radio_button_2.setCheckable(True)
        self.radio_button_3 = QPushButton('Игорь')
        self.radio_button_3.setCheckable(True)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)
        self.button_group.buttonClicked.connect(self._radiobtn_clk)
        self.grid_layot()
        self.show()

    def grid_layot(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.radio_button_1, 1, 0)
        grid.addWidget(self.radio_button_2, 2, 0)
        grid.addWidget(self.radio_button_3, 3, 0)
        grid.addWidget(self.label, 2, 2)
        self.setLayout(grid)

    def _radiobtn_clk(self, button):
        self.label.setText(persons[button.text()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
