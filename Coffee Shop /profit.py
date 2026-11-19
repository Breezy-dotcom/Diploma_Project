import pandas as pd
import plotly.express as px

# загрузка данных
df_products = pd.read_csv('products.csv')
df_order_items = pd.read_csv('order_items.csv')
df_order = pd.read_csv('orders.csv')

# объединение данных о продажах и товарах
df_sales = pd.merge(df_order_items, df_products, on='product_id')

# расчет прибыли
df_sales['profit'] = (df_sales['price'] - df_sales['cost']) * df_sales['quantity']

# расчет прибыли по категориям
profit_by_category = df_sales.groupby('category')['profit'].sum().reset_index()

profit_by_category['category'] = profit_by_category['category'].replace({
    'Bakery': 'Выпечка',
    'Cold Drinks': 'Холодные напитки',
    'Dessert': 'Десерты',
    'Food': 'Еда',
    'Hot Drinks': 'Горячие напитки'
})


# создание графика
fig = px.bar(
    profit_by_category,
    x='category',
    y='profit',
    title='Прибыль кофейни по категориям за 2025 год',
    text='profit',



    labels={
        'category': 'Категория товаров',
        'profit': 'Прибыль (руб.)',
    },

)


fig.update_layout(
    xaxis_title='Категория товаров',
    yaxis_title='Прибыль (руб.)',

),


fig.update_traces(
    texttemplate='%{y:,.0f} ₽',
    textposition='outside'

),




fig.show()
