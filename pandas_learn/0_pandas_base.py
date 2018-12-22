from __future__ import print_function
from pandas_learn import *
import numpy as np

# print("version:"+pd.__version__)


print(city_dataframe.head())
# print(city_dataframe.hist('population'))
print(type(city_dataframe['city']))
print(city_dataframe['city'])

print(type(city_dataframe['city'][1]))
print(city_dataframe['city'][1])

print(type(city_dataframe[0:2]))
print(city_dataframe[0:2])

print("------------------操作数据------------------")
print(population / 1000.)

print("------------------numpy ------------------")
print(np.log(population))

print(population.apply(lambda val: val > 1000000))




