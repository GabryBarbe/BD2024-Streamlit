import streamlit as st
from utils.utils import *
import pandas as pd

def create_page():
    query = "WITH costi_mensili AS (SELECT STANZA_CodS, Costo, EXTRACT(YEAR FROM STR_TO_DATE(DataInizio, '%Y-%m-%d')) AS Anno, EXTRACT(MONTH FROM STR_TO_DATE(DataInizio, '%Y-%m-%d')) AS Mese FROM PRENOTAZIONE), costi_mensili_medi AS (SELECT STANZA_CodS, Anno, Mese, AVG(Costo) AS prezzo_medio_mensile FROM costi_mensili GROUP BY STANZA_CodS, Anno, Mese), max_costi_mensili_medi AS (SELECT Anno, Mese, MAX(prezzo_medio_mensile) AS prezzo_medio_max_mensile FROM costi_mensili_medi GROUP BY Anno, Mese) SELECT S.CodS, S.Piano, S.Superficie, S.Type, CMM.prezzo_medio_mensile, CMM.Anno, CMM.Mese FROM costi_mensili_medi CMM, max_costi_mensili_medi MCMM, STANZA S WHERE prezzo_medio_mensile = prezzo_medio_max_mensile AND CMM.Anno = MCMM.Anno AND CMM.Mese = MCMM.Mese AND CMM.STANZA_CodS = S.CodS;"
    result = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(result)

    st.line_chart(df, x='Mese', y='prezzo_medio_mensile', use_container_width=True)

if __name__ == "__main__":
    st.title("💸 :blue[Prenotazioni]")
    
    if check_connection():
        create_page()