import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['figure.figsize'] = 8,6
df_features = pd.read_csv("kaggle_ACS_Financial_Features.csv", encoding='ISO-8859-1' )
#looking the shape of data
print(df_features.shape)

#in my local notebook I also have plotted describe(), info() functions
print(df_features.nunique())
df_features.head()
print(df_features.Type.value_counts())
plt.subplot(221)
g = sns.factorplot(x='Type', data=df_features, kind="count",size=6,aspect=2)
g.set_titles("Count by Type")
# plt.show()
print(df_features.Primary.value_counts())

sns.factorplot(x="Primary", data=df_features, kind="count",size=5,aspect=1)
plt.show()


g = sns.factorplot(x="Type", data=df_features,
               kind="count", hue="Primary",
               size=5, aspect=2)
g.set_axis_labels(x_var="Types",
                  y_var="Counting")
plt.show()

fig, ax = plt.subplots(5,1, figsize=(12,8*3))

sns.distplot(df_features['family_income_mean'],
             ax=ax[0],bins=50)
sns.boxplot(x='Type', y='family_income_mean', data=df_features,
            ax=ax[1])
sns.boxplot(x='Type', y='family_income_median', data=df_features,
            ax=ax[2])
sns.boxplot(x='Type', y='family_income_stdev', data=df_features,
            ax=ax[3])
sns.boxplot(x='Type', y='family_income_families', data=df_features,
            ax=ax[4])

plt.show()


fig, ax = plt.subplots(5,1, figsize=(12,8*3))

sns.distplot(df_features['gross_rent_mean'],
             ax=ax[0],bins=50)
sns.boxplot(x='Type', y='gross_rent_mean', data=df_features,
            ax=ax[1])
sns.boxplot(x='Type', y='gross_rent_median', data=df_features,
            ax=ax[2])
sns.boxplot(x='Type', y='gross_rent_stdev', data=df_features,
            ax=ax[3])
sns.boxplot(x='Type', y='gross_rent_samples', data=df_features,
            ax=ax[4])

plt.show()




fig, ax = plt.subplots(5,1, figsize=(12,8*3))

sns.distplot(df_features['morgages_ocsts_mean'],
             ax=ax[0],bins=50)
sns.boxplot(x='Type', y='morgages_ocsts_mean', data=df_features,
            ax=ax[1])
sns.boxplot(x='Type', y='morgages_ocsts_median', data=df_features,
            ax=ax[2])
sns.boxplot(x='Type', y='morgages_ocsts_stdev', data=df_features,
            ax=ax[3])
sns.boxplot(x='Type', y='morgages_csts_samples', data=df_features,
            ax=ax[4])

plt.show()


fig, ax = plt.subplots(5,1, figsize=(12,8*3))

sns.distplot(df_features['owner_cost_mean'],
             ax=ax[0],bins=50)
sns.boxplot(x='Type', y='owner_cost_mean', data=df_features,
            ax=ax[1])
sns.boxplot(x='Type', y='owner_cost_median', data=df_features,
            ax=ax[2])
sns.boxplot(x='Type', y='owner_cost_stdev', data=df_features,
            ax=ax[3])
sns.boxplot(x='Type', y='owner_cost_samples', data=df_features,
            ax=ax[4])
plt.show()




fig, ax = plt.subplots(5,1, figsize=(12,8*3))

sns.distplot(df_features['household_income_mean'],
             ax=ax[0],bins=50)
sns.boxplot(x='Type', y='household_income_mean', data=df_features,
            ax=ax[1])
sns.boxplot(x='Type', y='household_income_median', data=df_features,
            ax=ax[2])
sns.boxplot(x='Type', y='household_income_stdev', data=df_features,
            ax=ax[3])
sns.boxplot(x='Type', y='household_income_wsum', data=df_features,
            ax=ax[4])
plt.show()


print("States with frequency greatest than 500: ")
print(df_features.State_Name.value_counts()[:13])

g = sns.factorplot(x="State_Name", data=df_features,
                   kind="count", size = 6, aspect=2,
                   orient='v')
g.set_titles(template="State count")
g.set_axis_labels(x_var="States Name",
                  y_var="Counting ")
g.set_xticklabels(rotation=90)
plt.show()
