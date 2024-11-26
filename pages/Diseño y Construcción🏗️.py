# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:17:40 2024

@author: PERSONAL
"""

import streamlit as st

st.sidebar.markdown("# Diseño💻 y Construcción🏗️")
import streamlit as st

st.title("Diseño💻 y Construcción🏗️")
st.markdown("### Descripción del prototipo")
st.text("""
El prototipo consiste en un entrenador ESP32 con sensores para medir
variables meteorológicas como temperatura, humedad, y la luminocidad.
Los datos se visualizan en tiempo real en una pantalla OLED y se suben
a la plataforma ThingSpeak, donde se visualizan de manera gráfica los 
cambios detectados por cada sensor.
El prototipo aborda la falta de herramientas asequibles para el monitoreo 
ambiental en zonas remotas con conectividad limitada, su función principal 
es recopilar datos de variables atmosféricas (temperatura, humedad, gases 
y luz) en tiempo real, utilizando sensores integrados y módulos de
 comunicación inalámbrica NRF, estos datos son enviados a una plataforma 
 web para su análisis y posterior monitoreo para la toma de decisiones.

Sector de aplicación:

•	Agricultura: Monitorización de condiciones ambientales para 
optimizar cultivos.
•	Medioambiente: Vigilancia de niveles de gases y condiciones climáticas.
•	Industria: Evaluación de calidad del aire en entornos operativos.

""")

st.markdown("### Diseño esquemático")
st.text("""
El diseño incluye:
- Un ESP32 como controlador principal.
- Sensores como DHT11 (temperatura y humedad) y LDR (luminocidad).
- Pantalla OLED para visualizar los datos localmente.
- Plataforma ThingSpeak para gráficos en tiempo real.
""")

ruta_diseno = "diseño.png"  # Reemplaza por la ruta de tu imagen
if st.button("Ver diseño"):
    st.image(ruta_diseno, caption="Diseño del prototipo", use_column_width=True)

st.markdown("### Diseño de la ranita")
st.text("""
El diseño incluye:
- Lugar adecuado para posicionar la PCB con los sensores y componentes
- Cavidad interna para guardar las basterías
- Diseño creativo y acorde al conexto
""")

ruta_diseno = "planos.png"  # Reemplaza por la ruta de tu imagen
if st.button("Ver planos"):
    st.image(ruta_diseno, caption="Planos del prototipo", use_column_width=True)
    
st.markdown("### Proceso de construcción")
st.text("""
Componentes y elementos principales:

1.	Microcontroladores (ESP32):
    
•	Coordina la operación de sensores y la transmisión de datos.
•	Ejecuta los algoritmos para la comunicación entre receptor y emisor.

2.	Módulos NRF:
    
•	Sustituyen a los módulos LoRa, que fueron previamente establecidos 
como el sistema de comunicación para este proyecto y posteriormente
 remplazados debido a problemas de alcance.
•	Facilitan la comunicación inalámbrica en distancias moderadas.

3.	Sensores:
    
•	DHT11: Mide temperatura y humedad.
•	MQ5: Detecta gases inflamables como metano.
•	KY-018: Detecta la intensidad lumínica.

4.	Carcasa Protectora:
    
•	Material: Plástico ABS.
•	Propiedades: Resistente, ligero y aislante, protege los circuitos 
frente a polvo, agua y golpes.

5.	PCB (Placa de Circuito Impreso):
    
•	Diseñada para organizar y soldar los componentes electrónicos, 
reduciendo errores de conexión y mejora la estabilidad eléctrica.

Proceso de construcción:

Con la lista de materiales definida, se inició el diseño de las carcasas
 y la PCB, lo cual incluyó simulaciones detalladas para optimizar el 
 ensamblaje como se observan en los anexos, tras la adquisición de los 
 componentes y el previo proceso de diseño y simulación se realizaron
 pruebas preliminares en protoboard, utilizando los códigos desarrollados
 específicamente para el proyecto, estas pruebas garantizaron la 
 funcionalidad antes de soldar los componentes en la PCB y ensamblar
 el dispositivo en su carcasa protectora.
El prototipo final, completamente operativo, demostrando su viabilidad
 como solución práctica para el monitoreo ambiental remoto usando
 herramientas de bajo costo.


""")

ruta_proceso = "proceso1.jpg"  # Reemplaza por la ruta de tu imagen
st.image(ruta_proceso, caption="Carcasa protectora Ranita en impresión", use_column_width=True)

ruta_proceso = "proceso2.jpg"  # Reemplaza por la ruta de tu imagen
st.image(ruta_proceso, caption="Evidencia de la soldadura de los componentes a la PCB previamente diseñada", use_column_width=True)

