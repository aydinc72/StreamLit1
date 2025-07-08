import streamlit as st
import pandas as pd
 
st.title("Basit Streamlit Uygulamasi")
 
name = st.text_input("Ad girin:")
number = st.slider("sayi seçin:", 0, 100, 50)
 
if st.button("Goster"):
    st.write(f"Merhaba {name},  sayi {number}.")
