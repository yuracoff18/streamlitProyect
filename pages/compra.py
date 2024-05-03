import streamlit as st
from st_pages import *
from tallas import genTalla
from genFacturas import genFactura, genInfo
import os


show_pages([
    Page("__main__.py", "Home"),
    Page("pages/compra.py", "Compra"),
    Page("pages/factura.py", "factura")
])

hide_pages([
    "Home",
    "factura"
    ])

st.write("<div style='text-align:center'><h1>Sección de compra</h1></div>", unsafe_allow_html=True)

nombre = st.text_input("Ingrese su nombre:", value="")
st.text_input("Ingrese su Email:", value="")
st.divider()

modelo = st.selectbox("Modelo de zapato", ('Nike 1', 'Nike 2', 'Nike 3', 'Nike 4'))
medida = st.slider("Medida de su pie (cm): ", 12.0, 19.9, 12.0, 0.1)
if medida:
    st.write(f"Tu talla es: {genTalla(medida)[0]}")
st.divider()

cantidad = st.number_input("Cantidad:", 1, 10, 1, 1)
if cantidad and medida:
    st.write(f"Precio total esperado: {genTalla(medida)[1] * cantidad}")
st.divider()

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("Volver"):
        st.switch_page("__main__.py")
with col3:
    if st.button("Comprar", use_container_width=True):
        genFactura(nombre, cantidad,genTalla(medida)[1], modelo)
        genInfo(nombre, cantidad,genTalla(medida)[1], modelo)
        st.switch_page("pages/factura.py")
        
with col5:
    initial = 0
    dir = "facturas/"
    for i in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,i)):
            initial += 1
    st.write(f"Compras totales: {initial}")
