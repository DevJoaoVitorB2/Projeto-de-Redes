import streamlit as st

from Models.admin import Admin, Admins
from Models.computador import Computadores

from ServerCliente.host import LigarServidor

class AdminUI:
    @staticmethod
    def login():
        # Formulário de Login
        with st.form("LOGIN"):
            usuario = st.text_input("Usuario")
            senha = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar")

        # Formulário submetido
        if submit:
            admins = Admins.listar()
            usuario_encontrado = None
            # Criação do Administrador caso não tenha um cadastrado
            if len(admins) == 0:
                Admins.inserir(Admin(0, "Administrador", "senha1234"))

            # Procurar administrador a ser logado
            for admin in admins:
                if admin.usuario == usuario and admin.senha == senha:
                    usuario_encontrado = admin
                    break
            
            # Logado ou Não Logado
            if usuario_encontrado:
                st.session_state['logged_in'] = True
                st.session_state['current_user'] = usuario_encontrado
                st.success("Login realizado com sucesso!")
                AdminUI.logado()
            else:
                st.error("Usuario ou senha incorretos.")

    @staticmethod
    def logado():
        LigarServidor.ligar()
        maquinas = {} # Dicionario com os dados de todas as maquinas que foram conectadas

        for dados in Computadores.listar():
            maquinas[f"{dados.nome}"] = dados # Adicionar os dados
        
        if not maquinas:
            st.write("Dados Inexistentes! Nenhuma Maquina foi Conectada Ainda!")
        else:
            maquina = st.selectbox("Maquinas: ", list(maquinas.keys())) # SelectBox com as Maquinas que foram conectadas
            info = maquinas[maquina]

            st.subheader(f"{info.nome}")
            st.write(f"Memória RAM Total: {info.ramTotal}GB")
            st.write(f"Memória RAM Livre: {info.ramLivre}GB")
            st.write(f"Quantidade de Processadores: {info.qtdProcessadores}")
            st.write(f"Armazenamento Total: {info.armazTotal}GB")
            st.write(f"Armazenamento Livre: {info.armazLivre}GB")
