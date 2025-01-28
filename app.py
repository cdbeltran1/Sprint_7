#Importar Librerias
import pandas as pd
import streamlit as st
import plotly.express as px


#Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

#Título del reporte
st.header('Relación de variables', divider='gray')


hist_button = st.button('Construir histograma') # crear un botón
disp_button = st.button('Construir gráfico de dispersión') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y='days_listed')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    