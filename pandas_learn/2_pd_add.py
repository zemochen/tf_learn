from __future__ import print_function
from pandas_learn import *


print("------------------dataframe add------------------")
city_dataframe['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
city_dataframe['Population density'] = population / city_dataframe['Area square miles']

print(city_dataframe)

city_dataframe['famous'] = (city_dataframe['Area square miles'] > 50) & city_dataframe['city'].apply(
    lambda name: name.startswith('San'))

print(city_dataframe)