import streamlit as st
from datetime import datetime, timedelta
import pytz

# --- KONFIGURACJA STRONY (ZŁOTY REWOLWER) ---
st.set_page_config(
    page_title="Rancho Time Rodeo",
    page_icon="🌵",
    layout="centered"
)

# --- PEŁNY SZPAN: ULTRA STYLIZACJA WESTERN (CSS) ---
st.markdown("""
    <style>
    /* Tło całej aplikacji - stary, zakurzony pergamin / piasek */
    .stApp {
        background-color: #e6ccb2;
        color: #3d2314;
        font-family: 'Georgia', 'Courier New', serif;
    }
    
    /* Główne nagłówki stylizowane na napisy z Saloonu */
    h1, h2, h3 {
        color: #5c3a21 !important;
        font-family: 'Impact', 'Georgia', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 2px 2px 0px #b18567, 4px 4px 0px #3d2314;
        text-align: center;
    }
    
    /* Karty z czasem - wyglądają jak stare, drewniane deski obite skórą */
    .wood-card {
        background-color: #7f5539;
        border: 4px solid #4a2c11;
        border-radius: 4px;
        padding: 25px;
        text-align: center;
        box-shadow: inset 0px 0px 15px rgba(0,0,0,0.6), 8px 8px 0px #3d2314;
        margin-bottom: 25px;
    }
    
    .wood-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #ede0d4;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 10px;
        border-bottom: 2px dashed #9c6644;
        padding-bottom: 5px;
    }
    
    /* Wygląd STAREGO ZEGRU (Wypalone cyfry) */
    .old-clock {
        font-family: 'Courier New', monospace;
        font-size: 2.8rem;
        font-weight: bold;
        color: #ffb703;
        background-color: #2b1704;
        padding: 12px;
        border-radius: 3px;
        border: 2px solid #b18567;
        box-shadow: inset 0px 0px 10px rgba(0,0,0,0.9);
        letter-spacing: 3px;
    }
    
    .wood-date {
        margin-top: 12px;
        color: #ddb892;
        font-size: 1.1rem;
        font-weight: bold;
        font-style: italic;
    }

    /* Banery informacyjne o dacie */
    .date-same {
        background-color: #606c38 !important;
        color: #fefae0 !important;
        border: 2px solid #283618;
        padding: 10px;
        border-radius: 4px;
        text-align: center;
        font-weight: bold;
    }
    
    .date-yesterday {
        background-color: #bc6c25 !important;
        color: #fefae0 !important;
        border: 2px solid #dda15e;
        padding: 10px;
        border-radius: 4px;
        text-align: center;
        font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }

    /* Kowbojski przycisk */
    .stButton>button {
        background-color: #4a2c11 !important;
        color: #ffb703 !important;
        border: 3px solid #ffb703 !important;
        border-radius: 0px !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        text-transform: uppercase;
        box-shadow: 5px 5px 0px #3d2314;
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #ffb703 !important;
        color: #4a2c11 !important;
        box-shadow: 2px 2px 0px #3d2314;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIKA STREF CZASOWYCH ---
tz_polska = pytz.timezone('Europe/Warsaw')
tz_iowa = pytz.timezone('US/Central')

now_pl = datetime.now(tz_polska)
now_ia = datetime.now(tz_iowa)

# --- INTERFEJS SALOONU ---
st.markdown("<h1>🤠 SALOON TIME CHRONO 🌵</h1>")
st.markdown("<p style='text-align:center; font-style:italic; color:#5c3a21;'>Najszybszy zegar po tej stronie rzeki Missisipi</p>", unsafe_allow_html=True)
st.write("---")

# Aktualny stary zegar w drewnianych kartach
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="wood-card">
            <div class="wood-title">🪓 POLSKA (Warszawa)</div>
            <div class="old-clock">{now_pl.strftime('%H:%M:%S')}</div>
            <div class="wood-date">📅 {now_pl.strftime('%d.%m.%Y')}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="wood-card">
            <div class="wood-title">🦅 IOWA (Rancho)</div>
            <div class="old-clock">{now_ia.strftime('%H:%M:%S')}</div>
            <div class="wood-date">📅 {now_ia.strftime('%d.%m.%Y')}</div>
        </div>
    """, unsafe_allow_html=True)

# --- ANALIZA DROGI W CZASIE (CZY TO TA SAMA DATA?) ---
st.write(" ")
if now_pl.date() == now_ia.date():
    st.markdown('<div class="date-same">🐎 STAN DROGI: Wszyscy jedziemy na tym samym wozie! (Ta sama data w PL i Iowa)</div>', unsafe_allow_html=True)
elif now_ia.date() < now_pl.date():
    st.markdown('<div class="date-yesterday">🪦 UWAGA: Iowa zostaje w tyle! Rancho żyje jeszcze WCZORAJSZYM DNIEM.</div>', unsafe_allow_html=True)

st.write("---")

# --- KALKULATOR Z LASSO (FORMULARZ) ---
st.markdown("<h3>🌵 Złap czas na lasso</h3>")

if 'saved_time' not in st.session_state:
    st.session_state.saved_time = datetime.now().time()

with st.form(key='cowboy_form'):
    wybór = st.radio(
        "Gdzie ustawiasz wskazówki, szeryfie?", 
        ("Podaję godzinę w Polsce", "Podaję godzinę w Iowa")
    )
    
    wybrany_czas = st.time_input("Ustaw mechanizm starego zegara:", value=st.session_state.saved_time)
    
    submit_button = st.form_submit_button(label='🔥 PRZELICZ I WYSTRZEL')

# Obliczenia po pociągnięciu za spust
if submit_button:
    st.session_state.saved_time = wybrany_czas
    dzis = datetime.today().date()
    czysta_data_i_czas = datetime.combine(dzis, wybrany_czas)

    if wybór == "Podaję godzinę w Polsce":
        pl_dt = tz_polska.localize(czysta_data_i_czas)
        ia_dt = pl_dt.astimezone(tz_iowa)
        
        st.write("---")
        st.info(f"🎯 Gdy w Polsce bije **{pl_dt.strftime('%H:%M')}**, w Iowa jest **{ia_dt.strftime('%H:%M')}**.")
        
        # Porównanie dat dla wybranego czasu
        if ia_dt.date() == pl_dt.date():
            st.markdown('`🐎 Wybrany czas wypada tego samego dnia w obu miejscach.`')
        elif ia_dt.date() < pl_dt.date():
            st.markdown('`🪦 Wybrany czas oznacza, że w Iowa cofamy się do WCZORAJSZEGO DNIA!`')
            
    else:
        ia_dt = tz_iowa.localize(czysta_data_i_czas)
        pl_dt = ia_dt.astimezone(tz_polska)
        
        st.write("---")
        st.info(f"🎯 Gdy w Iowa wybije **{ia_dt.strftime('%H:%M')}**, w Polsce zegary pokazują już **{pl_dt.strftime('%H:%M')}**.")
        
        # Porównanie dat dla wybranego czasu
        if pl_dt.date() == ia_dt.date():
            st.markdown('`🐎 Wybrany czas wypada tego samego dnia w obu miejscach.`')
        elif pl_dt.date() > ia_dt.date():
            st.markdown('`🚀 Gdy w Iowa trwa ten moment, w Polsce kowboje są już w JUTRZEJSZYM DNIU!`')

# --- STOPKA Z SALOONU ---
st.write("---")
st.markdown("<center style='color:#5c3a21; font-weight:bold;'>🚬 Opracowano na dzikim rancho. Nie strzelać do pianisty. </center>", unsafe_allow_html=True)
