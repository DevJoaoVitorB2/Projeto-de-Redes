import streamlit as st

from ServerCliente.cliente import Cliente

def clienteUI():
    st.title("Conecte-se com o Servidor")
    if st.button("Conecte-se"):
        cliente = Cliente()
        cliente.procurar_servidor()
    