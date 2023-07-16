import subprocess
from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Добре дошли в моят калкулатор")
title_label = Label(root, text="Добре дошли в моя дигитален калкулатор!", font=("Arial", 24))
title_label.pack(pady=20)

description_label = Label(root, text="Моля, изберете опцията, която желаете да използвате:", font=("Arial", 16))
description_label.pack(pady=10)


def open_age_calculator():
    subprocess.call(["python", "u91.py"])

def open_credit_calculator():
    subprocess.call(["python", "u92.py"])

def open_simple_calculator():
    subprocess.call(["python", "u93.py"])



# Label(text="Welcome to my calculator app!", font="arial 20 bold").pack(pady=50)

Button(text="Възрастов калкулатор", font="arial 15", bg="white" ,fg="black", bd=10, command=open_age_calculator).pack(pady=20)
Button(text="Калкулатор за кредити", font="arial 15", bg="white", fg="black", bd=10, command=open_credit_calculator).pack(pady=20)
Button(text="Simple Калкулатор", font="arial 15", bg="white", fg="black", bd=10, command=open_simple_calculator).pack(pady=20)

Button(text="Exit", font="arial 15", bg="white", fg="black", bd=10, command=root.destroy).pack(pady=20)

root.mainloop()

