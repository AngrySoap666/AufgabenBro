import streamlit as st
import random

st.title("🧼 Aufgaben-Bro für Larry 🧼")

# Bunter Header
st.markdown("<h3 style='color:#6A1B9A;'>Los geht's mit den Aufgaben! 💪</h3>", unsafe_allow_html=True)

alle_aufgaben = [
    "Staubsaugen 🧹",
    "Boden wischen 🧽",
    "Geschirr spülen 🍽️",
    "Sofa schicki machen 🛋️",
    "Tisch aufräumen und abwischen 🧴",
    "Wäsche waschen 🧺",
    "Müll rausbringen 🗑️",
    "Dusche putzen 🚿",
    "Bad aufräumen 🛁",
    "Kühlschrank checken 🧊",
    "Schildegard Küsschen geben 😘",
    "Wasser trinken! Wichtig und richtig 💧",
    "Bettchen machen und ggf. neu beziehen 🛏️",
    "Mach 1 kleine Pausi ☕",
    "Das machst du toll! 👏",
    "Ich bin stolzi 😎",
    "Ich hab dich lieb ❤️",
    "Gönn dir 1 Snacki 🍪"
]

if "verbleibende_aufgaben" not in st.session_state:
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()

if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

gesamt = len(alle_aufgaben)
verbleibend = len(st.session_state. verbleibende_aufgaben)
erledigt = gesamt - verbleibend
fortschritt = erledigt / gesamt

st.progress(fortschritt)

col1, col2 = st.columns(2)

with col1:
    if st.button("Welche Aufgabe soll ich machen?"):
        if st.session_state.verbleibende_aufgaben:
            aufgabe = random.choice(st.session_state.verbleibende_aufgaben)
            st.session_state.verbleibende_aufgaben.remove(aufgabe)
            st.success(f"✨ Deine Aufgabe: **{aufgabe}**")
        else:
            st.image("https://media4.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif", caption="🎆DU HAST ALLES GESCHAFFT!!!")
            st.info("🎉 Alle Aufgaben geschafft! Jetzt kannst du chillen und deine Eierstöcke schaukeln. 🥳")

if st.session_state.verlauf:
    st.subheader("Was du schon geschafft hast:")
    for aufgabe in st.session_state.verlauf:
        st.markdown(f"✅ **{aufgabe}**")

with col2:
    if st.button("Neustarten"):
        st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()
        st.info("🔄 Liste wurde zurückgesetzt")

# Footer
st.markdown("---")
st.markdown("<small style='color:gray;'>Programm für Larry Barry von Mexy 💻💜</small>", unsafe_allow_html=True)
