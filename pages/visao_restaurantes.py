#Importando as bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import folium as fl
import plotly.graph_objects as go

from PIL import Image
from streamlit_folium import folium_static
from folium.plugins import FastMarkerCluster

#================================
#Funções:
#================================
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

def clear_code(df1):
    for i in range(df1.shape[0]):
        df1.loc[i, 'Country Code'] = country_name(df1.loc[i, 'Country Code'])
        df1.loc[i, 'Price range'] = create_price_tye(df1.loc[i, 'Price range'])
        df1.loc[i, 'Rating color'] = color_name(df1.loc[i, 'Rating color'])  
        
    df1["Cuisines"] = df1.loc[:, "Cuisines"].astype(str).apply(lambda x: x.split(",")[0])
    
    for i in range(len(df1.columns)):
        df1 = df1.loc[df1[df1.columns[i]] != 'nan',:]
        
    return df1

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df11.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df1.columns = cols_new
    return df1

def colunas(df1, ordenacao):
    df1_aux = (df1.loc[:,['Restaurant Name','Aggregate rating','City','Average Cost for two', 'Country Code', 'Cuisines']]
                      .groupby(['Country Code','Restaurant Name','City','Cuisines','Average Cost for two'])
                      .mean()
                      .sort_values(['Aggregate rating'], ascending=ordenacao)
                      .reset_index())
    return df1_aux

#-------------------------------- Inicio da Estrutura lógica do código --------------------------------
df = pd.read_csv('../dataset/zomato.csv.zip')
df1 = df.copy()

df1 = clear_code(df1)
df = df1.copy()
st.set_page_config(
    page_title="🥣 Restaurante",
    layout='wide'   
)

#==================================
# Barra Lateral Streamlit
#==================================
image = Image.open('../logo.png')
st.sidebar.image(image, width=100)

st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('### Sua melhor comida está aqui #')
st.sidebar.markdown("""---""")

country_unique = df1['Country Code'].unique()

qtd_country = st.sidebar.slider('Quantos paises deseja ver?',min_value=0,max_value=len(country_unique))

if qtd_country < 6:
    qtd_country = 6

country = st.sidebar.multiselect('Escolha o país que deseja filtrar',
                                country_unique,
                                default=country_unique[0:qtd_country])

selecao = df1['Country Code'].isin(country)
df1 = df1.loc[selecao,:]



restaurant_unique = df1['Restaurant Name'].unique()

qtd_country = st.sidebar.slider('Quantos restaurantes deseja ver?',min_value=0,max_value=len(restaurant_unique))

if qtd_country < 6:
    qtd_country = 6

cuisines = df1['Cuisines'].unique()

cuisines = st.sidebar.multiselect('Escolha o país que deseja filtrar',
                                cuisines,
                                default=cuisines[0:5])

selecao = df1['Cuisines'].isin(cuisines)
df1 = df1.loc[selecao,:]

#==================================
# Main Page
#==================================
st.markdown('# Visão por Tipos de Pratos')
st.markdown('## Melhores resutantes por tipos de pratos culinários')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    with col1:
        df1_aux = colunas(df1, False)
        col1.metric('Pais: ', df1_aux.iloc[0,0], help="Com base no filtro aplicado")
        
    with col2:
        df1_aux = colunas(df1, False)
        col2.metric('Melhor Restaurante: ', df1_aux.iloc[0,1], help="Com base no filtro aplicado")

    with col3:
        df1_aux = colunas(df1, False)
        col3.metric('Melhor Culinária: ', value=str(df1_aux.iloc[0,3]), help="Com base no filtro aplicado")

    with col4:
        df1_aux = colunas(df1, False)
        col4.metric('Vlr Prato P/ 2: ', value=str(df1_aux.iloc[0,4]), help="Com base no filtro aplicado")

    with col5:
        df1_aux = colunas(df1, False)
        col5.metric('Nota: ', value=str(df1_aux.iloc[0,5]) + '/5.0', help="Com base no filtro aplicado")

with st.container():
    st.markdown('# Top 10 Restaurantes')
    df1_aux = colunas(df1, False)
    st.dataframe(df1_aux.head(10))

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('## Top 10 Culinárias')
        df1_aux = colunas(df, False)
        df1_aux = (df1_aux.loc[:,['Cuisines', 'Aggregate rating','Country Code']]
                          .groupby(['Cuisines','Aggregate rating'])
                          .nunique()
                          .sort_values('Aggregate rating', ascending=False)
                          .reset_index())

        fig = px.bar(df1_aux.head(10), x='Cuisines', y='Aggregate rating', text_auto=True, labels={'Cuisines':'','Aggregate rating':''})
        st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown('## Top 10 Piores Culinárias')
            df1_aux = colunas(df, True)
            df1_aux = df1_aux.loc[df1_aux['Aggregate rating'] >= 2,:]
    
            fig = px.bar(df1_aux.head(10), x='Cuisines', y='Aggregate rating', text_auto=True, labels={'Cuisines':'','Aggregate rating':''})
            st.plotly_chart(fig, use_container_width=True)
    
    
        

