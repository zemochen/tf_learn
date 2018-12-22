import pandas as pd
#####
#  详见:https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=pandas-colab&hl=zh-cn&authuser=0&refresh=1#scrollTo=yBdkucKCwy4x
#  副本：https://colab.research.google.com/drive/1EGHdQxrDDQuFz2O5gfGPSj8hP_dZ3yLx
#######


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
city_dataframe = pd.DataFrame({"city": city_names, "population": population})
