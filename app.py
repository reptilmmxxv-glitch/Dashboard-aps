import streamlit as st
import pandas as pd

st.title("Dashboard APS")

archivo = st.file_uploader(
    "Sube un archivo Excel o CSV",
    type=["csv", "xlsx"]
)

if archivo is not None:

    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo)

    else:
        df = pd.read_excel(archivo)

    st.subheader("Vista previa de datos")
    st.dataframe(df)