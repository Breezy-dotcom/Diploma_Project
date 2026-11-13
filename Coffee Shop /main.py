import pandas as pd
import plotly.express as px


# загрузка данных
df_orders = pd.read_csv('orders.csv')
df_products = pd.read_csv('products.csv')
df_order_items = pd.read_csv('order_items.csv')

# объединение данных о продажах и товарах
df_sales = pd.merge(df_order_items, df_products, on='product_id')

# расчет выручки
df_sales['revenue'] = df_sales['price'] * df_sales['quantity']
total_revenue = df_sales['revenue'].sum()

print(f"Общая выручка кофейни: {total_revenue} руб.")

# расчет ежемесячной выручки
monthly_revenue = df_sales.groupby('month_id')['revenue'].sum().reset_index()
df = pd.merge(df_orders, monthly_revenue, on='month_id')


# создание графика
fig = px.line(
    df,
    x='month',
    y='revenue',
    title='Выручка кофейни по месяцам за 2025 год',
    markers=True
)

# оформление графика
fig.update_traces(
    line=dict(color='blue', width=3),
    marker=dict(size=8)

)


fig.show()