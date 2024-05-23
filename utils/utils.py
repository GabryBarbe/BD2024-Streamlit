import streamlit as st
from sqlalchemy import create_engine,text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""

# Funzione di connessione al database
def connect_db(dialect, username, password, host, dbname):
    try:
        engine = create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}') 
        conn = engine.connect() #connessione
        return conn
    except:
        return False
    
# Funzione di esecuzione query
def execute_query(conn, query):
    return conn.execute(text(query))

# Funzione che controlla la connesione
def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

    if st.sidebar.button("Connettiti al Database"):
        myconnection=connect_db(dialect="mysql+pymysql",username="student",password="user_pwd",host="localhost",dbname="classicmodels")
        if myconnection is not False:
            st.session_state["connection"]=myconnection

        else:
            st.session_state["connection"]=False
            st.sidebar.error("Errore nella connessione al DB", icon="❌")

    if st.session_state["connection"]:
        st.sidebar.success("Connesso al DB", icon="✅")
        return True


# Funzione di formattazione del testo
def compact_format(num):
    num=float(num)
    if abs(num) >= 1e9:
        return "{:.2f}B".format(num / 1e9)
    elif abs(num) >= 1e6:
        return "{:.2f}M".format(num / 1e6)
    elif abs(num) >= 1e3:
        return "{:.2f}K".format(num / 1e3)
    else:
        return "{:.0f}".format(num)
