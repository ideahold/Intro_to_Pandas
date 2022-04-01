import pandas as pd
data = pd.read_csv('data.csv', index_col=0)

data.rename(columns={'points' : 'quality'}) # заменяем имя столбца points на quality

data.rename(index={0: 'firstRow', 1: 'secondRow'}) # изменяем имя строк


# Combining section
data = pd.read_csv('data.csv')
data2 = pd.read_csv('data2.csv')

pd.concat( [data, data2] ) # объеденяем две таблицы
