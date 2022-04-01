import pandas as pd
data = pd.read_csv('data.csv', index_col=0)

data.groupby('points').price.min() # выводим минимальное значение цены для каждого значения points

# выводим продукт с самым высоким значением points для каждой провинции в каждой стране
data.groupby(['country', 'province']).apply(lambda x: x.loc[x.points.idxmax()])


# сортируем по значениям (слова по алфавиту, числа по возрастани)
data.sort_values(by='country')

data.sort_values(by=['country', 'points'])


data[pd.isnull(data.country)] # выводим все столбцы с пустым значение в стобце country

data.region_2.fillna('Unknown') # заменить все NaN на 'Unknown'


# replace заменяет одно значение на другое
data.taster_twitter_handle.replace('@kerinokeefe', '@slava')
