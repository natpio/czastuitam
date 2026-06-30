# --- KALKULATOR PRZYSZŁEGO CZASU (ZŁAP CZAS NA LASSO) ---
st.subheader("🌵 Złap czas na lasso (Kalkulator)")

wybór = st.radio("Z której strefy startujesz, kowboju?", ("Chcę podać godzinę w Polsce", "Chcę podać godzinę w Iowa"))

wybrany_czas = st.time_input("Ustaw czas na zegarze:", datetime.now().time())

# Tworzymy "czysty" obiekt datetime bez żadnej strefy (naive)
czysta_data_i_czas = datetime.combine(datetime.today(), wybrany_czas)

if wybór == "Chcę podać godzinę w Polsce":
    # 1. Mówimy systemowi: to jest dokładnie ta godzina w Polsce
    pl_dt = tz_polska.localize(czysta_data_i_czas)
    # 2. Przeliczamy na Iowa
    ia_dt = pl_dt.astimezone(tz_iowa)
    
    st.info(f"🎯 Gdy w **Polsce** jest **{pl_dt.strftime('%H:%M')}**, na rancho w **Iowa** zegary wskazują **{ia_dt.strftime('%H:%M')}**.")

else:
    # 1. Mówimy systemowi: to jest dokładnie ta godzina w Iowa
    ia_dt = tz_iowa.localize(czysta_data_i_czas)
    # 2. Przeliczamy na Polskę
    pl_dt = ia_dt.astimezone(tz_polska)
    
    st.info(f"🎯 Gdy w **Iowa** jest **{ia_dt.strftime('%H:%M')}**, w **Polsce** kowboje widzą już **{pl_dt.strftime('%H:%M')}**.")
