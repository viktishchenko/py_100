import pandas as pd

SRC = 'D:/pyAngela/day25/pandas_2_analysis/squirrel_data.csv'

data = pd.read_csv(SRC)

# GET COLUMNS NAME
# col = data.columns # ['X', 'Y', ...,'Primary Fur Color']
# GET COLUMN VALUE
# column_data = data['Primary Fur Color']
    # 0            NaN
    # 1           Gray
    # 2       Cinnamon
    # 3           Gray
    # ...

# GET COLUMN VALUE COUNT
# column_data = data['Primary Fur Color'].value_counts() # [2473, 392, 103]

# SAVE AS COUNT.CSV
# column_data.to_csv('day25/pandas_2_analysis/squirrel_analysis.csv')

# OR
column_data = data['Primary Fur Color']
    # 0            NaN
    # 1           Gray
    # 2       Cinnamon
    # 3           Gray
    # 4            NaN

# print(type(column_data)) # <class 'pandas.core.series.Series'>
color = column_data.value_counts()
# gray = color['Gray'] # np.int64(2473)
# black = color['Black'] # np.int64(103)
# red = color['Cinnamon'] # np.int64(392)

data_dict = {
  'Fur colors': ['Gray','Black', 'Red'],
  'Count': [color['Gray'],color['Black'],color['Cinnamon']],
}

pd.DataFrame(data_dict).to_csv('day25/pandas_2_analysis/squirl_data.csv')



# OR

# data = pd.read_csv(SRC)
# # gray_sqirrel = data[data['Primary Fur Color'] == 'Gray']
#     # print(gray_sqirrel)
#     #               X          Y  ... Other Interactions                                      Lat/Long
#     # 1    -73.957044  40.794851  ...                 me  POINT (-73.9570437717691 40.794850940803904)
#     # ...         ...        ...  ...                 ...
#     # 3021 -73.963994  40.789915  ...                NaN    POINT (-73.9639941227864 40.7899152327912)
# gray_sqirrel_num = len(data[data['Primary Fur Color'] == 'Gray']) # 2473
# black_sqirrel_num = len(data[data['Primary Fur Color'] == 'Black']) # 103
# red_sqirrel_num = len(data[data['Primary Fur Color'] == 'Cinnamon']) # 392

# # CONSTRACT DATA FRAME

# # a) CREATE A DICTIONARY
# data_dict = {
#   'Fur color':['Gray', 'Black', 'Red'],
#   'Count': [gray_sqirrel_num, black_sqirrel_num,red_sqirrel_num]
# }
# squrl_data = pd.DataFrame(data_dict)
#     #   Fur color  Count
#     # 0      Gray   2473
#     # 1     Black    103
#     # 2       Red    392
# squrl_data.to_csv('day25/pandas_2_analysis/squrl_data.csv')
