from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox,
    QPushButton, QHBoxLayout, 
    QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup)
from random import randint, shuffle
app = QApplication([])

class Question():
    def __init__(self, question,r_answ, wrong1, wrong2, wrong3):
        self.question = question
        self.r_answ = r_answ
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_l = []
questions_l.append(Question('Ты кто?','Не знаю','Хлеб','Уэнсдей','Николай'))
questions_l.append(Question('Почему Уэнсдей ест хлеб?','Потому что','Он вкусный','Ей просто нечего есть','Она любит хлеб'))
questions_l.append(Question('Как тебя зовут?','Стейси','Зубенко Михаил Петрович','Ангара','Хлеб'))
questions_l.append(Question('Сколько было пилотируемых высадок на Луну?','Шесть','Одна','Десять','Три'))
questions_l.append(Question('Как называется еврейский Новый год?','Рох ха-Шана','Оливье','Новый год','Хашиш-Ара'))
questions_l.append(Question('Как называется семейная стая львов?','Прайд','Пакет','Стадо','Хаги ваги'))
questions_l.append(Question('Кто был главой государства в Японии во время второй мировой войны?','Император Хирохито','Император Эчпочмак','Император Акихито','Николай'))
questions_l.append(Question('Как называют место для нарезки продуктов?','Разделочная доска','Стол','Планшет','Парта'))
questions_l.append(Question('Как называют человка который видит мир в других цветах?','Дальтоник','Дальнозоркий','Великий слепой','Художник'))
questions_l.append(Question('В чём измеряется радиация?','Беккерель','Броколли','Метр','Брахли'))
questions_l.append(Question('Сколько вкусовых рецепторов имеет средний человеческий язык?','10,000','20.000','100.000','500'))
questions_l.append(Question('Каков диаметр баскетбольного кольца в сантиметрах?','45.72 см','46.25 см','42.38 см','49.17 см'))

window = QWidget()
window.setWindowTitle('Opros')
btn_OK = QPushButton ('Ответить')
lb_Question = QLabel ('В каком году была основана Москва?')
RadioGroupBox = QGroupBox ('Варианты ответов')
rbtn_1 = QRadioButton ('1147')
rbtn_2 = QRadioButton ('1242')
rbtn_3 = QRadioButton ('1861')
rbtn_4 = QRadioButton ('1943')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1= QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch (1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout ()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addSpacing(5)
layout_card.addLayout(layout_line3, stretch=8)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(r_answ)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(r_answ)
    show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:  Question):
    shuffle(answers)
    answers[0].setText(q.r_answ)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.r_answ)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answ():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
            print('Рейтинг',(window.score/window.total*100),'%')


def n_question():
    '''window.cur_question = window.cur_question + 1'''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_l) - 1)
    q = questions_l[cur_question]
    '''if window.cur_question >= len(questions_l):
        window.cur_question = 0
    q = questions_l[window.cur_question]'''
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answ()
    else:
        n_question()


btn_OK.clicked.connect(click_ok)
window.score = 0
window.total = 0
n_question()

window.setLayout(layout_card)


window.show()
app.exec()