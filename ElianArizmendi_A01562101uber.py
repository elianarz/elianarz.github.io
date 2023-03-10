import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber en New York City')

DATE_COLUMN = 'date/time'
DATA_URL = ('uber-raw-data-sep14.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Cargando datos...')
data = load_data(1000000)
data_load_state.text("Se logró cargar todo con éxito! (using st.cache)")

st.dataframe(data)

# Some number in the range 0-23
hour_to_filter = st.slider('HORA', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de todos los servicios de Uber a las %s:00 horas en New York City' % hour_to_filter)
st.map(filtered_data) 