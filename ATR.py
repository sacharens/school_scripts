import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

plt.style.use('fivethirtyeight')

folder_path = 'C:/Users/User/Documents/school/project/python_data/'  # must end with a /
if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')

all_files_in_folder = os.listdir(folder_path)
file_list = [file for file in all_files_in_folder if file.endswith('.dpt')]
fig, ax = plt.subplots(figsize=(25,15))

for file_name in file_list:
    df = pd.read_csv(folder_path+file_name,sep='\t')
    df = df.drop(df[df['wavenumber'] > 2000].index)
    ax.plot(df['wavenumber'],df['absorbance'],label=file_name[:-4])

ax.set_xlabel('Wave number (cm^-1)')  # Add an x-label to the axes.
ax.set_ylabel('Absorbance')  # Add a y-label to the axes.
ax.set_title("ATR-FTIR")  # Add a title to the axes.
ax.legend()  # Add a legend.
# plt.show()
plt.savefig(folder_path + 'ATR.jpg')
