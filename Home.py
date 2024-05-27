import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *

if __name__ == "__main__":
    st.set_page_config(
        page_title="La mia App",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://dbdmg.polito.it/',
            'Report a bug': "https://dbdmg.polito.it/",
            'About': "# Corso di *Basi di Dati*"
        }
    )
    
    col1, col2 = st.columns(2)
    col1.markdown("# :red[Laboratorio 06] :blue[Basi di Dati]")
    col1.markdown("### Gabriele Barbero")
    col2.image("images/polito_white.png")

    check_connection()