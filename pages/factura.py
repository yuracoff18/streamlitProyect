import streamlit as st
from st_pages import *
from datetime import date
from datetime import datetime
import os

show_pages([
    Page("__main__.py", "Home"),
    Page("pages/compra.py", "Compra"),
    Page("pages/factura.py", "factura")
])

hide_pages([
    "Home",
    "Compra"
    ])

st.success("Su compra se ha realizado con exito")

with open("actual_info/info.txt", "r") as arch:
    info = arch.read()
    info = info.split(",")
    precio = int(info[2])
    cantidad = int(info[1])
    st.write(f"""
<div style='text-align:center'><h1>Factura</h1>

**Empresa: Piecitos**


**Fecha: {date.today()}**  
**Hora: {datetime.now().hour}:{datetime.now().minute}**  


**Nombre: {info[0]}**    
**Cantidad: {info[1]}**  
**Modelo: {info[3]}**  


**Valor unitario: {precio}**  
**Valor sin IVA: {precio*cantidad}**  
**Valor total: {(precio*cantidad) + ((precio*cantidad)* 0.19)}**</div>
    """, unsafe_allow_html=True)

m1,m2,m3,m4,m5 = st.columns(5)
with m3:
    if st.button("Volver", use_container_width=True):
       st.switch_page("__main__.py")