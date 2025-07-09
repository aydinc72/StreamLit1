import streamlit as st
import random

# ✅ Gizli sayı oluşturma fonksiyonu
def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)
    # İlk rakam 0 olmasın
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(digits[:4])

# ✅ Değerlendirme fonksiyonu
def evaluate_guess(secret, guess):
    correct_place = sum(s == g for s, g in zip(secret, guess))
    correct_digit = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    wrong_place = correct_digit - correct_place
    return correct_place, wrong_place

# ✅ Session state başlatma
if 'secret' not in st.session_state:
    st.session_state.secret = generate_secret_number()
    st.session_state.attempts = 0
    st.session_state.found = False
    st.session_state.history = []

st.title("🔢 4 Haneli Gizli Sayıyı Tahmin Et")

# ✅ Kullanıcıdan giriş al
user_input = st.text_input("4 haneli, rakamları farklı bir sayı girin:")

if st.button("Tahmin Et") and not st.session_state.found:
    if not user_input.isdigit() or len(user_input) != 4 or len(set(user_input)) != 4:
        st.warning("Lütfen 4 haneli ve rakamları farklı bir sayı girin.")
    else:
        st.session_state.attempts += 1
        correct_place, wrong_place = evaluate_guess(st.session_state.secret, user_input)

        # Geçmişe ekle
        st.session_state.history.append(
            (user_input, correct_place, wrong_place)
        )

        # Sonuç
        if correct_place == 4:
            st.success(f"🎉 Tebrikler! Doğru tahmin: {user_input}")
            st.info(f"{st.session_state.attempts} denemede bildiniz.")
            st.session_state.found = True
        else:
            st.info(f"✅ {correct_place} doğru yerde, 🔄 {wrong_place} yanlış yerde.")

# ✅ Geçmiş tahminleri göster
if st.session_state.history:
    st.subheader("🕓 Önceki Tahminler:")
    for idx, (g, cp, wp) in enumerate(st.session_state.history, 1):
        st.write(f"{idx}. Tahmin: {g} → ✅ {cp} doğru yerde, 🔄 {wp} yanlış yerde")

# ✅ Oyunu sıfırlama
if st.button("🔄 Yeni Oyun"):
    st.session_state.secret = generate_secret_number()
    st.session_state.attempts = 0
    st.session_state.found = False
    st.session_state.history = []
    st.success("Yeni oyun başlatıldı!")

