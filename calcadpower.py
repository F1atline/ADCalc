import sys
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Frame, Entry, Label, Button
from math import sqrt, cos
from numpy import angle, sign

root = Tk()

root.title("hello")
root.geometry('500x400+300+200')

#variables

#catalog data

tip = '4MTKF(H)200L6'
pp = 3
u1n = 220
f1n = 50
Pn = 22000
nn = 935
I1n = 51
kpdn = 0.83
cosfi1n = 0.79
Mk = 760
Mp = 706
I1p = 275

#obm
r1 = 0.232
r2p = 0.325
x1 = 0.285
x2p = 0.2844
Imn = 26.3

iu = 1
it = 0
dt = 0

#params of source

if iu == 1:
    u1s = 220
    f1 = 50

if it == 1:
    i1s = 55
    f1 = 15

if dt == 1:
    #it == 1
    f1 = 0
    Ipost = 100
    kc = 0.816
    i1s = kc * Ipost

R1d = 0
X1d = 0
kot = 0
krn = 1

#####################

pi = 3.1416
won = 2 * pi * f1n / pp
wn = nn / 9.55
Mn = Pn / wn
sn = (won - wn) / won
Mko = Mk / Mn
Mpo = Mp / Mn
I1po = I1p / I1n
a1 = r1 / r2p
sk = sn * (Mko + sqrt((Mko ** 2 - 1) + 2 * a1 * sn * (Mko - 1)) / (1 - 2 * sn * a1 * (Mko - 1)))
Memn = 2 * Mk * (1 + a1 * sk) / (sn / sk + sk / sn + 2 * a1 * sk)
dMxn = Memn - Mn
r2v = Mp * won / (3 * (I1p ** 2))
sinfi1n = sqrt(1 - cosfi1n ** 2)
if Imn == 0:
    Imn = I1n * (sinfi1n - cosfi1n * sn / sk)

xmn = u1n / Imn - x1
E1n = Imn*xmn
r1 = r1 + R1d
x1 = x1 + X1d
ks = 0
Im = Imn
won = abs(won)
wna = -10
wko = 110
dw = 0.5

M1 = Mk
w1 = won * (1 - sk)
M2 = Mp
w2 = 0
M3 = I1p
w3 = 0

w = wna
while w > wko:
    if dt == 1:
        a = 1
        s = -w / won
        wo = won
    else:
        f1 = 50
        a = (f1 + ks) / f1n
        wo = a * won
        s = (wo - w) / wo

    if abs(s) < 0.001:
        s = 0.001
    if krn == 0:
        xm = xmn
    else:
        imo = Im / Imn

    if imo < 0.37:
        em = 1.35 * imo
    if imo > 0.37:
        em = 0.5+1.09 * (imo-0.37)
    if imo > 0.6:
        em = 0.75+0.625 * (imo-0.6)
    if imo > 1:
        em = 1+0.5 * (imo-1)
    if imo > 1.2:
        em = 1.1+0.167 * (imo-1.2)
    if imo > 1.8:
        em = 1.2+0.1 * (imo-1.8)
    if em > 1.3:
        em = 1.3

    xm = em * E1n / (imo * Imn)
    w = w - dw

r2s = (r2v) / s
# if (r2v - r2p) > 0 r2s=(r2p+(r2v-r2p)) / s
z2p = r2s + j * x2p * a
zm = j * xm * a
zmr = zm * z2p / (zm + z2p)

z1 = r1 + j * x1 * a
zc = z1 + zmr
if dt == 1:
    i2p = i1s * zm / (z2p + zm)
    I2p = abs(i2p)
    im = i1s * z2p / (z2p + zm)
    Im = abs(im)
    I1 = abs(i1s)
    I1a = i1s.real
else:
    if it == 1:
        i1 = i1s
        u1 = i1 * zc
    if iu == 1:
        u1 = u1s + ks * u1n / f1n
        i1 = u1 / zc
        I1 = abs(i1)
        I1a = i1.real
        e = i1 * zmr
        im = e / zm
        Im = abs(im)
        i2p = -e / z2p
        I2p = abs(i2p)

dfoi = f1n * I1a / (I1n * cosfi1n)
if w > wo:
    dfoi = 0
ks = kot * sn * dfoi

M = 3 * I2p ** 2 * r2s / wo
if f1 == 0:
    cosfi = 0
else:
    cosfi = abs(cos(angle(zc)))

dMx = abs(dMxn) * sign(w)
Pv = (M - dMx) * w
dP2 = 3 * I2p * I2p * r2p
Pem = M * w + dP2
dP1 = 3 * I1 * I1 * r1
Pc = 3 * abs(u1) * I1a

if dt == 1:
    Pc = 0
    kpd = 0
else:
    kpd = Pv / Pc
if Pv < 0 and Pc < 0:
    kpd = Pc / Pv
if M == 0 or w == 0:
    kpd = 0
if kpd <= 0:
    kpd = 0
if kpd > 1:
    kpd = 0

# create
frame1 = Frame(root, bd=1)
frame2 = Frame(root, bd=1)

def button_clicked():
    print("Clicked")
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

button_ploting = Button(frame1, text='Plot', width=10)
button_ploting.config(command=button_clicked)

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
button_ploting.pack()
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
