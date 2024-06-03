import streamlit as st
from utils.utils import *
import pandas as pd

def df_optional():
    query = 'SELECT DISTINCT OPTIONAL_optional FROM has_optional;'
    result = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(result)
    return df

def create_query_stanze(tipo_stanza):
    if tipo_stanza=='tutte':
        return ""
    else:
        return f" AND Type='{tipo_stanza}'"

def create_query_optional(optional):
    query = ""
    for el in optional:
        query = query + f" AND OPTIONAL_optional='{el}'"
    return query

def create_query_cucina(cucina):
    if cucina==True:
        return " AND SPAZI_spazi='cucina'"
    else:
        return ""

def create_page():
    with st.expander("Filtri", True):
        col1, col2, col3 = st.columns(3)

        tipo_stanza = col1.radio("Tipo di stanza: ", ["singola", "doppia", "tripla", "tutte"], index=3)
        optional = col2.multiselect("Optional: ", df_optional())
        cucina = col3.checkbox("Cucina")

        query_stanze = create_query_stanze(tipo_stanza)
        query_optional = create_query_optional(optional)
        query_cucina = create_query_cucina(cucina)

    query = f"SELECT stanza.CodS, stanza.Piano, stanza.Superficie, stanza.Type FROM stanza, has_spazi, has_optional WHERE stanza.CodS=has_spazi.STANZA_CodS AND stanza.CodS=has_optional.STANZA_CodS {query_stanze} {query_optional} {query_cucina};"
    result = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(result)
    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":

    st.title("🛎 :blue[Stanze]")

    if check_connection():
        create_page()