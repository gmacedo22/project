import pandas as pd
import streamlit as st
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("Catalgo de Carros USA")
print()
hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button(
    'Construir un diagrama de dispersión')  # Crear botón
if scatter_button:
    # Escribir mensaje
    st.write('Creación de un diagrama de dispersión')
    # Creacion de diagrama de dispersion
    fig1 = px.scatter(car_data, x="model_year", y="price", color="type")
    # monstrar el diagrama
    st.plotly_chart(fig1, use_container_width=True)
# Ejemplo de Checkbox

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    # Mensaje
    st.write('Construir un histograma para la columna odómetro')
    # Creacion de Histograma
    fig2 = px.histogram(car_data, x='days_listed')
    # Monstrar el histograma
    st.plotly_chart(fig2, use_container_width=True)
