import pandas as pd
data = pd.read_csv('data.csv', index_col=0)

data.describe()

data.points.describe() # описание столбца (или всей таблицы), подробнее можно узнать в видео на канале

data.points.mean() # выводим среднее значение по столбцу

data.taster_name.unique() # выводим все значения без повторений

data.taster_name.value_counts() # количество каждого значения в столбце


data_mean_points = data.points.mean()
# map позволяет применить некоторые действия ко всему столбцу
# lambda принимает (p) и возвращает (p - data_mean_points) для каждой ячейки
data.points.map(lambda p: p - data_mean_points) 

# аналогичная запись с использованием apply()
def rp(row):
    row.points = row.points - data_mean_points
    return row

data.apply(rp, axis='columns')
