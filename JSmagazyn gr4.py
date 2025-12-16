import streamlit as st

# Ustawienie szerokiego układu strony, aby Mikołaj miał miejsce
st.set_page_config(layout="wide", page_title="Magazyn z Mikołajem")

# Kod SVG (grafika wektorowa) rysująca prostego Mikołaja
santa_svg = """
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 80 L100 10 L150 80 Z" fill="#D42426" />
    <circle cx="100" cy="10" r="15" fill="white" />
    <rect x="50" y="75" width="100" height="20" rx="10" fill="white" />
    
    <circle cx="100" cy="110" r="40" fill="#FFCCBC" />
    
    <circle cx="85" cy="100" r="4" fill="black" />
    <circle cx="115" cy="100" r="4" fill="black" />
    
    <circle cx="100" cy="115" r="7" fill="#EF9A9A" />
    
    <path d="M60 110 Q100 180 140 110" fill="white" stroke="#EEE" stroke-width="2"/>
    <circle cx="100" cy="150" r="30" fill="white" />
    <circle cx="75" cy="140" r="20" fill="white" />
    <circle cx="125" cy="140" r="20" fill="white" />
</svg>
"""

# Tytuł
st.title("📦 Świąteczny Magazyn")

# --- UKŁAD STRONY (KOLUMNY) ---
# Tworzymy dwie kolumny: 
# col1 (lewa) - zajmuje 70% szerokości (logika aplikacji)
# col2 (prawa) - zajmuje 30% szerokości (Mikołaj)
col1, col2 = st.columns([7, 3])

# --- LEWA STRONA (APLIKACJA) ---
with col1:
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = []

    st.subheader("Dodaj nowy produkt")
    nazwa_produktu = st.text_input("Wpisz nazwę produktu:")

    if st.button("Dodaj produkt"):
        if nazwa_produktu:
            st.session_state.magazyn.append(nazwa_produktu)
            st.success(f"Dodano: {nazwa_produktu}")
        else:
            st.warning("Proszę wpisać nazwę produktu.")

    st.divider()

    st.subheader("Stan magazynowy")
    if len(st.session_state.magazyn) > 0:
        for i, produkt in enumerate(st.session_state.magazyn, 1):
            st.text(f"{i}. {produkt}")
        
        st.write("---")
        
        produkt_do_usuniecia = st.selectbox(
            "Wybierz produkt do usunięcia:", 
            options=st.session_state.magazyn
        )
        
        if st.button("Usuń wybrany produkt"):
            st.session_state.magazyn.remove(produkt_do_usuniecia)
            st.rerun()
    else:
        st.info("Magazyn jest obecnie pusty.")

# --- PRAWA STRONA (MIKOŁAJ) ---
with col2:
    st.write("### Twój pomocnik:")
    # Renderowanie kodu SVG jako HTML
    st.markdown(santa_svg, unsafe_allow_html=True)
    st.caption("Ho, ho, ho! Zarządzaj mądrze!")
