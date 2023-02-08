# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv('california_housing_train.csv')

df #вывести всё

df.head(7) #выборка сверху

df.tail(3) #выборка снизу

df.shape #показать количество ячеек - строки и столбцы

df.isnull() #проверка на нулевые элементы false - если не пустой, true, если пустой

df.isnull().sum() #проверим сумму, чтобы найти пустую ячейку

df.dtypes # проверка типов



df.columns #названия столбцов

df['latitude'] #вывести столбец

df[['latitude', 'population']] #вывести два столбец

df[df['housing_median_age'] < 20] #сделали выборку по условию

df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
#объединили условия запросов

df.loc[df['housing_median_age'] > 20, ('total_rooms', 'total_bedrooms')]

df['population'].max() #максимальное

df['population'].min() #минимальное

df['population'].mean() #среднее

df[['population', 'total_rooms']].median() # среднее в двух столбцах

df.describe() #статистические данные

import seaborn as sns

sns.scatterplot(data=df, x='longitude', y='latitude')

sns.scatterplot(data=df, x='households', y='population', hue='total_rooms') #
 

cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)


sns.relplot(data=df, x='latitude', y='median_house_value', kind='line')

sns.histplot(data=df, x='median_income')

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Взрослые'
#маркируем столбцы

df

df.groupby('age_group')['median_income'].mean().plot(kind='bar')

