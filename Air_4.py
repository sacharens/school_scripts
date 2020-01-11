import numpy as np
import matplotlib.pyplot as plt
import math
import os
from scipy.integrate import simps

folder_path = 'C:/Users/User/Documents/school/'

if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')


# -----------------------------------------------------------------------------------------------
def my_formula(dp, t):
    r = np.piecewise(dp, [(dp < 0.2) * (dp >= 0.1), (dp <= 1) * (dp >= 0.2), (dp > 1) * (dp < 2)],
                     [lambda dp: (-4 * dp + 0.9), lambda dp: 0.1, lambda dp: (0.4 * dp - 0.3)])
    a = np.exp((-1 * ((np.log(dp / 0.2)) ** 2)) / (2 * (np.log(1.5) ** 2)))
    b = 100 / (np.sqrt(2 * math.pi) * math.log(1.5))
    c = np.exp(-r * t)
    d = (0.1 / r) * (1 - np.exp(-r * t))
    return b * a * c + d  # a+b = n


# סעיף א-----------------------------------------------------------------------------------
list_t = []
dp = np.linspace(0.1, 2, num=150)
plt.figure()
"""
for t in range(0, 3):
    n = my_formula(dp, t)
    plt.plot(dp, n)
    list_t.append('t = ' + str(t))
"""
n = my_formula(dp, t=0)
plt.plot(dp, n, 'r-', linewidth=2, label='t=0')
n = my_formula(dp, t=1)
plt.plot(dp, n, 'b--', linewidth=2, label='t=1')
n = my_formula(dp, t=3)
plt.plot(dp, n, 'g:', linewidth=2, label='t=3')
plt.legend()
plt.title('n(Dp,t)')
plt.xlabel('Dp[um]')
plt.ylabel('n[1/cm^3]')
plt.tight_layout()
# plt.show()
plt.savefig(folder_path + 'n(Dp,t).jpg', dpi=300)

# סעיפ ב-----------------------------------------------------------------------------------
# חישוב לפי שיטת הטרפז
list_t = []
N_list = []
plt.figure()
for t in range(0, 3):
    n = my_formula(dp, t)
    n[149] = 0.00001
    N = simps(n)
    N_list.append(N)
    list_t.append('t' + str(t))

plt.plot(list_t, N_list, marker='o')
plt.title('N total number of particles')
plt.xlabel('time')
plt.ylabel('N total number of particles')
plt.tight_layout()
# plt.show()
plt.savefig(folder_path + 'N total number of particles.jpg', dpi=300)
