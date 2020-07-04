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
file_list = [file for file in all_files_in_folder if file.endswith('.counts')]
count = 0
for file_name in file_list:
    df = pd.read_csv(folder_path+file_name,sep='\t', header=None)
    df.rename(columns = {0: 'gene',1:file_name},inplace=True)
    if count == 0:
        merged_df = df
        count+=1
    else:
        merged_df = merged_df.merge(df, on=['gene'])

merged_df['sum'] = merged_df.sum(axis=1)
merged_df = merged_df.drop(merged_df[merged_df['sum'] == 0].index)
merged_df.drop(['sum'], axis=1, inplace=True)
for i in ['__no_feature','__ambiguous','__too_low_aQual','__not_aligned','__alignment_not_unique']:
    merged_df = merged_df.drop(merged_df[merged_df['gene'] == i].index)

# plotting
fig, ax = plt.subplots(figsize=(25,15))
sns.set(style="whitegrid")
plt.bar(merged_df['gene'],merged_df["all2.counts"],label="all2.counts")
plt.bar(merged_df['gene'],merged_df["all3.counts"],label="all3.counts")
ax.set_xlabel('gene')
plt.xticks(rotation=90)# Add an x-label to the axes.
ax.set_ylabel('counts')  # Add a y-label to the axes.
ax.legend()  # Add a legend.
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'bar.jpg')


#heat map
#dropping the big gene counts
#
#
merged_df = merged_df.drop(merged_df[merged_df['gene'] == 'ON00_RS19690'].index)
merged_df = merged_df.drop(merged_df[merged_df['gene'] == 'ON00_RS19675'].index)
#
#
heat_df = merged_df.set_index('gene')
ax = plt.subplots(figsize=(25,15))
ax = sns.heatmap(heat_df, cmap="YlGnBu")
plt.tight_layout()
#plt.show()
plt.savefig(folder_path + 'heat.jpg')
