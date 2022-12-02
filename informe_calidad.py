import pandas as pd

df_diccionario_datos = pd.read_csv('data_dictionary.csv',sep = ",", encoding = "LATIN_1")

tipos_diccionario = df_diccionario_datos.dtypes
print(f'El tipo de datos de cada columna en el data_dictionary.csv es:\n{tipos_diccionario}')
print('\n')
nans_diccionario = df_diccionario_datos.isna().sum()
print(f'El número de NaN por cada columna en el data_dictionary.csv es:\n{nans_diccionario}')
print('\n')
nulls_diccionario = df_diccionario_datos.isnull().sum()
print(f'El número de Null por cada columna en el data_dictionary.csv es:\n{nulls_diccionario}')
print('\n')


df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ",", encoding = "LATIN_1")

tipos_detalle_pedidos = df_detalle_pedidos.dtypes
print(f'El tipo de datos de cada columna en el order_details.csv es:\n{tipos_detalle_pedidos}')
print('\n')
nans_detalle_pedidos = df_detalle_pedidos.isna().sum()
print(f'El número de NaN por cada columna en el order_details.csv es:\n{nans_detalle_pedidos}')
print('\n')
nulls_detalle_pedidos = df_detalle_pedidos.isnull().sum()
print(f'El número de Null por cada columna en el order_details.csv es:\n{nulls_detalle_pedidos}')
print('\n')


df_pedidos = pd.read_csv('orders.csv',sep = ",", encoding = "LATIN_1")

tipos_pedidos = df_pedidos.dtypes
print(f'El tipo de datos de cada columna en el orders.csv es:\n{tipos_pedidos}')
print('\n')
nans_pedidos = df_pedidos.isna().sum()
print(f'El número de NaN por cada columna en el orders.csv es:\n{nans_pedidos}')
print('\n')
nulls_pedidos = df_pedidos.isnull().sum()
print(f'El número de Null por cada columna en el orders.csv es:\n{nulls_pedidos}')
print('\n')


df_tipos_pizza = pd.read_csv('pizza_types.csv', sep = ",", encoding = "LATIN_1")

tipos_tipos_pizza = df_tipos_pizza.dtypes
print(f'El tipo de datos de cada columna en el pizza_types.csv es:\n{tipos_tipos_pizza}')
print('\n')
nans_tipos_pizza = df_tipos_pizza.isna().sum()
print(f'El número de NaN por cada columna en el pizza_types.csv es:\n{nans_tipos_pizza}')
print('\n')
nulls_tipos_pizza = df_tipos_pizza.isnull().sum()
print(f'El número de Null por cada columna en el pizza_types.csv es:\n{nulls_tipos_pizza}')
print('\n')


df_pizza = pd.read_csv('pizzas.csv', sep = ",", encoding = "LATIN_1")

tipos_pizza = df_pizza.dtypes
print(f'El tipo de datos de cada columna en el pizzas.csv es:\n{tipos_tipos_pizza}')
print('\n')
nans_pizza = df_pizza.isna().sum()
print(f'El número de NaN por cada columna en el pizzas.csv es:\n{nans_pizza}')
print('\n')
nulls_pizza = df_pizza.isnull().sum()
print(f'El número de Null por cada columna en el pizzas.csv es:\n{nulls_pizza}')