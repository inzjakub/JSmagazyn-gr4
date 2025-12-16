import streamlit as st

# Tytuł aplikacji
st.title("📦 Prosty Magazyn")

# --- DODANIE MIKOŁAJA ---
# Mikołaj zostanie wyświetlony na górze, aby nie zakłócać działania aplikacji.
# Używamy st.image() z adresem URL, co jest najbezpieczniejszą metodą.
st.image("https://openclipart.org/image/400px/11821", caption="Ho Ho Ho!", width=100)


# --- LOGIKA APLIKACJI (Kod z Twojej pierwszej, działającej wersji) ---

# 1. INICJALIZACJA STANU (SESSION STATE)
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

# 2. SEKCJA DODAWANIA PRODUKTU
st.header("Dodaj nowy produkt")
nazwa_produktu = st.text_input("Wpisz nazwę produktu:")

if st.button("Dodaj produkt"):
    if nazwa_produktu:
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
    produkt_do_usuniecia = st.selectbox(
        "Wybierz produkt do usunięcia:", 
        options=st.session_state.magazyn
    )
    
    if st.button("Usuń wybrany produkt"):
        st.session_state.magazyn.remove(produkt_do_usuniecia)
        st.rerun() # Przeładowanie strony, aby zaktualizować listę natychmiast
else:
    st.info("Magazyn jest obecnie pusty.")
