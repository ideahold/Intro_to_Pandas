import pandas as pd
data = pd.read_csv('data.csv', index_col=0)

data.describe()

data.points.describe()

data.points.mean()

data.taster_name.unique()

data.taster_name.value_counts()


data_mean_points = data.points.mean()
data.points.map(lambda p: p - data_mean_points)


def rp(row):
    row.points = row.points - data_mean_points
    return row

data.apply(rp, axis='columns')
