import pandas as pd

data = pd.read_csv('data.csv', index_col=0) # сохраняем без пустых записей

data.country # data['country'] - альтернатива


# iloc функция "выбор по метке"
data.iloc[0] # data.iloc[:, 0], data.iloc[-3:, 0] - можно также работать с срезом списков

# loc функция "выбор по позиции"
data.loc[0, 'country']

data.loc[0, ['country', 'description', 'taster_twitter_handle']]

data.loc[data.country == 'US']

data.loc[(data.country == 'US') & (data.points == 90)]
