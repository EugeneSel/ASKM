from tkinter import *
import numpy as np
from matplotlib import pyplot as plt
import sys
import os


def exitWin():
    global root
    root.destroy()


def restart():
    global root
    root.destroy()
    main()


def least_squares (n, y, sse):
    A = np.array([[0.0, 0.0], [0.0, 0.0]])
    B = np.array([0.0, 0.0])

    for i in range(n):
        B[0] += 2 * sse[i]
        B[1] += 2 * sse[i]/y[i]
        A[0, 0] += 2
        A[0, 1] += 2/y[i]
        A[1, 0] += 2/y[i]
        A[1, 1] += 2/y[i] ** 2

    det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    det1 = B[0] * A[1, 1] - A[0, 1] * B[1]
    det2 = A[0, 0] * B[1] - B[0] * A[1, 0]
    a0 = det1/det
    a1 = det2/det

    return a0, a1


def solution():
    enter_field_label1.config(text="Обсяг виробництва:")
    enter_field_label2.config(text="Собівартість одиниці продукції:")
    submit.config(text="Рестарт", command=restart)

    global n
    global y
    global sse

    T_theor = 2.36

    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            if j == 0:
                y[i] = cell.get()
            elif j == 1:
                sse[i] = cell.get()

    a0, a1 = least_squares(n, y, sse)

    equation.config(text="sse = %f + %f / y" % (a0, a1))

    a0_avg = 0
    for i in range(n):
        a0_avg += sse[i] - a1 / y[i]
    a0_avg /= n

    a1_avg = 0
    for i in range(n):
        a1_avg += y[i] * (sse[i] - a0)
    a1_avg /= n

    a0_dev = 0
    for i in range(n):
        a0_dev += ((sse[i] - a1 / y[i]) - a0_avg) ** 2
    a0_dev = np.sqrt(a0_dev / (n - 1))

    a1_dev = 0
    for i in range(n):
        a1_dev += (y[i] * (sse[i] - a0) - a1_avg) ** 2
    a1_dev = np.sqrt(a1_dev / (n - 1))

    y_avg = 0
    for i in range(n):
        y_avg += y[i] / n

    S_y = 0
    for i in range(n):
        S_y += (y[i] - y_avg) ** 2
    S_y = np.sqrt(S_y / (n - 1))

    sse_avg = 0
    for i in range(n):
        sse_avg += sse[i] / n

    S_sse = 0
    for i in range(n):
        S_sse += (sse[i] - sse_avg) ** 2
    S_sse = np.sqrt(S_sse / (n - 1))

    T0 = np.abs(y_avg - a0) * np.sqrt(n) / S_y
    T1 = np.abs(sse_avg - a1) * np.sqrt(n) / S_sse

    # T0 = 456940.483
    # T1 = 29109.191
    # if n == 4:
    #     T0 = 228470.2
    #     T1 = 14554.6

    student = Label(text="Значення критеріїв Ст'юдента для кожного з параметрів:")
    student.place(relx=.5, rely=.8, anchor="c")

    coefficients = Label(text="T0 = %f, T1 = %f" % (T0, T1))
    coefficients.place(relx=.5, rely=.85, anchor="c")

    conclusion = Label(text="")
    conclusion.place(relx=.5, rely=.9, anchor="c")

    if T0 > T_theor:
        if T1 > T_theor:
            conclusion.config(text="Вплив a0 та a1 значущий")
        else:
            conclusion.config(text="Вплив a0 значущий, вплив a1 незначний")
    else:
        if T1 > T_theor:
            conclusion.config(text="Вплив a0 незначний, вплив a1 значущий")
        else:
            conclusion.config(text="Вплив a0 та a1 незначний")

    x = np.arange(min(y) - 1, max(y) + 1)
    z = a0 + a1 / x
    plt.scatter(y, sse, marker='o', color='red')
    plt.plot(x, z, color='blue')
    plt.grid()
    plt.xlabel("Обсяг виробництва")
    plt.ylabel("Собівартість")
    plt.show()


def start_data():
    dim_label.config(text="Кількість досліджуваних періодів:")

    global n
    global y
    global sse
    global enter_field

    n = int(dim_field.get())
    y = np.zeros([n])
    sse = np.zeros([n])

    global enter_field_label1
    global enter_field_label2
    enter_field_label1 = Label(text="Введіть обсяг виробництва:")
    enter_field_label1.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=5)

    enter_field_label2 = Label(text="Введіть собівартість одиниці продукції:")
    enter_field_label2.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=5)

    global rows
    global cols

    rows = []
    for i in range(n):
        cols = []
        for j in range(2):
            enter_field = Entry(relief=RIDGE, text='%d.%d' % (i, j))
            enter_field.grid(row=i+2, column=j, ipadx=10, ipady=6, padx=10, pady=2)
            cols.append(enter_field)
        rows.append(cols)

    submit.config(text="Розв`язок", command=solution)


def main():
    global root
    root = Tk()
    root.title("Прогнозування витрат")
    root.geometry("550x550+500+200")

    file_menu = Menu()
    file_menu.add_command(label="Рестарт", command=restart)
    file_menu.add_separator()
    file_menu.add_command(label="Вихід", command=exitWin)

    main_menu = Menu()
    main_menu.add_cascade(label="Меню", menu=file_menu)
    main_menu.add_cascade(label="Вихід", command=exitWin)

    root.config(menu=main_menu)

    global dim_label
    dim_label = Label(text="Оберіть кількість досліджуваних періодів:")
    dim_label.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)

    global dim_field
    dim_field = Spinbox(from_=1, to=100)
    dim_field.grid(row=0, column=1, ipadx=10, ipady=6, padx=10, pady=10)

    global equation
    equation = Label(text="")
    equation.place(relx=.5, rely=.75, anchor="c")

    global submit
    submit = Button(
                text="Далі",
                background="#555",
                foreground="#ccc",
                padx="20",
                pady="8",
                font="16",
                command=start_data
                )
    submit.place(relx=0.62, rely=0.95, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    exit = Button(
        text="Вихід",
        background="#555",
        foreground="#ccc",
        padx="20",
        pady="8",
        font="16",
        command=exitWin
    )
    exit.place(relx=0.85, rely=0.95, anchor="c", height=30, width=130, bordermode=OUTSIDE)

    root.mainloop()


main()
