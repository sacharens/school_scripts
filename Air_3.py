import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import os

folder_path = 'C:/Users/User/Documents/school/'

if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')


# function that returns dy/dt part A ----------------------------------------
def model1(y, t, Dp):
    tau = float(Dp**2)/float(18*math.pi*2*10**(-4))
    dydt = -y*tau + 0.2*tau
    return dydt


# function that returns dy/dt part B ---------------------------------------
def model2(y, t, Dp, a):
    u = 0.4*math.exp(-t/a)
    tau = float(Dp**2)/float(18*math.pi*2*10**(-4))
    dydt = -y*tau + u*tau
    return dydt


# function that returns dy/dt part C ---------------------------------------
def model3(y, t):
    Dp0 = 0.02
    b = 2
    Dp = Dp0 * math.exp(-t / b)
    tau = float(Dp**2)/float(18*math.pi*2*10**(-4))
    dydt = -y*tau + 0.2*tau
    return dydt


# initial condition
y0 = 0

# time points
t = np.linspace(0, 4)

# solve ODE part a-----------------------------------------------
Dp = 0.1
y1 = odeint(model1,y0,t,args=(Dp,))
Dp = 0.2
y2 = odeint(model1,y0,t,args=(Dp,))
Dp = 0.5
y3 = odeint(model1,y0,t,args=(Dp,))


# plot results part A--------------------------------------------
plt.figure(figsize=(6,5))
plt.plot(t,y1,'r-',linewidth=2,label='Dp=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='Dp=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='Dp=0.5')
plt.xlabel('time[sec]')
plt.ylabel('Vp(t)[cm/sec]')
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'part_a.jpg', dpi=300)

# plot results part B first a ---------------------------------------------
a = 1
Dp = 0.1
y1 = odeint(model2,y0,t,args=(Dp,a))
Dp = 0.2
y2 = odeint(model2,y0,t,args=(Dp,a))
Dp = 0.5
y3 = odeint(model2,y0,t,args=(Dp,a))
yf = np.exp(-t/a)
plt.figure(figsize=(6,5))
plt.plot(t,yf,'y-',linewidth=2,label='fluid')
plt.plot(t,y1,'r-',linewidth=2,label='Dp=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='Dp=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='Dp=0.5')
plt.xlabel('time[sec]')
plt.ylabel('Vp(t)[cm/sec]')
plt.legend(title="a = 1")
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'part_b.jpg', dpi=300)

# plot results part B second a ---------------------------------------------
a = 3
Dp = 0.1
y1 = odeint(model2,y0,t,args=(Dp,a))
Dp = 0.2
y2 = odeint(model2,y0,t,args=(Dp,a))
Dp = 0.5
y3 = odeint(model2,y0,t,args=(Dp,a))
yf = np.exp(-t/a)
plt.figure(figsize=(6,5))
plt.plot(t,yf,'y-',linewidth=2,label='fluid')
plt.plot(t,y1,'r-',linewidth=2,label='Dp=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='Dp=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='Dp=0.5')
plt.xlabel('time[sec]')
plt.ylabel('Vp(t)[cm/sec]')
plt.legend(title="a = 3")
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'part_b_second.jpg', dpi=300)
# part C --------------------------------------------------------------

y = odeint(model3,y0,t)
plt.figure(figsize=(6,5))
plt.plot(t,y,'r-',linewidth=2)
plt.xlabel('time[sec]')
plt.ylabel('Vp(t)[cm/sec]')
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'part_c.jpg', dpi=300)
