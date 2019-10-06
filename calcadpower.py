#project for python 3.7

import matplotlib.pyplot as pyplot
import numpy as np
import math as math

figure = pyplot.figure()
axes = pyplot.axes()
x = np.linspace(0, 10, 1000)
axes.plot(x, x*x)


#comstants

pi = 3.1416

#params of drive

pare_of_pole=3
Voltage_of_phase=220           
freqency=50               
Power_nominal=22000       
Velocity_nominal=935            
Current_of_stator=51             
efficient=0.83       
COS_current_of_stator=0.79  
Torque_critical=760           
Start_torque=706          
Current_of_start=275          

Resistanse_of_stator_coil=0.232
Res=0.325      
x1=0.285         
x2p=0.2844    
Current_of_magnetic_field=26.3        

Sourse_of_voltage=1
Source_of_current=0              
Dynamic_break=0              

if Source_of_voltage == 1:
    Voltage_of_source=220
    freqency_of_source=50


if Source_of_current == 1:
   current_of_source=55           
   freqency_of_source=15              


if Dynamic_break == 1 and Source_of_current == 1:
   freqency_of_source=0                  
   Current_of_break=100       
   koeff_sleep=0.816        
   current_of_source=koeff_sleep*Current_of_break 
                     
   
Resistanse_of_stator_coil=0
X1D=0
        
hayatov_evgeny=1  
                    
      
juravlevam=1         
     
   
pi=3.1416
won=2*pi*freqency/pare_of_pole 
wn=Velocity_nominal/9.55      
Mn=Power_nominal/wn       
sn=(won-wn)/won 
Torque_criticalo=Torque_critical/Mn       
Start_torqueo=Start_torque/Mn      
Current_of_starto=Current_of_start/Current_of_stator    
a1=Resistanse_of_stator_coil/Res
sk=sn*(Torque_criticalo + sqrt((Torque_critical^2-1)+2*a1*sn*(Torque_criticalo-1))/(1-2*sn*a1*(Torque_criticalo-1)))
Memn=2*Torque_critical*(1+a1*sk)/(sn/sk+sk/sn+2*a1*sk) 
dMxn=Memn-Mn         
r2v=Start_torque*won/(3*Current_of_start^2)   
sinfCurrent_of_stator = sqrt(1 - COS_current_of_stator^2)
if Current_of_magnetic_field == 0:
    Current_of_magnetic_field = Current_of_stator*(sinfCurrent_of_stator - COS_current_of_stator*sn/sk)
                      
xmn=Voltage_of_phase/Current_of_magnetic_field-x1
E1n=Current_of_magnetic_field*xmn
Resistanse_of_stator_coil= Resistanse_of_stator_coil + Resistanse_of_stator_coild
x1=x1+X1D
ks=0
Im=Current_of_magnetic_field
won=abs(won)  
wna=-10            
wko=110            
dw=0.5            
M1=Torque_critical  
w1=won*(1-sk)     
M2=Start_torque
w2=0
M3=Current_of_start
w3=0

for w=wna:dw:wko
    if Dynamic_break==1 and a==1:
       s=-(w/won)
       wo=won
    else:
       a=(freqency_of_source+ks)/freqency
       wo=a*won
       s=(wo-w)/wo
	   
print("Hello my friend")  

if abs(s)<0.001:
    s=0.001
if juravlevam==0:
   xm=xmn
else:
  imo=Im/Current_of_magnetic_field

if imo<0.37:
    em=1.35*imo
if imo>0.37:
    em=0.5+1.09*(imo-0.37)
if imo>0.6:
    em=0.75+0.625*(imo-0.6)
if imo>1:
    em=1+0.5*(imo-1)
if imo>1.2:
    em=1.1+0.167*(imo-1.2)
if imo>1.8:
    em=1.2+0.1*(imo-1.8)
if em>1.3:
    em=1.3
xm=em*E1n/(imo*Current_of_magnetic_field)

print("Hello world!")    

r2s=(r2v)/s
if (r2v-Res)>0:
    r2s=(Res+(r2v-Res))/s
z2p=r2s+j*x2p*a                          
zm=j*xm*a
zmr=zm*z2p/(zm+z2p)
  
z1=Resistanse_of_stator_coil+j*x1*a
zc=z1+zmr
if Dynamic_break==1:
    i2p=current_of_source*zm/(z2p+zm)
    I2p=abs(i2p)
    im=current_of_source*z2p/(z2p+zm)
    Im=abs(im)
    I1=abs(current_of_source)
    I1a=real(current_of_source)
else:
      if Source_of_current==1:
          i1=current_of_source
          u1=i1*zc
      if Sourse_of_voltage==1:
          u1=Voltage_of_source+ks*Voltage_of_phase/freqency
          i1=u1/zc
      I1=abs(i1)                                                            
      I1a=real(i1)
      e=i1*zmr
      im=e/zm 
      Im=abs(im)
      i2p=-e/z2p 
      I2p=abs(i2p)                             
     
dfoi=freqency*I1a/(Current_of_stator*COS_current_of_stator)        
if w > wo and dfoi == 0:
   ks=hayatov_evgeny*sn*dfoi                           

   M=3*I2p^2*r2s/wo            
   if freqency_of_source==0:
    cosfi=0
   else:
   cosfi=abs(cos(angle(zc)))
   
   
dMx=abs(dMxn)*sign(w)                   
Pv=(M-dMx)*w                      
dP2=3*I2p*I2p*Res             
Pem=M*w+dP2                 
dP1=3*I1*I1*Resistanse_of_stator_coil               
Pc=3*abs(u1)*I1a             
  
if Dynamic_break==1:
    Pc=0
    kpd=0
else:
    kpd=Pv/Pc
if (Pv < 0)and(Pc < 0):
    kpd=Pc/Pv
if M==0 or w==0:
    kpd=0
if kpd <=0:
    kpd=0
if kpd >1:
    kpd=0

axes.plot(M/Mn,w/abs(won))
axes.plot(I1/Current_of_stator,w/abs(won))
axes.plot(I2p/Current_of_stator,w/abs(won))
axes.plot(Im/Current_of_stator,w/abs(won))
axes.plot(kpd,w/abs(won))
axes.plot(cosfi,w/abs(won))
axes.plot(M1/Mn,w1/abs(won))
axes.plot(M2/Mn,w2/abs(won))
axes.plot(M3/Current_of_stator,w3/abs(won))

pyplot.show()

print("Good bye!")
