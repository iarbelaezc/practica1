import streamlit as st 
from PIL import Image 

st.title(" Aplicación de alertas tempranas")

st.header (" En este espacio se podrá obtener información sobre precipitación, calidad del aire y movimientos en masa")

image= Image.open('alertas.png')
st.image(image,caption='Alertas tempranas')
st.write("Enlace para conectar con sensores")
st.write("Ingreas al enlace [link] (https://demo.thingsboard.io/dashboards/221eb150-db1f-11ee-bc03-55147b89654f)")
