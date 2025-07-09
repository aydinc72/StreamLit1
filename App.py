import streamlit as st
import math

st.title("Daire Hesaplama Uygulaması")

# 1. Yarıçap girişi
radius = st.number_input("Dairenin yarı çapını girin:", min_value=0.0, format="%.2f")

# 2. İşlem türü seçimi
calculation_type = st.radio("Hangi işlemi yapmak istersiniz?", ("Alan", "Çevre"))

# 3. Butona basıldığında hesaplama yapılır
if st.button("Göster"):
    if radius == 0:
        st.warning("Yarı çap sıfır olamaz.")
    else:
        if calculation_type == "Alan":
            area = math.pi * radius ** 2
            st.success(f"Dairenin alanı: {area:.2f}")
        else:
            circumference = 2 * math.pi * radius
            st.success(f"Dairenin çevresi: {circumference:.2f}")
