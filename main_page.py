#Importando as bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import folium as fl

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

#-------------------------------- Inicio da Estrutura lógica do código --------------------------------
df = pd.read_csv('dataset/zomato.csv.zip')
df1 = df.copy()

df1 = clear_code(df1)

st.set_page_config(
    page_title="🥡 Page Main",
    layout='wide'   
)

#==================================
# Barra Lateral Streamlit
#==================================
image = Image.open('logo.png')
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

#==================================
# Main Page
#==================================

with st.container():
    st.markdown('# Fome Zero')
    st.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito!')
    st.markdown('### Conheça os nosso números:')

with st.container():
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        restaurant_unique = '{:,}'.format(len(df1.loc[:,'Restaurant ID'].unique())).replace(',','.')
        col1.metric('Total Restaurantes', restaurant_unique, help="Total de restaurantes com base no filtro aplicado")

    with col2:
        country_unique = len(df1.loc[:,'Country Code'].unique())
        col2.metric('Total Paises', country_unique, help="Total de paises com base no filtro aplicado")

    with col3:
        city_unique = len(df1.loc[:,'City'].unique())
        col3.metric('Total Cidades', city_unique, help="Total de cidades com base no filtro aplicado")

    with col4:
        cuisines_unique = len(df1.loc[:,'Cuisines'].unique())
        col4.metric('Tipos de Culinárias',cuisines_unique, help="Tipos de culinárias diferentes com base no filtro aplicado")
    
    with col5:
        sum_rating = '{:,}'.format(sum(df1.loc[:,'Votes'])).replace(',','.')
        col5.metric('Total Avaliações',sum_rating, help="Total de votos com base no filtro aplicado")

    with col6:
        mean_rating = '{:,.2f}'.format(df1.loc[:,'Aggregate rating'].mean()).replace('.',',')
        col6.metric('Média das Avaliações',mean_rating + '/5,0', help="Media da avaliação dos restaurantes com base no filtro aplicado. Nota máxima 5,0")
        

with st.container():
    df_aux = (df1.loc[:,['Latitude','Longitude','Restaurant Name', 'Restaurant ID','Rating color','Cuisines','Aggregate rating','Average Cost for two','Currency']]
                 .groupby(['Restaurant Name','Latitude','Longitude','Rating color','Cuisines','Aggregate rating','Average Cost for two','Currency'])
                 .nunique()
                 .reset_index())
    
    map = fl.Map()
    marker_cluster = fl.plugins.MarkerCluster().add_to(map)
    
    for index, location_index in df_aux.iterrows():
        icone = fl.Icon(color=location_index['Rating color'])
        latitude = location_index['Latitude']
        longitude = location_index['Longitude']
        pop_up = f'<div style="width: 250px;">' \
                 f"<b>{location_index['Restaurant Name']}</b><br><br>" \
                 f" Type: {location_index['Cuisines']} <br>" \
                 f" Preço Para Dois: {location_index['Average Cost for two']:.2f} ({location_index['Currency']})<br>" \
                 f" Nota: {location_index['Aggregate rating']}/5.0 <br>" \
                 f'</div>'
        
        fl.Marker([latitude,longitude], zoom_start=15, popup=pop_up, icon=icone).add_to(marker_cluster)
        #FastMarkerCluster([latitude,longitude]).add_top(map)
    
    folium_static(map, width=864, height=486)
    
