# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:48:17 2024

@author: PERSONAL
"""
import streamlit as st

st.title("✨Electrónica Digital 2024/2✨")
st.markdown("# El sapito del clima🐸")
st.text("Desarrollo de una mini estación meteorológica mediante un entrenador de ESP32⛰️")

st.sidebar.markdown("# Inicio🐸")

ruta_imagen = "Imagen1.jpg"

try:
    st.image(ruta_imagen, caption="Prototipo funcional", use_column_width=True)
except FileNotFoundError:
    st.error("La imagen no se encuentra en la ruta especificada.")
