import streamlit as st
import random

st.markdown("<h1 style='color:hotpink;'>🐢 Larrys Aufgaben-Bro 🐆</h1>", unsafe_allow_html=True)

alle_aufgaben = [
    "Staubsagen", "Boden Wischen", "Geschirr spülen", "Sofa schicki machen", 
    "Tisch aufräumen und abwischen", "Wäsche waschen", "Müll rausbringen",
    "Dusche putzen", "Bad aufräumen", "Kühlschrank checken", 
    "Schildegard küsschen geben", "Wasser trinken! Wichtig und richtig",
    "Bettchen machen und ggf. neu beziehen", "mach 1 kleine Pausi", 
    "Das machst du toll!", "Ich bin stolzi", "ich hab dich lieb", 
    "gönn dir 1 Snacki"
]

if "verbleibende_aufgaben" not in st.session_state:
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()

if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

if "aktuelle_aufgabe" not in st.session_state:
    st.session_state.aktuelle_aufgabe = None

if st.button("🦩 Welche Aufgabe soll ich machen? 🦩"):
    if st.session_state.aktuelle_aufgabe:
        st.session_state.verlauf.append(st.session_state.aktuelle_aufgabe)

    if st.session_state.verbleibende_aufgaben:
        neue_aufgabe = random.choice(st.session_state.verbleibende_aufgaben)
        st.session_state.verbleibende_aufgaben.remove(neue_aufgabe)
        st.session_state.aktuelle_aufgabe = neue_aufgabe
    else:
        st.balloons()
        st.image("https://media.giphy.com/media/YOX5DJzV6TfI7dAfxh/giphy.gif", caption="💖 Schildegard sagt: CHILL, Baby 💖")
        st.session_state.aktuelle_aufgabe = None

# In Progress
if st.session_state.aktuelle_aufgabe:
    st.markdown("### 🐆 Gerade in Arbeit:")
    st.info(f"🚧 **{st.session_state.aktuelle_aufgabe}**")

# Erledigt
if st.session_state.verlauf:
    st.markdown("### 🐢 Was du schon geschafft hast:")
    for erledigt in st.session_state.verlauf:
        st.markdown(f"🩷 ✅ **{erledigt}** 🐆")

# Reset
if st.button("🔄 Neustarten"):
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()
    st.session_state.verlauf = []
    st.session_state.aktuelle_aufgabe = None
    st.success("💅 Aufgaben wurden zurückgesetzt, du wildes Faultier 🦥💕")

