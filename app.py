import streamlit as st
from datetime import datetime, time
import pytz

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Rancho Time Rodeo PRO",
    page_icon="🌵",
    layout="centered"
)

# --- LEVEL 999 PRO: KINOWY STYL WESTERN + MODYFIKACJA SLIDERÓW ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rye&family=Special+Elite&display=swap');

    .stApp {
        background: radial-gradient(circle, #e6ccb2 0%, #b18567 100%);
        color: #3d2314;
        font-family: 'Special Elite', monospace;
    }
    
    .saloon-header {
        font-family: 'Rye', serif;
        color: #4a2c11;
        text-align: center;
        font-size: 3rem;
        margin-top: -20px;
        margin-bottom: 5px;
        text-shadow: 3px 3px 0px #ffb703, 5px 5px 0px #2b1704;
        line-height: 1.2;
    }
    
    .saloon-sub {
        text-align: center;
        font-size: 1.1rem;
        font-style: italic;
        color: #5c3a21;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    
    .wood-card {
        background: linear-gradient(135deg, #6c584c 0%, #4a3728 100%);
        border: 4px solid #2b1704;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 15px 25px rgba(0,0,0,0.5), inset 0px 0px 20px rgba(0,0,0,0.4);
        margin-bottom: 25px;
        transform: perspective(500px) rotateX(2deg);
    }
    
    .wood-title {
        font-family: 'Rye', serif;
        font-size: 1.5rem;
        color: #ffb703;
        letter-spacing: 2px;
        margin-bottom: 15px;
        text-shadow: 2px 2px 0px #000;
    }
    
    .old-clock {
        font-family: 'Courier New', monospace;
        font-size: 3.2rem;
        font-weight: bold;
        color: #ffb703;
        background: radial-gradient(circle, #2b1704 0%, #110700 100%);
        padding: 15px 10px;
        border-radius: 8px;
        border: 3px solid #b18567;
        box-shadow: inset 0px 0px 20px rgba(0,0,0,1), 0px 0px 15px rgba(255,183,3,0.3);
        letter-spacing: 4px;
    }
    
    .wood-date {
        margin-top: 15px;
        color: #ddb892;
        font-size: 1.2rem;
        letter-spacing: 1px;
    }

    .date-same {
        background: linear-gradient(90deg, #556b2f, #6b8e23);
        color: #fefae0 !important;
        border: 2px solid #283618;
        padding: 12px;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    }
    
    .date-yesterday {
        background: linear-gradient(90deg, #bc6c25, #9a5316);
        color: #fefae0 !important;
        border: 2px solid #5c3a21;
        padding: 12px;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
    }

    /* Guzik - Czyste złoto z Fortu Knox */
    .stButton>button {
        font-family: 'Rye', serif !important;
        background: linear-gradient(180deg, #ffb703 0%, #fb8500 100%) !important;
        color: #2b1704 !important;
        border: 3px solid #2b1704 !important;
        border-radius: 6px !important;
        font-size: 1.4rem !important;
        box-shadow: 0px 6px 0px #2b1704, 0px 10px 20px rgba(0,0,0,0.3);
        width: 100%;
        transition: all 0.1s ease;
        padding: 10px !important;
    }
    .stButton>button:active {
        transform: translateY(4px);
        box-shadow: 0px 2px 0px #2b1704;
    }
    
    /* STYLIZACJA KOWBOJSKICH SLIDERÓW (STREFA AKTYWNA) */
    div[data-baseweb="slider"] [role="progressbar"] {
        background-color: #8b4513 !important;
    }
    /* Kolor suwaka (kulka/nabój) */
    div[data-baseweb="slider"] [thumbvalue] {
        background-color: #ffb703 !important;
        border: 3px solid #2b1704 !important;
    }
    
    label, .stRadio p {
        color: #2b1704 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIKA STREF CZASOWYCH ---
tz_polska = pytz.timezone('Europe/Warsaw')
tz_iowa = pytz.timezone('US/Central')

now_pl = datetime.now(tz_polska)
now_ia = datetime.now(tz_iowa)

# --- INTERFEJS SALOONU ---
st.markdown("<div class='saloon-header'>🤠 SALOON CHENO 🌵</div>", unsafe_allow_html=True)
st.markdown("<div class='saloon-sub'>Najszybszy rewolwer czasowy po tej stronie Missisipi</div>", unsafe_allow_html=True)
st.write("---")

# Aktualny czas w ultra kartach 3D
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

# --- ANALIZA DNIA ---
st.write(" ")
if now_pl.date() == now_ia.date():
    st.markdown('<div class="date-same">🐎 STAN DROGI: Wszyscy jedziemy na tym samym wozie! (Ta sama data)</div>', unsafe_allow_html=True)
elif now_ia.date() < now_pl.date():
    st.markdown('<div class="date-yesterday">🪦 OSTRZEŻENIE: Iowa zostaje w tyle! Rancho żyje jeszcze WCZORAJSZYM DNIEM.</div>', unsafe_allow_html=True)

st.write("---")

# --- KALKULATOR Z LASSO (REWOLWERY CZASU) ---
st.markdown("<h3 style='font-family:\"Rye\", serif; text-align:center; color:#4a2c11;'>🌵 ZAŁADUJ BĘBENEK CZASU</h3>", unsafe_allow_html=True)

# Inicjalizacja domyślnych wartości w sesji
if 'saved_hour' not in st.session_state:
    st.session_state.saved_hour = int(datetime.now().hour)
if 'saved_minute' not in st.session_state:
    st.session_state.saved_minute = int(datetime.now().minute)

with st.form(key='cowboy_form_sliders'):
    wybór = st.radio(
        "Gdzie ustawiasz wskazówki, szeryfie?", 
        ("Podaję godzinę w Polsce", "Podaję godzinę w Iowa")
    )
    
    st.write(" ")
    # Rozbijamy wybór czasu na dwa klimatyczne suwaki
    wybrana_godzina = st.slider("🤠 Wybierz godzinę (Bębenek H):", min_value=0, max_value=23, value=st.session_state.saved_hour, step=1)
    wybrana_minuta = st.slider("🎯 Wybierz minutę (Celownik M):", min_value=0, max_value=59, value=st.session_state.saved_minute, step=1)
    
    st.write(" ")
    submit_button = st.form_submit_button(label='🔥 WYSTRZEL I PRZELICZ')

if submit_button:
    # Zapisujemy stan, żeby nie uciekał przy odświeżeniu
    st.session_state.saved_hour = wybrana_godzina
    st.session_state.saved_minute = wybrana_minuta
    
    # Składamy czas z suwaków
    zbudowany_czas = time(wybrana_godzina, wybrana_minuta)
    dzis = datetime.today().date()
    czysta_data_i_czas = datetime.combine(dzis, zbudowany_czas)

    st.write("---")
    if wybór == "Podaję godzinę w Polsce":
        pl_dt = tz_polska.localize(czysta_data_i_czas)
        ia_dt = pl_dt.astimezone(tz_iowa)
        
        st.success(f"🎯 Gdy w Polsce bije **{pl_dt.strftime('%H:%M')}**, w Iowa jest **{ia_dt.strftime('%H:%M')}**.")
        if ia_dt.date() == pl_dt.date():
            st.markdown('<div class="date-same">🐎 Obie strefy lądują tego samego dnia.</div>', unsafe_allow_html=True)
        elif ia_dt.date() < pl_dt.date():
            st.markdown('<div class="date-yesterday">🪦 W Iowa wciąż trwa WCZORAJSZY DZIEŃ!</div>', unsafe_allow_html=True)
            
    else:
        ia_dt = tz_iowa.localize(czysta_data_i_czas)
        pl_dt = ia_dt.astimezone(tz_polska)
        
        st.success(f"🎯 Gdy w Iowa wybije **{ia_dt.strftime('%H:%M')}**, w Polsce jest już **{pl_dt.strftime('%H:%M')}**.")
        if pl_dt.date() == ia_dt.date():
            st.markdown('<div class="date-same">🐎 Obie strefy lądują tego samego dnia.</div>', unsafe_allow_html=True)
        elif pl_dt.date() > ia_dt.date():
            st.markdown('<div class="date-yesterday">🚀 Polska wyprzedza czas i jest już w JUTRZEJSZYM DNIU!</div>', unsafe_allow_html=True)

# --- STOPKA ---
st.write("---")
st.markdown("<center style='color:#2b1704; font-weight:bold; font-family:\"Rye\", serif;'>🚬 Gold Edition v999 Pro. Yee-haw!</center>", unsafe_allow_html=True)
