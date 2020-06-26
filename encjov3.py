import streamlit as st
import numpy as np
import pandas as pd
import db_defs



st.title("Encuesta HHJJ Pocuro")

st.header("Junio 2020")

st.write(
    "El Obispado está preocupado que las Actividades para Jóvenes (mutuales) puedan ser lo mas significativas para ustedes. Hemos preparado esta encuesta para tener una mejor vision de lo que necesitamos para que las actividades sean significativas y entretenidas para TODOS")

hombres_jovenes = ['Victor del Canto', 'Mati Sierra', 'Thayko Hernandez', 'Nacho Nuñez', 'Cris Venegas',
                   'Cris Benavente', 'Max Adasme', 'Mateo Palma', 'Benja Adasme', 'Benja Valenzuela ', 'Benja Ramirez']

# cache DataFrame
cache_df = pd.DataFrame(np.zeros((11, 4)), hombres_jovenes, columns=list(range(1, 5)))

joven = st.selectbox("Selecciona tu nombre", hombres_jovenes)


st.header ("1. Deportes no convencionales ")
valor1 = st.slider("Ejemplo : Una clase práctica de voleibol o tenis", 1, 4, 1)

st.header ("2. Cocina ")
valor2 = st.slider("Ejemplo: Aprender a preparar un plato o postre para la familia", 1, 4, 1)

valor3 = st.slider("3. Mutuales Conjuntas", 1, 4, 1)

valor4 = st.slider("4. Paintball", 1, 4, 1)

respuestas = [valor1, valor2, valor3, valor4]

if st.button('Enviar respuestas'):
    db_defs.insert_record(joven, valor1, valor2, valor3, valor4)
    cache_df.loc[joven] = respuestas

st.table(cache_df)

# def add_to_table()
