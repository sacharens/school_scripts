import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

plt.style.use('fivethirtyeight')

folder_path = 'C:/Users/User/Documents/school/project/results/HTSeq2/'  # must end with a /
if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')

all_files_in_folder = os.listdir(folder_path)
file_list = [file for file in all_files_in_folder if file.endswith('.counts')]
count = 0
for file_name in file_list:
    df = pd.read_csv(folder_path + file_name, sep='\t', header=None)
    df.rename(columns={0: 'gene', 1: file_name}, inplace=True)
    if count == 0:
        merged_df = df
        count += 1
    else:
        merged_df = merged_df.merge(df, on=['gene'])

merged_df['sum'] = merged_df.sum(axis=1)

# frequency df
fre_df = merged_df.copy()
for col in fre_df.columns:
    if col != 'gene':
        fre_df[col] = fre_df[col] / fre_df['sum']
for i in ['__no_feature', '__ambiguous', '__too_low_aQual', '__not_aligned', '__alignment_not_unique']:
    fre_df = fre_df.drop(fre_df[fre_df['gene'] == i].index)
fre_df = fre_df.drop(fre_df[fre_df['sum'] == 0].index)
fre_df.drop(['sum'], axis=1, inplace=True)

merged_df = merged_df.drop(merged_df[merged_df['sum'] == 0].index)
merged_df.drop(['sum'], axis=1, inplace=True)
for i in ['__no_feature', '__ambiguous', '__too_low_aQual', '__not_aligned', '__alignment_not_unique']:
    merged_df = merged_df.drop(merged_df[merged_df['gene'] == i].index)
merged_df.replace(0, 1, inplace=True)

merged_df.to_excel(folder_path + 'data.xlsx')

heat_df = merged_df.set_index('gene')
for idx in heat_df.index:
    if idx not in ['ON00_RS01980',
                   'ON00_RS04305',
                   'ON00_RS06850',
                   'ON00_RS08360',
                   'ON00_RS09645',
                   'ON00_RS09835',
                   'ON00_RS11515',
                   'ON00_RS16330',
                   'ON00_RS16580',
                   'ON00_RS19665',
                   'ON00_RS19680',
                   'ON00_RS19685']:
        heat_df.drop(index=idx, inplace=True)
rna_df = merged_df.copy()
for idx in list(rna_df['gene']):
    if idx not in ['ON00_RS19670',
                   'ON00_RS19675',
                   'ON00_RS19690']:
        rna_df.drop(merged_df.loc[merged_df['gene'] == idx].index, inplace=True)


merged_df['exp 1'] = np.log2(merged_df['all2.1.counts'] / merged_df['all1.1no.counts'])
merged_df['exp 2'] = np.log2(merged_df['all4.1.counts'] / merged_df['all3.1no.counts'])
merged_df['exp 3'] = np.log2(merged_df['all6.1.counts'] / merged_df['all5.1no.counts'])
merged_df['exp 4'] = np.log2(merged_df['all8.1.counts'] / merged_df['all7.1no.counts'])
for col in list(merged_df):
    if col not in ['exp 1', 'exp 2', 'exp 3','exp 4', 'gene']:
        merged_df.drop([col], axis=1, inplace=True)

for idx in list(merged_df['gene']):
    if idx not in [
        'ON00_RS04305',
        'ON00_RS06850',
        'ON00_RS08360',
        'ON00_RS09645',
        'ON00_RS09835',
        'ON00_RS11515',
        'ON00_RS16330',
        'ON00_RS16580',
        'ON00_RS19665',
        'ON00_RS19680']:
        merged_df.drop(merged_df.loc[merged_df['gene'] == idx].index, inplace=True)

dict_change = {'all2.1.counts': 'exp 1 ',
               'all1.1no.counts': 'exp 1 no',
               'all4.1.counts': 'exp 2',
               'all3.1no.counts': 'exp 2 no',
               'all6.1.counts': 'exp 3',
               'all5.1no.counts': 'exp 3 no',
               'all8.1.counts': 'exp 4',
               'all7.1no.counts': 'exp 4 no'}

heat_df.rename(columns=dict_change, inplace=True)

dict_change_rna = {'all2.1.counts': 'exp 1 ',
               'all1.1no.counts': 'exp 1 no',
               'all4.1.counts': 'exp 2',
               'all3.1no.counts': 'exp 2 no',
               'all6.1.counts': 'exp 3',
               'all5.1no.counts': 'exp 3 no',
               'gene':'gene',
               'all8.1.counts': 'exp 4',
               'all7.1no.counts': 'exp 4 no'}


rna_df.rename(columns=dict_change_rna, inplace=True)

