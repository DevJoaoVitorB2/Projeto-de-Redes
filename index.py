import streamlit as st

from Templates.indexAdmin import AdminUI
from Templates.indexCliente import clienteUI

def index():
    st.title("Sistema Servidor/Cliente")
    pagina = st.radio("Escolha a Página: ", ("Ligar Servidor", "Conectar-se a um Servidor"))
    
    if pagina == "Ligar Servidor":
        AdminUI.login()
    if pagina == "Conectar-se a um Servidor":
        clienteUI()

index()