from __future__ import print_function
from pandas_learn import *
import numpy as np


print("------------------索引------------------")

print(city_names.index)
print(city_dataframe.index)
print(city_dataframe.reindex([2, 0, 1]))

for n in range(0, 3):
    print("------------------reindex", n, "------------------")
    print(city_dataframe.reindex(np.random.permutation(city_dataframe.index)))

print(city_dataframe.reindex([0, 6, 20]))