# change the gene to prodoct
gene_to_product = {'ON00_RS00870': "tRNA-Glu", 'ON00_RS01005': "tRNA-Asp",
                   'ON00_RS01010': "tRNA-Asp", 'ON00_RS01495': "tRNA-Ala",
                   'ON00_RS01740': "tRNA-Ser", 'ON00_RS01835': "tRNA-Arg",
                   'ON00_RS01980': "tRNA-Asn", 'ON00_RS19970': "RNase P RNA component class A",
                   'ON00_RS20045': "signal recognition particle sRNA small type",
                   'ON00_RS02815': "tRNA-Met", 'ON00_RS03455': "tRNA-His",
                   'ON00_RS03525': "tRNA-Val", 'ON00_RS03585': "tRNA-Leu",
                   'ON00_RS04060': "tRNA-Lys", 'ON00_RS04305': "tRNA-Cys",
                   'ON00_RS04440': "tRNA-Thr", 'ON00_RS06100': "tRNA-Trp",
                   'ON00_RS06390': "tRNA-Val", 'ON00_RS06595': "tRNA-Pro",
                   'ON00_RS06820': "tRNA-Gly", 'ON00_RS06850': "tRNA-Tyr",
                   'ON00_RS07435': "tRNA-Thr", 'ON00_RS07555': "tRNA-Arg",
                   'ON00_RS20140': "transfer-messenger RNA", 'ON00_RS08360': "tRNA-Ser",
                   'ON00_RS09645': "tRNA-Thr", 'ON00_RS09835': "tRNA-Gln",
                   'ON00_RS11370': "tRNA-Leu", 'ON00_RS11515': "tRNA-Gly",
                   'ON00_RS12405': "tRNA-Lys", 'ON00_RS12565': "tRNA-Val",
                   'ON00_RS13405': "tRNA-Leu", 'ON00_RS14015': "tRNA-Ser",
                   'ON00_RS15240': "tRNA-Phe", 'ON00_RS16055': "tRNA-Glu",
                   'ON00_RS16330': "tRNA-Pro", 'ON00_RS16580': "tRNA-Leu",
                   'ON00_RS16755': "tRNA-Ser", 'ON00_RS17010': "tRNA-Arg",
                   'ON00_RS17290': "tRNA-Ala", 'ON00_RS17970': "tRNA-Gly",
                   'ON00_RS18130': "tRNA-Gln", 'ON00_RS18215': "tRNA-Arg",
                   'ON00_RS18480': "tRNA-Ile", 'ON00_RS18485': "tRNA-Pro",
                   'ON00_RS19665': "tRNA-Met", 'ON00_RS19670': "5S ribosomal RNA",
                   'ON00_RS19675': "23S ribosomal RNA", 'ON00_RS19680': "tRNA-Ala",
                   'ON00_RS19685': "tRNA-Ile", 'ON00_RS19690': "16S ribosomal RNA"}
merged_df.replace({"gene": gene_to_product}, inplace=True)

rna_df.replace({'gene': {'ON00_RS19670':  "5S ribosomal RNA",'ON00_RS19675':  "23S ribosomal RNA",'ON00_RS19690':  "16S ribosomal RNA"}},inplace=True)

for col in list(merged_df):
    if col not in ['exp 3', 'exp 2', 'exp 1','exp 4', 'gene']:
        merged_df.drop([col], axis=1, inplace=True)

merged_df.to_excel(folder_path + 'log exp.xlsx')

#
fig, ax = plt.subplots(figsize=(25, 15))

# ax = sns.clustermap(heat_df, row_cluster=False, cmap="YlGnBu")
ax = sns.clustermap(heat_df, row_cluster=False, cmap="YlGnBu",
                    z_score=0)  # 0 means z score is calculated on a row basis and 1 on column basis.
plt.xticks(rotation=90)
# plt.show()
plt.savefig(folder_path + 'heat.jpg', dpi=150, bbox_inches='tight')

merged_df_transposed = merged_df.set_index('gene')
merged_df_transposed = merged_df_transposed.stack()
merged_df_transposed = merged_df_transposed.to_frame()

merged_df_transposed.reset_index(inplace=True)
merged_df_transposed.rename({"level_1": 'experiment'},axis=1,inplace=True)

# merged_df_transposed = merged_df_transposed.unstack('gene')

# merged_df_transposed.reset_index(inplace=True)
plt.figure(figsize=(12, 10))
sns.barplot(x="gene", y=0, hue="experiment", data=merged_df_transposed)
plt.xticks(rotation=45)
plt.ylabel('log2(modified/not modified)')

# plt.show()
plt.savefig(folder_path + 'bar_plot_log2.jpg', dpi=150, bbox_inches='tight')

rna_df = rna_df.set_index('gene')
rna_df = rna_df.stack()
rna_df = rna_df.to_frame()
rna_df[0]= rna_df[0].apply(np.log10)
rna_df.reset_index(inplace=True)
rna_df.rename({"level_1": 'experiment'},axis=1,inplace=True)


plt.figure(figsize=(12, 10))
sns.barplot(x="gene", y=0, hue="experiment", data=rna_df,palette=sns.color_palette("Paired"))
plt.xticks(rotation=45)
plt.ylabel('log10(counts)')
sns.cubehelix_palette(8, start=.5, rot=-.75)
# plt.show()
plt.savefig(folder_path + 'bar_plot_rna.jpg', dpi=150, bbox_inches='tight')
