# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:44:50 2024

@author: PERSONAL
"""

import streamlit as st

st.sidebar.markdown("# Links🔗 y Explicación🤯")
import streamlit as st

st.title("Links🔗 y Explicación🤯")
st.markdown("### Repositorio de GitHub")
st.text("Link para que accedas al repositorio de GITHUB por si quieres replicar tu propio sapito del clima")
# URL del video
video_url1 = " https://github.com/SaraNu0720/El-sapito-del-clima"  # Cambia por tu enlace

# Agregar enlace
st.markdown(f"[Haz clic aquí para ir al repositorio]({video_url1})", unsafe_allow_html=True)

st.markdown("### Video funcionamiento final ")
# URL del video
video_url2 = " https://youtube.com/shorts/RFTrdXMv6sc?feature=share"  # Cambia por tu enlace

# Agregar enlace
st.markdown(f"[Haz clic aquí para ver el video]({video_url2})", unsafe_allow_html=True)


