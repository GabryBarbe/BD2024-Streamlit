import streamlit as st
from utils.utils import *
import pandas as pd

# Funzione per la creazione della pagina
def create_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        query = "SELECT COUNT(*) AS NAgenzie FROM agenzia;"
        result = execute_query(st.session_state["connection"], query)
        num_agenzie = [dict(zip(result.keys(), row)) for row in result]

        st.metric("Numero di Agenzie: ", num_agenzie[0]['NAgenzie'])
    with col2:
        query = "SELECT COUNT(DISTINCT Citta_Indirizzo) AS NCitta FROM agenzia;"
        result = execute_query(st.session_state["connection"], query)
        num_citta = [dict(zip(result.keys(), row)) for row in result]

        st.metric("Numero di Citta: ", num_citta[0]['NCitta'])
    with col3:
        query = "WITH agenzie_per_citta AS (SELECT Citta_Indirizzo, COUNT(*) AS NAgenzie FROM agenzia GROUP BY Citta_Indirizzo) SELECT Citta_Indirizzo FROM agenzie_per_citta WHERE NAgenzie = (SELECT MAX(NAgenzie) FROM agenzie_per_citta);"
        result = execute_query(st.session_state["connection"], query)
        citta = [dict(zip(result.keys(), row)) for row in result]

        st.metric("Città con più agenzie: ", citta[0]['Citta_Indirizzo'])

    query = "SELECT Latitudine as 'lat', Longitudine as 'lon' FROM citta, agenzia WHERE citta.Nome=agenzia.Citta_Indirizzo;"
    coord = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(coord)
    st.map(df)

    filtro_citta = st.text_input("Filtro per città: ")
    if filtro_citta!='':
        query=f"SELECT Citta_Indirizzo, CONCAT(Via_Indirizzo, ',', Numero_Indirizzo) AS Indirizzo FROM agenzia WHERE Citta_Indirizzo='{filtro_citta}';"
    else:
        query = "SELECT Citta_Indirizzo, CONCAT(Via_Indirizzo, ',', Numero_Indirizzo) AS Indirizzo FROM agenzia;"
    result = execute_query(st.session_state["connection"], query)

    df = pd.DataFrame(result)
    st.dataframe(df, use_container_width=True)
        


if __name__ == "__main__":
    st.title("🏢 :blue[Agenzie]")
    
    if check_connection():
        create_page()
