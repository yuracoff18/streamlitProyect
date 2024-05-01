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
    st.write(
    """
    # Piecitos
    Compra al por mayor de zapatos
    """)

    if st.button("Comprar"):
        st.switch_page("pages\compra.py")



if __name__ == "__main__":
    main()