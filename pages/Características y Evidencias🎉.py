# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:20:12 2024

@author: PERSONAL
"""

import streamlit as st

st.sidebar.markdown("# Características y Evidencias🎉")
import streamlit as st

st.title("Características y Evidencias")
st.markdown("### Características del prototipo")
st.text("""
- Controlador: ESP32.
- Sensores: DHT11 (temperatura y humedad),LDR (luminocidad).
- Visualización: Pantalla OLED (128x64 px).
- Transmisión de datos: Wi-Fi con actualización en tiempo real en ThingSpeak.
- Uso eficiente de energía y tamaño compacto.
""")

st.markdown("### Evidencias del prototipo en acción")
st.text("""
Se le realizó una prueba tanto al correcto funcionamiento del entrenador como 
al correcto envíoi de datos en tiempo real detectados por los sensores. 
Para esto, se utilizaron un sensor de metano(MQ-5) y un NRF24L01 para 
verificar el correcto estado de los pines del entrenador. Luego, se colocó
a la ranita en un entorno con un cambio brusco de temperatura y luminocidad para
poder evidenciar su comportamiento.
A continuación, se muestran imágenes del prototipo funcionando,
incluyendo gráficos de datos en tiempo real obtenidos desde ThingSpeak.
""")

ruta_evidencia1 = "evidencia2.jpg"  # Ruta a una imagen de evidencia
ruta_evidencia2 = "evidencia1.jpg"  # Ruta a otra imagen

st.image([ruta_evidencia1, ruta_evidencia2], caption=["Ranita con el sol", 
        "Gráficas en ThingSpeak"], use_column_width=True)


st.title("Enlace para ver el video de evidencia del funcionamiento")

# URL del video
video_url = "https://youtu.be/MvuiFU-0bIk"  # Cambia por tu enlace

# Agregar enlace
st.markdown(f"[Haz clic aquí para ver el video]({video_url})", unsafe_allow_html=True)



