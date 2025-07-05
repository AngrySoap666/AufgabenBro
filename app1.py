import streamlit as st
import random

st.title("Aufgaben-Bro")

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

# Initialisierung
if "verbleibende_aufgaben" not in st.session_state:
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()

if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

# Button: Aufgabe anzeigen
if st.button("Welche Aufgabe soll ich machen?"):
    if st.session_state.verbleibende_aufgaben:
        aufgabe = random.choice(st.session_state.verbleibende_aufgaben)
        st.session_state.verbleibende_aufgaben.remove(aufgabe)
        st.session_state.verlauf.append(aufgabe)
    else:
        st.image("https://media4.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif", caption="🎆DU HAST ALLES GESCHAFFT!!!")
        st.info("Alle Aufgaben geschafft! Jetzt kannst du chillen und deine Eierstöcke schaukeln.")

# Fortschrittsanzeige
if st.session_state.verlauf:
    st.subheader("Was du schon geschafft hast:")
    for aufgabe in st.session_state.verlauf:
        st.markdown(f"✅ **{aufgabe}**")

# Button: Zurücksetzen
if st.button("Neustarten"):
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()
    st.session_state.verlauf = []
    st.info("Liste wurde zurückgesetzt.")

# Footer
st.markdown("---")
st.markdown("<small style='color:gray;'>Programm für Larry Barry von Mexy 💻💜</small>", unsafe_allow_html=True)
