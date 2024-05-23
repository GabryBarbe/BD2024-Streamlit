import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata

# Funzione per creare la tab_prodotti con le specifiche delle slide
def create_tab_prodotti(tab):
    col1, col2, col3 = tab.columns(3)

    payment_info = execute_query(st.session_state["connection"],"SELECT SUM(amount) AS 'Total Amount', MAX(amount) AS 'Max Payment', AVG(amount) AS 'Average Payment' FROM payments;")
    payment_info_dict = [dict(zip(payment_info.keys(), result)) for result in payment_info]

    col1.metric("Importo Totale", f"${compact_format(payment_info_dict[0]['Total Amount'])}")
    col2.metric("Pagamento Massimo", f"${compact_format(payment_info_dict[0]['Max Payment'])}")
    col3.metric("Pagamento Medio", f"${compact_format(payment_info_dict[0]['Average Payment'])}")

    with tab.expander("Panoramica Prodotti", True):
        prod_col1, prod_col2, prod_col3 = st.columns(3)

        sort_param = prod_col1.radio("Ordina per: ", ["code", "name", "quantity", "price"])
        sort_choice = prod_col2.selectbox("Ordine: ", ["Crescente", "Decrescente"])

        sort_dict={"Crescente":"ASC", "Decrescente":"DESC"}

        if prod_col1.button("Mostra", type="primary"):
            query_base = "SELECT productCode AS 'code', productName AS 'name', quantityInStock AS quantity, buyPrice AS price, MSRP FROM products"
            query_sort = f"ORDER BY {sort_param} {sort_dict[sort_choice]};"
            prodotti = execute_query(st.session_state["connection"], query_base+" "+query_sort)
            df_prodotti = pd.DataFrame(prodotti)
            st.dataframe(df_prodotti, use_container_width=True)


if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti, tab_staff, tab_clienti = st.tabs(["Prodotti","Staff","Clienti"])

    if check_connection():
        create_tab_prodotti(tab=tab_prodotti)
    