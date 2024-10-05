from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGroupBox, QWidget, QPushButton, QRadioButton, QSpinBox, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout


window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(500, 400)
window.move(200,200)

window.setStyleSheet('''
background: #47b57e;
font-size: 30px;
''' )

menu_btn = QPushButton("меню")

btn_style = '''

'''
rest_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_label = QLabel("Хвилин")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addWidget(rest_btn)
row1.addWidget(time_box)
row1.addWidget(time_label)

question_text = QLabel("mouse")



btn1 = QRadioButton("миша")
btn2 = QRadioButton("щур")
btn3 = QRadioButton("мишок")
btn4 = QRadioButton("мус")

radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)

group_box = QGroupBox("Варіанти перекладу")

col1 = QVBoxLayout()
col2 = QVBoxLayout()
row2 = QHBoxLayout()

col1.addWidget(btn1)
col1.addWidget(btn2)

col2.addWidget(btn3)
col2.addWidget(btn4)

row2.addLayout(col1)
row2.addLayout(col2)

group_box.setLayout(row2)

result_box = QGroupBox("Результат")
result_text = QLabel("миша")
answer_text = QLabel("миша")

result_col = QVBoxLayout()
result_col.addWidget(result_text)
result_col.addWidget(answer_text,  alignment=Qt.AlignCenter, stretch=2)

result_box.setLayout(result_col)
result_box.hide()
answer_btn = QPushButton("Відповісти")


main_line = QVBoxLayout()
main_line.addLayout(row1, stretch=1)
main_line.addWidget(question_text, alignment=Qt.AlignCenter, stretch=2)
main_line.addWidget(result_box, stretch=5)
main_line.addWidget(group_box, stretch=5)
main_line.addWidget(answer_btn, stretch=3)


window.setLayout(main_line)