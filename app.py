import streamlit as st
from datetime import datetime
import pytz

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Rodeo Time Tracker",
    page_icon="🤠",
    layout="centered"
)

# --- STYLIZACJA RODEO / COWBOY (CSS) ---
st.markdown("""
    <style>
    /* Główny motyw - kolory pustyni, skóry i drewna */
    .stApp {
        background-color: #f4ece1;
        color: #5c3a21;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Nagłówki */
    h1, h2, h3 {
        color: #8b4513 !important;
        font-weight: bold;
        text-shadow: 1px 1px 2px #d2b48c;
    }
    
    /* Karty z czasem */
    .time-card {
        background-color: #d2b48c;
        border: 3px solid #8b4513;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    
    .time-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #5c3a21;
        margin-bottom: 5px;
    }
    
    .time-display {
        font-size: 2.2rem;
        font-weight: bold;
        color: #ffffff;
        background-color: #8b4513;
        padding: 10px;
        border-radius: 5px;
        letter-spacing: 2px;
    }
    
    /* Stopka i inne elementy */
    .leather-text {
        color: #a0522d;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIKA STREF CZASOWYCH ---
tz_polska = pytz.timezone('Europe/Warsaw')
tz_iowa = pytz.timezone('US/Central')

now_pl = datetime.now(tz_polska)
now_ia = datetime.now(tz_iowa)

# --- INTERFEJS REVOLVEROWCA ---
st.title("🤠 RODEO TIME TRACKER 🐎")
st.markdown("<p class='leather-text'>Szybki kalkulator czasu: Polska vs Iowa (Rancho Central Time)</p>", unsafe_allow_html=True)
st.write("---")

# Aktualny czas w kowbojskich kartach
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="time-card">
            <div class="time-title">🇵🇱 POLSKA (Warszawa)</div>
            <div class="time-display">{now_pl.strftime('%H:%M:%S')}</div>
            <p style="margin-top:10px; color:#5c3a21;">{now_pl.strftime('%d.%m.%Y')}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="time-card">
            <div class="time-title">🇺🇸 IOWA (Des Moines)</div>
            <div class="time-display">{now_ia.strftime('%H:%M:%S')}</div>
            <p style="margin-top:10px; color:#5c3a21;">{now_ia.strftime('%m/%d/%Y')}</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- KALKULATOR PRZYSZŁEGO CZASU (ZŁAP CZAS NA LASSO) ---
st.subheader("🌵 Złap czas na lasso (Kalkulator)")

wybór = st.radio("Z której strefy startujesz, kowboju?", ("Chcę podać godzinę w Polsce", "Chcę podać godzinę w Iowa"))

wybrany_czas = st.time_input("Ustaw czas na zegarze:", datetime.now().time())

# Tworzymy "czysty" obiekt datetime bez przypisanej strefy (naive)
czysta_data_i_czas = datetime.combine(datetime.today(), wybrany_czas)

if wybór == "Chcę podać godzinę w Polsce":
    # Wskazujemy, że podany czas to godzina w PL i przeliczamy na Iowa
    pl_dt = tz_polska.localize(czysta_data_i_czas)
    ia_dt = pl_dt.astimezone(tz_iowa)
    
    st.info(f"🎯 Gdy w **Polsce** jest **{pl_dt.strftime('%H:%M')}**, na rancho w **Iowa** zegary wskazują **{ia_dt.strftime('%H:%M')}**.")

else:
    # Wskazujemy, że podany czas to godzina w Iowa i przeliczamy na PL
    ia_dt = tz_iowa.localize(czysta_data_i_czas)
    pl_dt = ia_dt.astimezone(tz_polska)
    
    st.info(f"🎯 Gdy w **Iowa** jest **{ia_dt.strftime('%H:%M')}**, w **Polsce** kowboje widzą już **{pl_dt.strftime('%H:%M')}**.")

# --- STOPKA ---
st.write("---")
st.markdown("<center> Yee-haw! Aplikacja śmiga szybciej niż Colt 45. 🌵🦅</center>", unsafe_allow_html=True)
