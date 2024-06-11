import streamlit as st
import pandas as pd
import numpy as np



st.title("Viajes Uber en Nueva York")

FECHA='date/time'
DATA_URL='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

#Comodín de streamlit para guardar los datos en la caché.
@st.cache_data

def cargarData(nfilas):
    # Leer el archivo CSV desde la URL, cargando solo 'nfilas' filas
    data = pd.read_csv(DATA_URL, nrows=nfilas)
    
    # Definir una función lambda para convertir los nombres de las columnas a minúsculas
    lowercase = lambda x: str(x).lower()
    
    # Renombrar las columnas del DataFrame usando la función lambda
    data.rename(lowercase, axis='columns', inplace=True)
    
    # Convertir la columna de fecha y hora a un objeto datetime
    data[FECHA] = pd.to_datetime(data[FECHA])
    
    # Devolver el DataFrame resultante
    return data


data_load_state=st.text("Cargando datos...")
data=cargarData(1000)
data_load_state.text("Completado")
if st.checkbox("Mostrar datos crudos?"):
    st.subheader('Datos Crudas')
    st.write(data)



#Crear un histograma

st.subheader("Total de viajes por Hora")
valores=np.histogram(data[FECHA].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(valores)


#Crear un mapa
st.subheader("Inicio de los Viajes")
hora=filtrado =st.slider("hour", 0, 23, 17)
17
filtrado=data[data[FECHA].dt.hour==hora]
st.map(filtrado)

