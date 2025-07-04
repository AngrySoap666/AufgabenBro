import streamlit as st
import random

st.title("Aufgaben-Bro")

alle_aufgaben = [
    "Staubsagen", "Boden Wischen", "Geschirr spülen", "Sofa schicki machen", "Tisch aufräumen und abwischen", "Wäsche waschen", "Müll rausbringen",
    "Dusche putzen", "Bad aufräumen", "Kühlschrank checken", "Schildegard küsschen geben", "Wasser trinken! Wichtig und richtig",
    "Bettchen machen und ggf. neu beziehen", "mach 1 kleine Pausi", "Das machst du toll!", "Ich bin stolzi", "ich hab dich lieb", "gönn dir 1 Snacki"
    ]

if "verbleibende_aufgaben" not in st.session_state:
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()

if st.button("Welche Aufgabe soll ich machen?"):
    if st.session_state.verbleibende_aufgaben:
        aufgabe = random.choice(st.session_state.verbleibende_aufgaben)
        st.session_state.verbleibende_aufgaben.remove(aufgabe)
        st.success(f"Deine Aufgabe: **{aufgabe}**")

    else:
        st.balloons()
        st.info("Alle Aufgaben geschafft! Jetzt kannst du chillen und deine Eierstöcke schaukeln.")

if st.button("Neustarten") :
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()
    st.info("Liste wurde zurückgesetzt")
    
