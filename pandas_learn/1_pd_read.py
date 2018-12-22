import pandas as pd
import matplotlib.pyplot as plt


housing_dataframe = pd.read_csv("/Users/SuperZemo/Downloads/california_housing_train.csv",sep=",")
housing_dataframe.describe()
housing_dataframe.head()
housing_dataframe.hist('housing_median_age')
plt.show()