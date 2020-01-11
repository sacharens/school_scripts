import numpy as np
import matplotlib.pyplot as plt
import math
import os


folder_path = 'C:/Users/User/Documents/school/'

if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')


# part A-----------------------------------------------------------------------------------------------
def my_formula(dp, t):
    a = np.exp((-1 * (np.log(np.sqrt(dp ** 2 - 2 * 0.01 * t) / 0.2))**2) / 2 * (np.log(0.01) ** 2))
    b = 100 / np.sqrt(2 * math.pi) * np.log(1.5)
    c = dp / np.sqrt(dp ** 2 - (2 * 0.01 * t))

    return c*b*a


# part B-----------------------------------------------------------------------------------------------
def my_formula_B(dp, t):
    a = np.exp((-1 * (np.log(np.sqrt(dp - 0.03*t) / 0.2))**2) / 2*(np.log(0.01)**2))
    b = 100 / np.sqrt(2 * math.pi) * math.log(1.5)

    return b*a


plt.figure()
dp = np.linspace(0, 1)
for t in range(0, 10, 2):
    n = my_formula_B(dp, t)  # <- note now we're calling the function 'formula' with t
    plt.plot(dp, n)
plt.title('graph B')
plt.xlabel('Dp[um]')
plt.ylabel('n[1/cm^3]')
plt.tight_layout()
plt.show()
# plt.savefig(folder_path + 'part_b.jpg', dpi=300)
