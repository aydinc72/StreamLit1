import streamlit as st
import pandas as pd
 
st.title("Basit Streamlit Uygulaması")
 
name = st.text_input("Adınızı girin:")
number = st.slider("Bir sayı seçin:", 0, 100, 50)
 
if st.button("Göster"):
    st.write(f"Merhaba {name}, seçtiğin sayı {number}.")
