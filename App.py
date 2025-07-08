import streamlit as st
import pandas as pd

st.title("Basit Streamlit Uygulamasi")

name = st.text_input("Ad girin:")
number = st.slider("sayi secin:", 0, 100, 50)

if st.button("Goster"):
    if (name.upper().startswith("AYD")):
        st.write(f"Merhaba super {name}")
    if (name.upper().startswith("MEL")):
        st.write(f"Merhaba gıcık {name}")
    if (not name.upper().startswith("MEL") and not name.upper().startswith("AYD")):
        st.write(f"Merhaba normal {name}")
