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

#-------------------------------- Inicio da Estrutura lógica do código --------------------------------
df = pd.read_csv('dataset/zomato.csv.zip')
df1 = df.copy()

df1 = clear_code(df1)
df = df1.copy()

st.set_page_config(
    page_title="🌃 Citys",
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

country_unique = df1['City'].unique()

qtd_country = st.sidebar.slider('Quantos paises deseja ver?',min_value=0,max_value=len(country_unique))

if qtd_country < 6:
    qtd_country = 6

country = st.sidebar.multiselect('Escolha o país que deseja filtrar',
                                country_unique,
                                default=country_unique[0:qtd_country])

selecao = df1['City'].isin(country)
df1 = df1.loc[selecao,:]

#==================================
# Main Page
#==================================
st.markdown('# Visão Cidades')

with st.container():
    st.markdown('### Número de restaurantes por cidade')
    df_aux = (df1.loc[:,['City','Restaurant Name']]
             .groupby(['City'])
             .nunique()
             .sort_values('Restaurant Name', ascending=False)
             .reset_index())
    
    fig = px.bar(df_aux, x='City', y='Restaurant Name', text_auto=True, labels={'City':'', 'Restaurant Name':''})
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""---""")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Top 7 cidades com nota > 4')
        df_aux = df.loc[df['Aggregate rating'] >= 4,:]
        df_aux = (df_aux.loc[:,['City','Restaurant Name']]
                .groupby(['City'])
                .nunique()
                .sort_values('Restaurant Name', ascending=False)
                .reset_index())
        df_aux = df_aux.loc[0:6,:]
        
        fig = px.bar(df_aux, x='City', y='Restaurant Name', text_auto=True, labels={'City':'','Restaurant Name':''})
        st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown('### Top 7 cidades com nota < 2,5')
            df_aux = df.loc[df['Aggregate rating'] < 2.5,:]
            df_aux = (df_aux.loc[:,['City','Restaurant Name']]
                    .groupby(['City'])
                    .nunique()
                    .sort_values('Restaurant Name', ascending=False)
                    .reset_index())
            df_aux = df_aux.loc[0:6,:]
            
            fig = px.bar(df_aux, x='City', y='Restaurant Name', text_auto=True, labels={'City':'','Restaurant Name':''})
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("""---""")

with st.container():
    st.markdown('### Top 10 cidades com mais variedade de culinária')
    df_aux = (df.loc[:,['City','Cuisines']]
                 .groupby(['City'])
                 .nunique()
                 .sort_values('Cuisines', ascending=False)
                 .reset_index())
    
    df_aux = df_aux.loc[0:10,:]
    
    fig = px.bar(df_aux, x='City', y='Cuisines', text_auto=True, labels={'City':'','Cuisines':''})
    st.plotly_chart(fig, use_container_width=True)

