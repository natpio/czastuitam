import streamlit as st
from datetime import datetime, time
import pytz

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Rancho Time Rodeo ULTRA PRO",
    page_icon="🤠",
    layout="centered"
)

# --- ARCHITEKTURA DZIKIEGO ZACHODU (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rye&family=Special+Elite&display=swap');

    /* TŁO: Prawdziwa faktura starych, spalonych słońcem desek saloonu */
    .stApp {
        background-color: #3a2212;
        background-image: 
            linear-gradient(90deg, transparent 50%, rgba(255,255,255,.03) 50%),
            linear-gradient(rgba(0,0,0,.4) 50%, transparent 50%),
            linear-gradient(90deg, #4a2c11 0%, #2b1704 100%);
        background-size: 50px 50px, 12px 12px, 100% 100%;
        color: #f4ece1;
        font-family: 'Special Elite', monospace;
    }
    
    /* Naprawiony i podkręcony nagłówek Saloonu */
    .saloon-header {
        font-family: 'Rye', serif;
        color: #ffb703;
        text-align: center;
        font-size: 3.5rem;
        margin-top: -10px;
        margin-bottom: 5px;
        text-shadow: 4px 4px 0px #110700, -2px -2px 0px #8b4513;
        letter-spacing: 4px;
    }
    
    .saloon-sub {
        text-align: center;
        font-size: 1.2rem;
        font-style: italic;
        color: #ddb892;
        letter-spacing: 3px;
        margin-bottom: 40px;
        text-shadow: 1px 1px 2px #000;
    }
    
    /* Główne karty 3D ze skórzanym połyskiem */
    .wood-card {
        background: linear-gradient(135deg, #2b1704 0%, #110700 100%);
        border: 5px double #ffb703;
        border-radius: 8px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 20px 35px rgba(0,0,0,0.8), inset 0px 0px 30px rgba(0,0,0,0.9);
        margin-bottom: 25px;
    }
    
    .wood-title {
        font-family: 'Rye', serif;
        font-size: 1.6rem;
        color: #ffb703;
        letter-spacing: 2px;
        margin-bottom: 15px;
        text-shadow: 2px 2px 3px #000;
    }
    
    /* Zegary Vintage */
    .old-clock {
        font-family: 'Courier New', monospace;
        font-size: 3.5rem;
        font-weight: bold;
        color: #ffb703;
        background: black;
        padding: 15px 5px;
        border-radius: 6px;
        border: 2px dashed #ffb703;
        box-shadow: inset 0px 0px 25px rgba(255,183,3,0.2);
        letter-spacing: 5px;
    }
    
    .wood-date {
        margin-top: 15px;
        color: #b18567;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* BĘBENEK REWOLWERU (Custom Time Picker UI) */
    .revolver-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin: 25px 0;
    }
    
    .cylinder-slot {
        background: radial-gradient(circle, #4a2c11 0%, #110700 100%);
        border: 4px solid #ffb703;
        border-radius: 50px;
        width: 110px;
        padding: 15px 0;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.6), inset 0px 0px 15px #000;
    }
    
    .cylinder-label {
        font-family: 'Rye', serif;
        font-size: 0.9rem;
        color: #ddb892;
        margin-bottom: 8px;
    }
    
    .cylinder-val {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffb703;
        text-shadow: 0px 0px 10px rgba(255,183,3,0.7);
        margin: 10px 0;
        font-family: 'Courier New', monospace;
    }

    /* Guziki Złotego Fortu */
    .stButton>button {
        font-family: 'Rye', serif !important;
        background: linear-gradient(180deg, #ffb703 0%, #fb8500 100%) !important;
        color: #2b1704 !important;
        border: 3px solid #110700 !important;
        border-radius: 4px !important;
        font-size: 1.5rem !important;
        box-shadow: 0px 8px 0px #110700, 0px 15px 25px rgba(0,0,0,0.5);
        width: 100%;
        padding: 12px !important;
        text-transform: uppercase;
    }
    .stButton>button:active {
        transform: translateY(6px);
        box-shadow: 0px 2px 0px #110700;
    }
    
    /* Poprawki tekstu systemowego Streamlit */
    .stRadio p, label {
        color: #f4ece1 !important;
        font-size: 1.2rem !important;
        text-shadow: 2px 2px 2px #000;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIKA STREF CZASOWYCH ---
tz_polska = pytz.timezone('Europe/Warsaw')
tz_iowa = pytz.timezone('US/Central')

now_pl = datetime.now(tz_polska)
now_ia = datetime.now(tz_iowa)

# --- INTERFEJS SALOONU ---
st.markdown("<div class='saloon-header'>🤠 SALOON CHRONO 🌵</div>", unsafe_allow_html=True)
st.markdown("<div class='saloon-sub'>Wersja Legendarna 999. Zbudowana na czystym prochu.</div>", unsafe_allow_html=True)

# Aktualny czas w drewniano-metalowych kartach
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="wood-card">
            <div class="wood-title">🪓 POLSKA</div>
            <div class="old-clock">{now_pl.strftime('%H:%M:%S')}</div>
            <div class="wood-date">📅 {now_pl.strftime('%d.%m.%Y')}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="wood-card">
            <div class="wood-title">🦅 IOWA</div>
            <div class="old-clock">{now_ia.strftime('%H:%M:%S')}</div>
            <div class="wood-date">📅 {now_ia.strftime('%d.%m.%Y')}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- KALKULATOR: MECHANIZM CYLINDRA REWOLWERU ---
st.markdown("<h3 style='font-family:\"Rye\", serif; text-align:center; color:#ffb703; text-shadow: 2px 2px #000;'>🔮 OBRÓĆ BĘBENEK REWOLWERU</h3>", unsafe_allow_html=True)

# Inicjalizacja stanu bębenka w pamięci sesji
if 'bolt_hour' not in st.session_state:
    st.session_state.bolt_hour = int(datetime.now().hour)
if 'bolt_minute' not in st.session_state:
    st.session_state.bolt_minute = int(datetime.now().minute)

# Panel wyboru strefy
wybór = st.radio(
    "Którą strefę bierzesz na celownik, szeryfie?", 
    ("Podaję godzinę w Polsce", "Podaję godzinę w Iowa"),
    horizontal=True
)

# INTERFEJS GRAFICZNEGO BĘBENKA (Przyciski + i -)
st.markdown("<p style='text-align:center; font-style:italic;'>Klikaj strzałki poniżej, by obrócić komory bębenka:</p>", unsafe_allow_html=True)

c_col1, c_col2, c_col3, c_col4 = st.columns([2, 3, 3, 2])

with c_col2:
    # Manipulacja Godzinami
    if st.button("▲", key="h_up"):
        st.session_state.bolt_hour = (st.session_state.bolt_hour + 1) % 24
    
    st.markdown(f"""
        <div class="revolver-container" style="margin:0;">
            <div class="cylinder-slot">
                <div class="cylinder-label">GODZINA</div>
                <div class="cylinder-val">{st.session_state.bolt_hour:02d}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("▼", key="h_down"):
        st.session_state.bolt_hour = (st.session_state.bolt_hour - 1) % 24

with c_col3:
    # Manipulacja Minutami
    if st.button("▲ ", key="m_up"):
        st.session_state.bolt_minute = (st.session_state.bolt_minute + 1) % 60
        
    st.markdown(f"""
        <div class="revolver-container" style="margin:0;">
            <div class="cylinder-slot" style="border-color: #fb8500;">
                <div class="cylinder-label" style="color:#ffb703;">MINUTA</div>
                <div class="cylinder-val" style="color:#fb8500; text-shadow: 0px 0px 10px rgba(251,133,0,0.7);">{st.session_state.bolt_minute:02d}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("▼ ", key="m_down"):
        st.session_state.bolt_minute = (st.session_state.bolt_minute - 1) % 60

# Dopełnienie i główny strzał przelicznika
st.write(" ")
st.write(" ")
fire_trigger = st.button("🔥 WYSTRZEL I PRZELICZ STREFY")

if fire_trigger:
    # Składanie czasu z bębenków
    zbudowany_czas = time(st.session_state.bolt_hour, st.session_state.bolt_minute)
    dzis = datetime.today().date()
    czysta_data_i_czas = datetime.combine(dzis, zbudowany_czas)

    st.markdown("<div class='wood-card' style='border-color:#fb8500;'>", unsafe_allow_html=True)
    
    if wybór == "Podaję godzinę w Polsce":
        pl_dt = tz_polska.localize(czysta_data_i_czas)
        ia_dt = pl_dt.astimezone(tz_iowa)
        
        st.subheader(f"🎯 PL {pl_dt.strftime('%H:%M')} ➔ IOWA {ia_dt.strftime('%H:%M')}")
        if ia_dt.date() == pl_dt.date():
            st.info("🐎 Obie strefy czasowe są tego samego dnia.")
        else:
            st.warning("🪦 W Iowa wciąż trwa WCZORAJSZY DZIEŃ!")
            
    else:
        ia_dt = tz_iowa.localize(czysta_data_i_czas)
        pl_dt = ia_dt.astimezone(tz_polska)
        
        st.subheader(f"🎯 IOWA {ia_dt.strftime('%H:%M')} ➔ PL {pl_dt.strftime('%H:%M')}")
        if pl_dt.date() == ia_dt.date():
            st.info("🐎 Obie strefy czasowe są tego samego dnia.")
        else:
            st.success("🚀 Polska wyprzedza czas i jest już w JUTRZEJSZYM DNIU!")
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- STOPKA ---
st.write("---")
st.markdown("<center style='color:#ffb703; font-family:\"Rye\", serif; font-size:1.1rem;'>🚬 Odlano w stali. Legend Edition v999. Yee-haw!</center>", unsafe_allow_html=True)
