import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import re
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

"""
this script will take the eliza output file and mach it with excel file that maps the experiment,
then it will find the mean of all results and plot them in a graph the measures the intensity vs the samples
"""


def change_to_int(num):
    return int(num)


def sub_diluent(num, diluent):
    return float(num) - diluent


def type_of_result(str_index):
    if str_index.startswith('IgG'):
        return 'IgG'
    if str_index == 'diluent':
        return 'diluent'
    else:
        return re.findall(r'\w+\s\d', str_index)[0]


def find_con_from_eq(num, slope, intercept):
    return (num - intercept) / slope


def extract_dilutions(str_dilution):
    if str_dilution == 'diluent':
        return 0
    dict1_val1 = re.findall(r':\d+', str_dilution)
    dict1_val = dict1_val1[0]
    dict1_val = dict1_val[1:]
    return dict1_val


folder_path = 'C:/Users/User/Documents/HertzLab/'  # must end with a
if os.path.exists(folder_path):
    print('found path')
else:
    print('cant find path')

df_data = pd.DataFrame(columns=['well_data', 'intensity'])

result_df = pd.read_excel(folder_path + 'Book_26_12.xlsx', index_col=0)
map_df = pd.read_excel(folder_path + 'concentration_map.xlsx', index_col=0)

j = 0
for i in range(1, 25):
    for index in map_df.index:
        if map_df.loc[index, i] == map_df.loc[index, i]:
            df_data.loc[j] = [map_df.loc[index, i], result_df.loc[index, i]]
            j += 1

df_data['intensity'] = df_data['intensity'].apply(lambda k: int(k))
diluent_mean = df_data.loc[df_data['well_data'] == 'diluent']
diluent_mean = diluent_mean.mean()
diluent_mean_float = float(diluent_mean[0])
# print(df_data.info())
df_data['intensity'] = df_data['intensity'].apply(sub_diluent, diluent=diluent_mean_float)

df_mean = df_data.groupby('well_data')['intensity'].mean()
df_mean = df_mean.to_frame()

# ---------------for checking concentration----------------------------------

list_of_index = df_mean.index.values
list_no_standard = []
for ind in list_of_index:
    if ind.startswith('IgG'):
        list_no_standard.append(ind)

all_readings = df_mean.drop(list_no_standard)

list_standard = []
for ind in list_of_index:
    if not (ind.startswith('IgG')):
        list_standard.append(ind)

all_readings['index'] = all_readings.index
all_readings['dilutions'] = all_readings['index'].apply(extract_dilutions)
all_readings = all_readings.drop(labels=['index'], axis=1)

standard_readings = df_mean.drop(list_standard)

dict = {}
for Ab in standard_readings.index:
    dict_val = re.findall(r'_\d+.\d+', Ab)
    dict_val = str(dict_val).strip('[]')
    dict[float(dict_val[2:-1])] = Ab

standard_readings['concentration'] = dict

# -------------------------regression--------------------------------------------
# find the best fit by dropping top readings
max_r_squ = 0

for conc_val in ['500', '250', '125']:
    x = np.array(standard_readings['concentration'])
    x = x.reshape(-1, 1)
    # print(x)
    y = np.array(standard_readings['intensity'])
    y = y.reshape(-1, 1)
    # print(y)
    lm = LinearRegression(fit_intercept=True)
    lm.fit(x, y)
    print(lm.coef_)
    y_predict = lm.predict(x)
    current_r = r2_score(y, y_predict)
    if conc_val == '125':
        break
    if current_r > max_r_squ:
        max_r_squ = current_r
        standard_readings = standard_readings.drop('IgG_std1_' + conc_val)

slope = lm.coef_
intercept = lm.intercept_
print(intercept)
# -------------------------regression--------------------------------------------
print("Estimated coefficient:\nslope = {}".format(slope))
# y=b0+b1x
print('Estimated values:\nr_value_squr = {}'.format(current_r))
# finding concentration from readings
all_readings['concentration'] = all_readings['intensity'].apply(find_con_from_eq, slope=slope, intercept=intercept)

# plotting-----------------------------------------------------------------------
g = sns.lmplot(y='intensity', x='concentration', data=standard_readings)
g.fig.tight_layout()
g.savefig(folder_path + 'concentration_of_standards.jpg', dpi=300)
plt.show()
# -------------------------------------------------------------------------------

# moltiply by diloution
all_readings['index'] = all_readings.index
all_readings['dilutions'] = all_readings['index'].apply(extract_dilutions)
all_readings[['concentration', 'dilutions']] = all_readings[['concentration', 'dilutions']].astype(float)
all_readings['concentration'] = all_readings['concentration'] * all_readings['dilutions']

# units of [ug/ml]
all_readings['concentration'] = all_readings['concentration'] / 1000

# all_readings = all_readings.drop(labels = ['dilutions'], axis=1)
# all_readings = all_readings.drop(labels = ['index'], axis=1)
all_readings['data_from'] = all_readings.index
all_readings['data_from'] = all_readings['data_from'].apply(type_of_result)
all_readings = all_readings.drop(['diluent'])

# plotting-----------------------------------------------------------------------

plt.figure(figsize=(10, 6))
g = sns.boxplot(x='data_from', y='concentration', data=all_readings, width=1)
g = sns.stripplot(x="data_from", y="concentration", data=all_readings)

g.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
# plt.legend(title='data_from', loc='upper left')
plt.xticks()

# plt.annotate('what the fuck',(all_readings['data_from'][1],all_readings['concentration'][1]))
plt.tight_layout()

plt.savefig(folder_path + 'concentration.jpg')
plt.show()

# print(type(all_readings['index'][1]))

"""
# plotting-----------------------------------------------------------------------

g = sns.FacetGrid(all_readings, col="data_from", hue="data_from")
g.map(sns.kdeplot, "dilutions", "concentration", alpha=.7)
plt.savefig(folder_path + 'concentration.jpg')
plt.show()
"""
# -----------------------------------------------------------------------------------
all_means_and_dilutions = df_mean.drop('diluent')
all_means_and_dilutions['index'] = all_means_and_dilutions.index
all_means_and_dilutions['dilutions'] = all_means_and_dilutions['index'].apply(
    lambda string: re.findall(r'\d+', string)[len(re.findall(r'\d+', string)) - 1])
all_means_and_dilutions['group'] = all_means_and_dilutions['index'].apply(lambda string: re.findall(r'\w+\s\d', string))
all_means_and_dilutions['group'] = all_means_and_dilutions['group'].apply(
    lambda list_ofone: list_ofone[0] if len(list_ofone) != 0 else 'ref')
