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

root.mainloop()