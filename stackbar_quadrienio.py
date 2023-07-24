import pandas as pd
import plotly.express as px

# Ler o arquivo CSV
df = pd.read_csv('quadrienio.csv')
df = df[:-4]

# Remover valores nulos (NaN) do DataFrame
df = df.dropna(subset=['QUANTIDADE', 'NÍVEL', 'TIPO'])

# letras minúsculas
df['NÍVEL'] = df['NÍVEL'].str.lower()
df['TIPO'] = df['TIPO'].str.lower()

# Combinação
df['Categoria'] = df['NÍVEL'] + ' - ' + df['TIPO']


# Reordenar
ordem_desejada = ['mestrado - matrícula', 'mestrado - defesa', 'doutorado - matrícula', 'doutorado - defesa']
categoria_ordenada = pd.CategoricalDtype(categories=ordem_desejada, ordered=True)
df['Categoria'] = df['Categoria'].astype(categoria_ordenada)
df = df.sort_values(by='Categoria')

#Gráfico interativo
fig = px.bar(df, x='ANO', y='QUANTIDADE', color='Categoria', barmode='stack',
             labels={'QUANTIDADE': 'Quantidade', 'ANO': 'Ano', 'NÍVEL': 'Nível', 'TIPO': 'Tipo'},
             color_discrete_sequence=['#381787',"#6528F7", "#A076F9","#D7BBF5"],
             title='Quadriênio 2017-2023')

#Legendas
fig.update_layout(
    legend_title_text='Legenda',
    legend=dict(
        title_font=dict(size=14),
        font=dict(size=12),
    ),
    yaxis_title='Quantidade',       # Título do eixo y (quantidade)
)

# Salvar o gráfico interativo em um arquivo HTML
fig.write_html('stackbar_quadrienio.html')
