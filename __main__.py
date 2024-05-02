import streamlit as st
from st_pages import *

show_pages([
    Page("__main__.py", "Home"),
    Page("pages\compra.py", "Compra")
])

hide_pages([
    "Compra"
    
    ])

def main():
    st.image("multimedia\Logo.jpg", use_column_width=True)
    st.write("<div style='text-align:center'><h1>Piecitos</h1></div>", unsafe_allow_html=True)
    st.write("<div style='text-align:center'><h2>Venta de zapatos</h2></div>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("multimedia\zapato1.png", caption="Nike 1")
        st.image("multimedia\zapato2.png", caption="Nike 2")
        
    with col2:
        st.image("multimedia\zapato3.png", caption="Nike 3")
        st.image("multimedia\zapato4.png", caption="Nike 4")
        
    st.divider()
    
    div1, div2, div3, div4, div5 = st.columns(5)
    with div3:
        if st.button("Comprar", use_container_width=True):
            st.switch_page("pages\compra.py")

if __name__ == "__main__":
    main()