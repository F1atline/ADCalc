import sys
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Frame, Entry, Label


x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


root = Tk()

root.title("hello")
root.geometry('500x400+300+200')

# create
frame1 = Frame(root, bd=1)
frame2 = Frame(root, bd=1)

e_pp = Entry(frame1, width=10)
l_pp = Label(frame1, text='pair of pole')

e_u1n = Entry(frame1, width=10)
l_u1n = Label(frame1, text='voltage of phase')

e_f1n = Entry(frame1, width=10)
l_f1n = Label(frame1, text='freqency')

e_Pn = Entry(frame1, width=10)
l_Pn = Label(frame1, text='power')

e_nn = Entry(frame1, width=10)
l_nn = Label(frame1, text='nominal velocity, rpm')

e_I1n = Entry(frame1, width=10)
l_I1n = Label(frame1, text='nominal current of stator')

e_effnom = Entry(frame1, width=10)
l_effnom = Label(frame1, text='efficiency')

e_cosfi1n = Entry(frame1, width=10)
l_cosfi1n = Label(frame1, text='cos')

e_Mk = Entry(frame1, width=10)
l_Mk = Label(frame1, text='torque of down')

e_Mp = Entry(frame1, width=10)
l_Mp = Label(frame1, text='torque of start')

e_I1p = Entry(frame1, width=10)
l_I1p = Label(frame1, text='current of start')

frame1.pack()
l_pp.pack()
e_pp.pack()
e_u1n.pack()
l_u1n.pack()
e_f1n.pack()
l_f1n.pack()
e_Pn.pack()
l_Pn.pack()
e_nn.pack()
l_nn.pack()
e_I1n.pack()
l_I1n.pack()
e_effnom.pack()
l_effnom.pack()
e_cosfi1n.pack()
l_cosfi1n.pack()
e_Mk.pack()
l_Mk.pack()
e_Mp.pack()
l_Mp.pack()
e_I1p.pack()
l_I1p.pack()

root.mainloop()
sys.exit("Good bye!")
