# 90
from tkinter import *
# ====================== settings ======================
root = Tk()
root.title('calculator')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

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

# 91
# ====================== buttons ========================

btn_plus = Button(top_third, text="+", highlightbackground=color, width=10)
btn_plus.pack(side=LEFT, padx=10, pady=10)

btn_mines = Button(top_third, text='-', width=10, highlightbackground=color)
btn_mines.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, width=10, text='x', highlightbackground=color)
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, text='/', width=10, highlightbackground=color)
btn_div.pack(side=LEFT, padx=10, pady=10)


# ___________________________________________________________________________________________

root.mainloop()