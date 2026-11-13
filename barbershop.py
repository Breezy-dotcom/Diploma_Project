# import pandas as pd
# import plotly.express as px
# from dash import Dash, html, dcc
#
# # Загрузка данных
# df = pd.read_csv('data.csv')
#
# # Создание графика
# fig = px.bar(
#     df,
#     x='month',
#     y='revenue',
#     color='year',
#     barmode='group',
#     title='Сравнение доходов барбершопа за 2024 и 2025 годы',
#     text_auto=True
# )
#
# # Создание линейного графика
# fig_line = px.line(
#     df,
#     x='month',
#     y='revenue',
#     color='year',
#     title='Изменение доходов барбершопа за 2024 и 2025 годы',
#     markers=True
# )
#
# # Расчет общего дохода за каждый год
# df_2024 = df[df['year'] == '2024 год']
# df_2025 = df[df['year'] == '2025 год']
#
# total_2024 = df_2024['revenue'].sum()
# total_2025 = df_2025['revenue'].sum()
#
# # Расчет роста доходов
# growth = round((total_2025 - total_2024) / total_2024 * 100, 2)
#
# # Создание приложения
# app = Dash()
#
# app.layout = html.Div([
#     html.H1('Анализ доходов барбершопа за 2024–2025 годы'),
#
#     html.H2(f'Общий доход за 2024 год: {total_2024:,} руб.'),
#     html.H2(f'Общий доход за 2025 год: {total_2025:,} руб.'),
#     html.H2(f'Рост доходов: {growth} %'),
#
#
#     dcc.Graph(figure=fig),
#     dcc.Graph(figure=fig_line)
# ])
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
