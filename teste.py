import streamlit as st

placeholder = st.empty()

with placeholder.form("login"):
    st.markdown("#### Painel de Login")
    email = st.text_input("Email", placeholder="Digite aqui seu email")
    senha = st.text_input("Senha", placeholder="Digite aqui sua senha", type="password")
    login_button = st.form_submit_button("Login")

    if login_button:
        placeholder.empty()
        email = st.text_input("Email", placeholder="Digite aqui seu email")