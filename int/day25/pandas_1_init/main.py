# CSV DATA

# day,temp,condition
# Monday,12,Sunny
# Tuesday,14,Rain
# Wednesday,15,Rain
# Thursday,14,Cloudy
# Friday,21,Sunny
# Saturday,22,Sunny
# Sunday,24,Sunny


# # with open('D:/pyAngela/day25/weather_data.csv') as data_file:
# #   data = data_file.readlines() # data>>> ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++
# # python install
# # py -3 --version // Python 3.13.2 cmd
# # py --version // Python 3.13.2 (check python version)
# # py -m pip install prettytable // add prettytable
# # ++++++++++++++++++++++++++++++++++++++++++++++++++++

# import csv

DATA_SRC = 'D:/pyAngela/day25/pandas_1_init/weather_data.csv'

# with open(DATA_SRC) as data_file:
#   data = csv.reader(data_file) # data>>> <_csv.reader object at 0x000001FD913ED540>
#   temperature = []
#   for row in data:
#     # print(f'row>>> {row}')
#     # row>>> ['day', 'temp', 'condition']
#     # row>>> ['Monday', '12', 'Sunny']
#     # row>>> ['Tuesday', '14', 'Rain']
#     # row>>> ['Wednesday', '15', 'Rain']
#     # row>>> ['Thursday', '14', 'Cloudy']
#     # row>>> ['Friday', '21', 'Sunny']
#     # row>>> ['Saturday', '22', 'Sunny']
#     # row>>> ['Sunday', '24', 'Sunny']
#     if row[1] != 'temp':
#       temperature.append(int(row[1])) # temperature>>> [12, 14, 15, 14, 21, 22, 24]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pandas

data = pandas.read_csv(DATA_SRC)

#RANDAS READ CSV FILE

#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

# PANDAS DATA STRUCTURE TYPES

# print(type(data)) # <class 'pandas.core.frame.DataFrame'> (WHOLE TABLE OF DATA)
# print(type(data['temp'])) # <class 'pandas.core.series.Series'>  (SINGLE COLUMN IN TABLE - LIST)

# PANDAS READ COLUMN

# print(data['temp'])
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

# PANDAS DOCS: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html

# convert DATA → TO DATA DICTIONARY

# data_dict = data.to_dict()
# print(f'data_dict>>> {data_dict}') # data_dict>>> {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# convert DATA → TO DATA LIST

# day_list = data['day'].to_list()
# print(f'day_list>>> {day_list}') # day_list>>> ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(f'length_of_day_list>>> {len(day_list)}') # length_of_day_list>>> 7

# TEMPERATURE AVERAGE MATH/STATISTIC

# temp_average = sum(data['temp']) / len(data['temp']) # 17.428571428571427
# print(round(temp_average, 3)) # 17.429

# import statistics

# temp_stat = statistics.mean(data['temp']) # temp_stat>>> 17.428571428571427
# print(f'temp_stat>>> {temp_stat}')

# number = 123.123123
# s = str(number)
# print(f's>>> {s}') # s>>> 123.123123
# print(f'len(s)>>> {len(s)}') # 10
# print(f's.find(".")>>>', {s.find('.')}) # 3
# print(f's.find(".")>>>', {abs(s.find('.'))}) # 3
# print(abs(s.find('.') - len(s)) - 1) # 6

# def get_count(number):
#     s = str(number)
#     if '.' in s:
#         return abs(s.find('.') - len(s)) - 1
#     else:
#         return 0

# import math
# print(len(str(math.pi).split('.')[1])) # 15

# print(str(0.00000001)) # 1e-08

# l = list(range(10)) # l>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# FIND MAXIMUM NUMBER

# list  = data['temp'].to_list()
# for idx,num in enumerate(list):
#   max_num = 0
#   if max_num <  list[idx]:
#     max_num = list[idx]
# print(f'max_num>>> {max_num}') # 24

# pandas_max = data['temp'].max() # 24
# print(f'pandas_max>>> {pandas_max}')


pd = pandas

df = pd.DataFrame({'population': [59000000, 65000000, 434000,
                                  434000, 434000, 337000, 11300,
                                  11300, 11300],
                   'GDP': [1937894, 2583560 , 12011, 4520, 12128,
                           17036, 182, 38, 311],
                   'alpha-2': ["IT", "FR", "MT", "MV", "BN",
                               "IS", "NR", "TV", "AI"]},
                  index=["Italy", "France", "Malta",
                         "Maldives", "Brunei", "Iceland",
                         "Nauru", "Tuvalu", "Anguilla"])
                         

print(df)
  #           population      GDP alpha-2
  # Italy       59000000  1937894      IT
  # France      65000000  2583560      FR
  # Malta         434000    12011      MT
  # Maldives      434000     4520      MV
  # Brunei        434000    12128      BN
  # Iceland       337000    17036      IS
  # Nauru          11300      182      NR
  # Tuvalu         11300       38      TV
  # Anguilla       11300      311      AI

# print(df.nlargest(3,'population', keep='last'))

# print(data.temp)
# print(data['temp'])
# print(df.index)

# GET ROW DATA

# row = data[data.day == 'Monday'] # 0  Monday    12     Sunny

# res = df[df.population == 337000]
  #          population    GDP alpha-2
  # Iceland      337000  17036      IS


# large_temp_row = data.nlargest(1,'temp') # 6  Sunday    24     Sunny
# max_temp = data['temp'].max()
# # max_temp_row = data[data["temp"] == max_temp]
# max_temp_row = data[data.temp == max_temp]
# print('max_temp_row>>>',max_temp_row)
    # day  temp condition
    # 6  Sunday    24     Sunny
# print('to_dict>>>',max_temp_row.to_dict()) # {'day': {6: 'Sunday'}, 'temp': {6: 24}, 'condition': {6: 'Sunny'}}
# print('loc/iloc>>>',data.loc[1])
    # day          Tuesday
    # temp              14
    # condition       Rain
    # Name: 1, dtype: object
# print('loc/iloc values>>>',data.loc[1].values) # ['Tuesday' np.int64(14) 'Rain']
# print('loc/iloc values [0]>>>',data.loc[1].values[1]) # 14

# CELSIUS TO FAHRENHEIT

# celsium_temp = data.iloc[0].values[1]
# f_temp = (celsium_temp*9/5)+32 # 53.6

# or

# mon = data[data.day == 'Monday']
#     #    day  temp condition
#     # 0  Monday    12     Sunny
# mon_temp = mon.temp[0]
# f_temp = mon_temp*9/5+32 # 53.6

#CREATE DATA FRAME FROM SCRATCH
data_dict = {
  'students': ['Ammy', 'James', 'Tory'],
  'score': [76, 57, 83]
} # {'students': ['Ammy', 'James', 'Tory'], 'score': [76, 57, 83]}

data2 = pd.DataFrame(data_dict)
print(data2)
    #   students  score
    # 0     Ammy     76
    # 1    James     57
    # 2     Tory     83

# CONVERT TO CSV
# data2.to_csv('day25/stud.csv')






