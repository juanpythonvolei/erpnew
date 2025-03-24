import streamlit as st
from database.engine.database import *
from functions.users.cadastro import *
from time import sleep
from pathlib import Path
st.markdown("""
    <style>
       [aria-expanded='true'] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
botao_login = st.button('⬅️')
if botao_login:
  st.switch_page('Login.py')
logo_path = Path('./images/') / 'logo.jpg'
st.image(str(logo_path))
st.logo(str(logo_path),size='large')
passe = st.text_input(label='Chave',placeholder='Insira uma chave de acesso',type='password')

if passe:
  container_novo_usuario = st.container(border=True)
  container_novo_usuario.title('Cadastre-se Aqui')
  nome = container_novo_usuario.text_input(label='Nome',placeholder='Insira seu Nome')
  email= container_novo_usuario.text_input(label='Email',placeholder='Insira seu email')
  senha = container_novo_usuario.text_input(label='Senha',placeholder='Insira sua Senha',type='password')
  botao = container_novo_usuario.button('Cadastrar usuário')
  if botao:
    if nome and email and senha:
      with container_novo_usuario.status(label='Cadastrando'):
        novo_usuario = criar_usuario(nome,email,senha,passe)
      if novo_usuario:
        container_novo_usuario.success('Usuário criado e credenciado. Em segundos você será redirecionado para o login')
        sleep(4)
        st.switch_page('Login.py')
      else:
        container_novo_usuario.error('Erro ao criar Usuário')
    else:
      container_novo_usuario.error('Ainda faltam campos a serem preenchidos')
else:
  st.info('Insira uma chave para liberar o cadastro')