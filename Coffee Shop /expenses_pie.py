import pandas as pd
import plotly.express as px


# загрузка данных
df_products = pd.read_csv('products.csv')
df_order_items = pd.read_csv('order_items.csv')
df_order = pd.read_csv('orders.csv')

# объединение данных о продажах и товарах
df_sales = pd.merge(df_order_items, df_products, on='product_id')


# расчет расходов
df_sales['expenses'] = df_sales['cost'] * df_sales['quantity']


# расчет расходов по категориям
expenses_by_category = df_sales.groupby('category')['expenses'].sum().reset_index()

expenses_by_category['category'] = expenses_by_category['category'].replace({
    'Hot Drinks': 'Горячие напитки',
    'Dessert': 'Десерты',
    'Bakery': 'Выпечка',
    'Food': 'Еда',
    'Cold Drinks': 'Холодные напитки'
})


# создание круговой диаграммы
fig = px.pie(
    expenses_by_category,
    names='category',
    values='expenses',
    title='Расходы кофейни по категориям за 2025 год',

)


fig.show()
