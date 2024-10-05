from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout


stat_window = QWidget()
stat_window.setWindowTitle("Статистика") #назва вікна
stat_window.resize(200, 150) # змінити розмір вікна
stat_window.move(200, 200) #положення вікна