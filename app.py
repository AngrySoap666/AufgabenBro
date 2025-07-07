import streamlit as st
import random
import time

st.markdown("<h1 style='color:hotpink;'>🐢 Larrys Aufgaben-Bro 🐆</h1>", unsafe_allow_html=True)

alle_aufgaben = [
    "Staubsaugen", "Boden Wischen", "Geschirr spülen", "Sofa schicki machen", 
    "Tisch aufräumen und abwischen", "Wäsche waschen", "Müll rausbringen",
    "Dusche putzen", "Bad aufräumen", "Kühlschrank checken", 
    "Schildegard küsschen geben", "Wasser trinken! Wichtig und richtig",
    "Bettchen machen und ggf. neu beziehen", 
    "gönn dir 1 Snacki"
]

if "verbleibende_aufgaben" not in st.session_state:
    st.session_state.verbleibende_aufgaben = alle_aufgaben.copy()

if "start_time" not in st.session_state:
   st.session_state.start_time = 0.0
    

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
        st.session_state.start_time = time.time()
    else:
        st.image("https://media4.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif", caption="🎆DU HAST ALLES GESCHAFFT!!! 💖 Schildegard sagt: CHILL, Baby 💖")
        st.session_state.aktuelle_aufgabe = None

# In Progress
if st.session_state.aktuelle_aufgabe:
    st.markdown("### 🐆 Gerade in Arbeit:")
    st.markdown(f"""
    <div style='
        border: 2px dotted hotpink;
        padding: 20px;
        border-radius: 30px;
        background-image: url("https://i.pinimg.com/originals/43/87/64/4387641dd1cb8c0d62f1d336292e49f7.gif");
        background-size: cover;
        box-shadow: 0 0 10px hot pink, 0 0 20px deeppink, 0 0 30px pink;
        color: deeppink;
        font-weight: bold;
        font-size: 22px;
        text-align: center;
        animation: pulse 1.5s infinite;
    '>    
        <span style='color: #4B0082; font-size: 26px;'>✨ {st.session_state.aktuelle_aufgabe} ✨</span>
        <span style='font-size: 16px; color: #c71585;'>🐆 du machst das mega 💖</span>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.start_time:
        vergangene_zeit = time.time() - st.session_state.start_time
        if vergangene_zeit > 900:
            st.warning("⏰ Du bist schon 15 Minuten am schuften! Willst du eine kleine Rauchi-Pausi machen?")
            
if st.session_state.aktuelle_aufgabe:
    st.markdown("-------------------------")
    if st.button("⏸️ Ich brauch kurz Pause"):
       st.info("🍵Pausenmodus aktiviert. Nimm dir Zeit - du machst das toll!✨")

with st.sidebar:
    if st.session_state.aktuelle_aufgabe:
        if st.button("⏸️ Pause")
            st. info("Kleine Pause eingelegt ☕")

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

