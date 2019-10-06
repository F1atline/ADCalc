#for 2.7 python
#calculate power of charger device for LFP and IGM
#SUSU

import numpy as np
import matplotlib.pyplot as plt

#Input voltage amplitude
ampletude = 15

#Active components
resist_in = 10000.0; resist_afte_pre_charger = 0.10; resist_in_schame = 20.0; add_res =2.0;

#Reactive components
capacity=0.01; inductiance=0.06;

#Time components
Period=0.01; Time_start=0.0; step=Period/1000;
Time_freq=Period*10

steps=int(Time_freq/step);

#Input voltage
def E(Period):
    n=int(Period/Period)
    if ((Period >= n*Period )and(Period <= n*Period + Period/2)):
        return ampletude
    else:
        return 0.0


time = np.arange(Time_start, Time_freq, step)

ul = []; il = []; uc = []; ic = []; y = [];

for i in range(0, steps, 1):
    y.append(E(time[i]))

def dIl_dt(Period):
    return float((1.0/inductiance)*(E(Period) - (resist_afte_pre_charger+resist_in_schame)*il[int(Period/step)]*resist_in/(resist_in+resist_afte_pre_charger+resist_in_schame)))

def dUc_dt(Period):
    return float((1.0/capacity)*((resist_in_schame*resist_in*il[int(Period/step)]/(resist_in+resist_afte_pre_charger+resist_in_schame) - uc[int(Period/step)])/add_res))

#Uc
def Uc(Period):
    return float((il[int(Period/step)] - ic[int(Period/step)])*resist_in_schame - ic[int(Period/step)]*add_res)
#Il
def Il(Period):
    return float(((E(Period)-ul[int(Period/step)])*(resist_in*(resist_afte_pre_charger+resist_in_schame) + resist_in)/(resist_in*resist_in*(resist_afte_pre_charger+resist_in_schame))) + ic[int(Period/step)])

#Start condition
ul.append(E(0)); il.append(0.0); uc.append(0.0); ic.append(0.0);

#Euler method
for i in range(1, steps, 1):
    il.append(il[i-1] + step*dIl_dt(time[i-1]))
    uc.append(uc[i-1] + step*dUc_dt(time[i-1]))
    ul.append(inductiance*dIl_dt(time[i]))
    ic.append(capacity*dUc_dt(time[i]))
print("hello world MFC!")
plt.figure("charts")
e = plt.subplot(311)
e.plot(time, y)
e.set_xlabel('time (s)')
e.set_ylabel('E(Period), (V)', color='b')
plt.grid(True)
print("Damage for u brain!")

UL = plt.subplot(312)
UL.plot(time, ul)
UL.set_xlabel('time (s)')
UL.set_ylabel('Ul(Period), (V)', color = 'b')

IL = UL.twinx()
IL.plot(time, il, 'r')
IL.set_ylabel('Il(Period), (A)', color = 'r')
plt.grid(True)

UC = plt.subplot(313)
UC.plot(time, uc)
UC.set_xlabel('time (s)')
UC.set_ylabel('Uc(Period), (V)', color = 'b')

IC = UC.twinx()
IC.plot(time, ic, color = 'r')
IC.set_ylabel('Ic(Period), (A)', color = 'r')
plt.grid(True)

plt.show()