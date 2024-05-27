import streamlit as st
from sqlalchemy import create_engine,text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""


def execute_query(conn, query):
    return conn.execute(text(query))

def connect_db(dialect, username, pwd, host, db):
    try:
        engine = create_engine(f'{dialect}://{username}:{pwd}@{host}/{db}')
        conn = engine.connect()
        return conn
    except:
        return False
    
def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False

    if st.sidebar.button("Connetti il DB"):
        connection = connect_db(dialect="mysql+pymysql", username="root", pwd="root", host="localhost", db="hotel")
        if connection is not False:
            st.session_state["connection"] = connection
        else:
            st.sidebar.error("Connessione non riuscita", icon="❌")

    if st.session_state["connection"]:
        st.sidebar.success("Connessione riuscita!", icon="✅")
        return True