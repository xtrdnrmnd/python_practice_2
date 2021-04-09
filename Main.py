from tkinter import *  # Импорт библиотеки для создания графического интерфейса
import random  # подключение модуля случайных чисел random
import Task_One
import Task_Two
import Task_Three

# Создание графического интерфейса

# Создаем окно
root = Tk()
root.title("Лабораторная работа 1")
root.geometry('720x480')
theLabel = Label(root, text="Лабораторная работа 1.")
theLabel.pack()

# Создание объекта класса
LOC = Task_One.LinkedList()
LOC2 = Task_One.LinkedList()
for i in range(20):
    LOC.add(round(random.random(), 1))
textt = "ЛОС, составленный из случайных чисел:"
textt_Label = Label(root, text=textt)
LOC_Label = Label(root, text=LOC.__str__(), wraplength=700)
texxxt = "ЛОС без повторяющихся значений:"
texxxt_Label = Label(root, text=texxxt)
Rand_Label = Label(root)

# Создание объекта класса
Q = Task_Two.Queue()
Q2 = Task_Two.Queue()
for i in range(20):
    Q.enqueue(round(random.randint(0, 100)))
Qt = "Очередь, составленная из случайных чисел:"
Qt_Label = Label(root, text=Qt)
Qtt_Label = Label(root, text=Q.items, wraplength=700)
Qttt = "Количество простых чисел, содержащихся в очереди:"
Qttt_Label = Label(root, text=Qttt)
Simple_Label = Label(root)

# Создание объекта класса
Stack = Task_Three.Stack()
St2 = Task_Three.Stack()
for i in range(20):
    Stack.push(round(random.randint(0, 100)))
St = "Стек, составленный из случайных чисел:"
St_Label = Label(root, text=St)
Stt_Label = Label(root, text=Stack.items, wraplength=700)
Sttt = "Количество простых чисел, содержащихся в стеке:"
Sttt_Label = Label(root, text=Sttt)
Prime_Label = Label(root)

Entry_text = Label(root, text="Введите значение:")
message = StringVar()
EntryA = Entry(root, width=10, font='Arial 14', textvariable=message)  # создаем текстовое поле ввода
Entry_btn = Button(root, text="Добавить значение")
Res_btn = Button(root, text="Завершить ввод")
Res_Label = Label(root)
Ress_Label = Label(root)


def Add_One():
    if message.get() != '':
        r = float(message.get())
        LOC2.add(r)
    EntryA.delete(0, END)


def Add_Two():
    if message.get() != '':
        Q2.enqueue(int(message.get()))
    EntryA.delete(0, END)


def Add_Three():
    if message.get() != '':
        r = int(message.get())
        St2.push(r)
    EntryA.delete(0, END)


def Res_One():
    Res_Label.config(text=LOC2.__str__())
    Res_Label.place(x=20, y=370)
    Ress_Label.config(text=Task_One.LinkedList.RemoveDuplicates(LOC2))
    Ress_Label.place(x=20, y=400)


def Res_Two():
    Res_Label.config(text=Q2.items)
    Res_Label.place(x=20, y=370)
    Ress_Label.config(text=Task_Two.Queue.isPrime(Q2))
    Ress_Label.place(x=20, y=400)


def Res_Three():
    Res_Label.config(text=St2.items)
    Res_Label.place(x=20, y=370)
    Ress_Label.config(text=Task_Three.Stack.isPrime(St2))
    Ress_Label.place(x=20, y=400)


# Метод обработки нажатия на кнопку
def button_clicked():
    taskOneButton.pack_forget()
    taskTwoButton.pack_forget()
    taskThreeButton.pack_forget()


# Функция реализации задания 1
def task_one():
    button_clicked()

    taskLabel1.pack()
    backButton.pack()

    textt_Label.place(x=20, y=160)
    LOC_Label.place(x=20, y=180)
    texxxt_Label.place(x=20, y=200)

    Rand_Label['text'] = Task_One.LinkedList.RemoveDuplicates(LOC)
    Rand_Label.place(x=20, y=220)

    Entry_text.place(x=20, y=260)
    EntryA.place(x=20, y=280)
    Entry_btn['command'] = Add_One
    Entry_btn.place(x=20, y=310)
    Res_btn['command'] = Res_One
    Res_btn.place(x=20, y=340)


# Функция реализации задания 2
def task_two():
    button_clicked()

    taskLabel2.pack()
    backButton.pack()

    Qt_Label.place(x=20, y=160)
    Qtt_Label.place(x=20, y=180)
    Qttt_Label.place(x=20, y=200)

    Simple_Label['text'] = Task_Two.Queue.isPrime(Q)
    Simple_Label.place(x=20, y=220)

    Entry_text.place(x=20, y=260)
    EntryA.place(x=20, y=280)
    Entry_btn['command'] = Add_Two
    Entry_btn.place(x=20, y=310)
    Res_btn['command'] = Res_Two
    Res_btn.place(x=20, y=340)


# Функция реализации задания 3
def task_three():
    button_clicked()

    taskLabel3.pack()
    backButton.pack()

    St_Label.place(x=20, y=160)
    Stt_Label.place(x=20, y=180)
    Sttt_Label.place(x=20, y=200)

    Prime_Label['text'] = Task_Three.Stack.isPrime(Stack)
    Prime_Label.place(x=20, y=220)

    Entry_text.place(x=20, y=260)
    EntryA.place(x=20, y=280)
    Entry_btn['command'] = Add_Three
    Entry_btn.place(x=20, y=310)
    Res_btn['command'] = Res_Three
    Res_btn.place(x=20, y=340)


# Метод обработки кнопки "Назад"
def button_back():
    taskOneButton.pack()
    taskTwoButton.pack()
    taskThreeButton.pack()

    taskLabel1.pack_forget()
    taskLabel2.pack_forget()
    taskLabel3.pack_forget()
    backButton.pack_forget()
    EntryA.place_forget()
    Entry_text.place_forget()
    Entry_btn.place_forget()
    Res_btn.place_forget()
    Res_Label.place_forget()
    Ress_Label.place_forget()

    textt_Label.place_forget()
    LOC_Label.place_forget()
    texxxt_Label.place_forget()
    Rand_Label.place_forget()

    Qt_Label.place_forget()
    Qtt_Label.place_forget()
    Qttt_Label.place_forget()
    Simple_Label.place_forget()

    St_Label.place_forget()
    Stt_Label.place_forget()
    Sttt_Label.place_forget()
    Prime_Label.place_forget()


taskOneButton = Button(root, text="Задание 1", command=task_one, fg='red')
taskTwoButton = Button(root, text="Задание 2", command=task_two, fg='blue')
taskThreeButton = Button(root, text="Задание 3", command=task_three, fg='green')
taskLabel1 = Label(root, wraplength=700,
                   text="Сформировать ЛОС, элементами которого являются вещественные числа (среди которых есть "
                        "повторяющиеся значения). Составить программу, которая по списку строит новый список, "
                        "в котором отсутствуют повторяющиеся значения.")
taskLabel2 = Label(root, wraplength=700,
                   text="Составить программу построения очереди, содержащей целые числа. Вычислить количество "
                        "простых чисел, содержащихся в очереди.")
taskLabel3 = Label(root, wraplength=700,
                   text="Сформируйте исходный стек, элементами которого являются целые числа. Составить программу, "
                        "которая находит количество простых чисел в стеке.")
taskOneButton.pack()
taskTwoButton.pack()
taskThreeButton.pack()
backButton = Button(root, text='Назад', command=button_back)
t1oL = Label(root)

# Задержка окна
root.mainloop()
