import pandas as pd

def table(**kwargs):
    return pd.DataFrame(kwargs).set_index('Марка')

dict1 = {'Марка': pd.Series(['Жигули', 'Honda', 'KIA']), 'Модель': pd.Series(['2107', 'Fit', 'Ceed']),
         'Мощность ДВС(л.с.)': pd.Series([121, 121, 124])}
dict1_list = {k: v.tolist() for k, v in dict1.items()}
car = table(**dict1_list)
print(car)
print()

def func(**kwargs):
    df = pd.DataFrame(kwargs).set_index('x')
    df['y'] = pd.to_numeric(df['y'], errors='coerce')
    return df
x = {'x': [1, 2, 3], 'y': [3, 'a', 5]}
x_ = func(**x)
print(x_)




