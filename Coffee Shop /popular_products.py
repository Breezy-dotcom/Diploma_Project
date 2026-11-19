import pandas as pd
import plotly.express as px

# загрузка данных
df_products = pd.read_csv('products.csv')
df_order_items = pd.read_csv('order_items.csv')
df_order = pd.read_csv('orders.csv')

# объединение данных о продажах и товарах
df_sales = pd.merge(df_order_items, df_products, on='product_id')

# расчет количества продаж по товарам
sales_by_product = df_sales.groupby('product_name')['quantity'].sum().reset_index()
sales_by_products = sales_by_product.sort_values(by='quantity', ascending=False)

# создание графика
fig = px.bar(
    sales_by_product,
    x='quantity',
    y='product_name',
    title='Самые продаваемые товары за 2025 год',
    labels={
        'quantity': 'Количество проданных товаров',
        'product_name': 'Название товара'
    },
    orientation='h',
    text='quantity',
    color_discrete_sequence=['grey']
)

fig.update_yaxes(categoryorder='total ascending')



fig.update_traces(
    textposition='outside',

)


fig.show()
