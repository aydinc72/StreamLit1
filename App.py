import streamlit as st
import pandas as pd

st.title("Basit Streamlit Uygulamasi")

name = st.text_input("Ad girin:")
#number = st.slider("sayi secin:", 0, 100, 50)

if st.button("Göster"):
    if name:  # Boş giriş kontrolü
        name_upper = name.upper()

        if name_upper.startswith("AYD"):
            st.write(f"Merhaba süper {name}")
        elif name_upper.startswith("MEL"):
            st.write(f"Merhaba gıcık {name}")
        else:
            st.write(f"Merhaba normal {name}")
    else:
        st.warning("Lütfen bir isim girin.")
