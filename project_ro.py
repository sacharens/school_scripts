"""
This script gets the xls files from my ply and plots them into a good looking graph
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

plt.style.use('fivethirtyeight')

folder_path = 'C:/Users/User/Documents/school/project/'  # must end with a /
if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')

xls = pd.ExcelFile(folder_path + 'excel_16_03.xlsx')
df1 = pd.read_excel(xls, 'RO_Shafdan_1')
df2 = pd.read_excel(xls, 'RO_Shafdan_2')

# clean df1
head_list = list(df1)
for col in head_list:
    if col not in ['Time', 'Pressure  - Bar', 'Flow rate - gr/l']:
        df1.drop([col], axis=1, inplace=True)
df1['sys'] = df1['Time'].apply(lambda x: 'sys_1')
df1.rename(columns={"Pressure  - Bar": "Pressure [bar]", "Flow rate - gr/l": "Flow rate [ml/hr]"}, inplace=True)
df1['Time'] = df1['Time'].values.astype(float)


# clean df2
head_list = list(df2)
for col in head_list:
    if col not in ['Time', 'Pressure - Bar', 'Flow rate - gr/l']:
        df2.drop([col], axis=1, inplace=True)
df2['sys'] = df2['Time'].apply(lambda x: 'sys_2')
df2.rename(columns={"Pressure - Bar": "Pressure [bar]", "Flow rate - gr/l": "Flow rate [ml/hr]"}, inplace=True)
df2['Time'] = df2['Time'].values.astype(float)


# Plot the lines
fig, ax1 = plt.subplots(figsize=(15,8))

plt.title('sys_1 vs sys_2',fontsize=20)
ax1.set_xlabel('time', fontsize=16)
ax1.set_ylabel("Pressure [bar]",fontsize=16)
ax1.plot(df1['Time'], df1["Pressure [bar]"], c='brown',label= 'Pressure sys1')
ax1.plot(df2['Time'], df2["Pressure [bar]"], color='red',label= 'Pressure sys2')

ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


ax2.set_ylabel('Flow rate [ml/hr]',fontsize=16)  # we already handled the x-label with ax1
ax2.plot(df1['Time'], df1['Flow rate [ml/hr]'], color='teal',label= 'Flow sys1')
ax2.plot(df2['Time'], df2['Flow rate [ml/hr]'], color='blue',label= 'Flow sys2')

ax2.tick_params(axis='y')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='center left', bbox_to_anchor=(1.075, 0.5))

ax1.grid()

fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
plt.savefig(folder_path + 'sys_1 vs sys_2.jpg')

# ploy every system by itself--------------------------------------------------------------
pieces = {'sys_1': df1, 'sys_2': df2}

df_piece = pd.concat(pieces, sort=False)
df_piece['Time'] = df_piece['Time'].values.astype(float)

plt.subplots(figsize=(15,8))
sns.lineplot(x="Time", y="Flow rate [ml/hr]",
             hue="sys",
             data=df_piece)
plt.title('Flow rate',fontsize=20)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(folder_path + 'Flow rate.jpg')

plt.subplots(figsize=(15,8))
plt.style.use('ggplot')
sns.lineplot(x="Time", y="Pressure [bar]",
             hue="sys",
             data=df_piece)
plt.title('Pressure',fontsize=20)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(folder_path + 'Pressure.jpg')

