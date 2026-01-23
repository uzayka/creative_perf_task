from tkinter import *
from parolchiki import *
from interface import *

def generate():
    enrt.delete(0, END)
    num_1 =  int(spnlc.get())
    num_2 = int(spnnum.get())
    num_3 = int(spnup.get())
    num_4 = int(spnsn.get())
    state1 = lowercase.get()
    state2 = numbers.get()
    state3 = uppercase.get()
    state4 = signs.get()
    password = generate_password(state1, state2, state3, state4, num_1, num_2, num_3, num_4)
    enrt.insert(0, password)

bt1.config(command=generate)

window.mainloop()
