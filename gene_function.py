import re
import matplotlib.pyplot as plt
import os
from scipy.stats import chisquare

plt.style.use('fivethirtyeight')

folder_path = 'C:/Users/User/Documents/school/project/results/'  # must end with a /
if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')

dict_of_gene_product = {}
gene_list = ['ON00_RS00870', 'ON00_RS01005', 'ON00_RS01010', 'ON00_RS01495', 'ON00_RS01740', 'ON00_RS01835', 'ON00_RS01980', 'ON00_RS02815', 'ON00_RS03455', 'ON00_RS03525', 'ON00_RS03585', 'ON00_RS04060', 'ON00_RS04305', 'ON00_RS04440', 'ON00_RS06100', 'ON00_RS06390', 'ON00_RS06595', 'ON00_RS06820', 'ON00_RS06850', 'ON00_RS07435', 'ON00_RS07555', 'ON00_RS08360', 'ON00_RS09645', 'ON00_RS09835', 'ON00_RS11370', 'ON00_RS11515', 'ON00_RS12405', 'ON00_RS12565', 'ON00_RS13405', 'ON00_RS14015', 'ON00_RS15240', 'ON00_RS16055', 'ON00_RS16330', 'ON00_RS16580', 'ON00_RS16755', 'ON00_RS17010', 'ON00_RS17290', 'ON00_RS17970', 'ON00_RS18130', 'ON00_RS18215', 'ON00_RS18480', 'ON00_RS18485', 'ON00_RS19665', 'ON00_RS19670', 'ON00_RS19675', 'ON00_RS19680', 'ON00_RS19685', 'ON00_RS19690', 'ON00_RS19970', 'ON00_RS20045', 'ON00_RS20140']

with open(folder_path+'GCF_000241465.1_ASM24146v1_genomic.gtf') as file:
    for line in file:
        for gene in gene_list:
            if line.find(gene) != -1 and line.find('product') != -1:
                new_line = line.split(';')
                for word in new_line:
                    if word.find('product') != -1:
                        dict_of_gene_product[gene]= word


print(dict_of_gene_product)


