import streamlit as st
from pathlib import Path
from functions.users.Login import *

st.markdown("""
    <style>
       [aria-expanded='true'] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
logo_path = Path('./images/') / 'logo.jpg'
st.image(str(logo_path))
st.logo(str(logo_path),size='large')
main_container = st.container(border=True)
main_container.title('Seja bem vindo, Faça seu Login')
main_container.divider()
email = main_container.text_input(label='Email',placeholder='Insira seu Email')
senha = main_container.text_input(label='Senha',placeholder='Insira sua senha',type='password')
botao = main_container.button(' Logar')
cadastro = main_container.button('Cadastrar novo Usuário')
if botao:
  if email and senha:
    if login(email,senha):
      st.switch_page('./pages/Painel Geral.py')
    else:
      main_container.error('Erro ao logar o usuário')
  else:
    main_container.error('Ainda faltam campos a serem preenchidos')
if cadastro:
  st.switch_page('./pages/Cadastro Usuários.py')