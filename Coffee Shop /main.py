import pandas as pd
import plotly.express as px

# загрузка данных
df_products = pd.read_csv('products.csv')
df_order_items = pd.read_csv('order_items.csv')
df_order = pd.read_csv('orders.csv')

# объединение данных
df = pd.merge(df_order_items, df_products, on='product_id')

# расчет показателей
revenue = (df['price'] * df['quantity']).sum()
expenses = (df['cost'] * df['quantity']).sum()
profit = revenue - expenses


print('Выручка:', revenue)
print('Расходы:', expenses)
print('Прибыль:', profit)


# создание графика
fig = px.bar(
    x=['Выручка', 'Расходы', 'Прибыль'],
    y=[revenue, expenses, profit],
    title='Финансовые показатели кофейни за 2025 год',
    color_discrete_sequence=['peru']
)


fig.update_traces(
    texttemplate='%{y:,.0f} руб.',
    textposition='outside'
)

fig.update_layout(
    showlegend=False,
    xaxis_title='Категория',
    yaxis_title='Сумма (руб.)'
)

fig.show()
