import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale
import sklearn.preprocessing as sp
import functools
df = pd.read_csv('consolidated_coin_data.csv')
a = df.Date = pd.to_datetime(df.Date)#to convert date format in file
# a.to_csv("DATE.csv")
df = df[::-1]
# print(df)
df.head()
cripto_coin = [] #creating empty list
cripto_list = []
for i in df.Currency.unique():
    if df[df.Currency == i][['Date','Close']].shape[0] > 200:
        cripto_coin.append(df[df.Currency == i][['Date','Close']])
        cripto_list.append(i)
concatenated=functools.reduce(lambda left,right: pd.merge(left,right,on='Date',how='left' if left.shape[0] > right.shape[0] else 'right'),cripto_coin)
print(concatenated.shape)
concatenated.head()
# correlation_set = pd.DataFrame(sp.minmax_scale(pd.fit_transform(concatenated.iloc[:,1:].dropna())),crypto_list)
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.figure(figsize=(20,20))
# sns.heatmap(correlation_set.corr())
# plt.show()
