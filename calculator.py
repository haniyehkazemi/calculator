# 90
from tkinter import *
import tkinter.messagebox
# ====================== settings ======================
root = Tk()
root.title('calculator')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

# ====================== variable ======================
num1 = StringVar()
num2 = StringVar()
res_num = StringVar()
# ====================== frames ========================
top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# ___________________________________________________________________________________________
# 92
# ====================== functions  ========================


def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror("Error", "something went wrong")
    elif msg == "division zero error":
        tkinter.messagebox.showerror("division Error", "can not divide by 0")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_num.set(value)

    except:
        errorMsg("error")


def minus():
    try:
        value = float(num1.get())-float(num2.get())
        res_num.set(value)

    except:
        errorMsg("error")


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_num.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg("division zero error")
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res_num.set(value)
        except:
            errorMsg("error")


# ___________________________________________________________________________________________

# 91
# ====================== buttons ========================

btn_plus = Button(top_third, text="+", highlightbackground=color,
                  width=10, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_minus = Button(top_third, text='-', width=10,
                   highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, width=10, text='x',
                 highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10,
                 highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)

# ====================== enties and labels =======================

first_num = Label(top_first, text='input number 1 :', bg=color)
first_num.pack(side=LEFT, padx=10, pady=10)

first_num_entry = Entry(
    top_first, highlightbackground=color, textvariable=num1)
first_num_entry.pack(side=LEFT, padx=10, pady=10)

second_num = Label(top_second, text='input number 2 :', bg=color)
second_num.pack(side=LEFT, padx=10, pady=10)

second_num_entry = Entry(
    top_second, highlightbackground=color, textvariable=num2)
second_num_entry.pack(side=LEFT, padx=10, pady=10)


res_value = Label(top_forth, text="result :", bg=color)
res_value.pack(side=LEFT, padx=10, pady=10)

res_num_entry = Entry(
    top_forth, highlightbackground=color, textvariable=res_num)
res_num_entry.pack(side=LEFT, padx=10, pady=10)

root.mainloop()