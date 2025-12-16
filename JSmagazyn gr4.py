import streamlit as st

# Tytuł aplikacji
st.title("📦 Prosty Magazyn")

# 1. INICJALIZACJA STANU (SESSION STATE)
# Streamlit odświeża kod przy każdej akcji. Aby lista produktów nie znikała,
# musimy ją przechowywać w tzw. session_state.
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

# 2. SEKCJA DODAWANIA PRODUKTU
st.header("Dodaj nowy produkt")
nazwa_produktu = st.text_input("Wpisz nazwę produktu:")

if st.button("Dodaj produkt"):
    if nazwa_produktu:
        # Dodajemy produkt do listy w stanie sesji
        st.session_state.magazyn.append(nazwa_produktu)
        st.success(f"Dodano: {nazwa_produktu}")
    else:
        st.warning("Proszę wpisać nazwę produktu.")

st.divider() # Linia oddzielająca

# 3. SEKCJA LISTY I USUWANIA
st.header("Stan magazynowy")

if len(st.session_state.magazyn) > 0:
    # Wyświetlanie listy
    st.write("Aktualna lista produktów:")
    for i, produkt in enumerate(st.session_state.magazyn, 1):
        st.text(f"{i}. {produkt}")
    
    st.write("---")
    
    # Usuwanie produktu
    # Selectbox pozwala wybrać produkt z istniejącej listy
    produkt_do_usuniecia = st.selectbox(
        "Wybierz produkt do usunięcia:", 
        options=st.session_state.magazyn
    )
    
    if st.button("Usuń wybrany produkt"):
        st.session_state.magazyn.remove(produkt_do_usuniecia)
        st.rerun() # Przeładowanie strony, aby zaktualizować listę natychmiast
else:
    st.info("Magazyn jest obecnie pusty.")
