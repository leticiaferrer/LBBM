import pandas as pd
import plotly.express as px

# Ler o arquivo CSV
df = pd.read_csv('c:/Users/LBBM/Documents/Python_files/\Quadriênio/quadrienio.csv')
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
             color_discrete_sequence=['#B3C890',"#DBDFAA", "#749BC2","#91C8E4"],
             title='Quadriênio 2017-2023'
            )

#Legendas
fig.update_layout(
    title_font=dict(size=24),         
    xaxis_title="Ano",      
    xaxis=dict(
        tickfont=dict(size=20, family='Arial, bold'),
        title_font=dict(size=24),
        title_standoff=40
    ), 
    yaxis_title="Quantidade",        
    yaxis=dict(
        title_font=dict(size=24, family='Arial, bold'),     
        tickfont=dict(size=20),
        title_standoff=40,        
    ),
    legend_title_text='Legenda',      
    legend=dict(
        title_font=dict(size=25),     
        font=dict(size=20)            
    )
)

# Salvar o gráfico interativo em um arquivo HTML
fig.write_html('stackbar_quadrienio12.html')


