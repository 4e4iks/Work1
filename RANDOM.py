import pandas as pd

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем словарь для отображения уникальных значений в целые числа
unique_values = data['whoAmI'].unique()
value_to_int = {value: i for i, value in enumerate(unique_values)}

# Создаем новый DataFrame с one-hot закодированными столбцами
one_hot_data = pd.DataFrame()
for value in unique_values:
    one_hot_data[f'is_{value}'] = (data['whoAmI'] == value).astype(int)

# Выводим one-hot закодированный DataFrame
one_hot_data.head()
