import streamlit as st
from functions.historico.historico import *
from pathlib import Path
logo_path = Path('./images/') / 'logo.jpg'
st.image(str(logo_path))
st.logo(str(logo_path),size='large')
container_historico = st.container(border=True)
container_historico.title('Histórico')
barra = st.sidebar.segmented_control(label='Selecione um filtro',options=['Data','Categoria'])
if barra:
  if barra == 'Data':
    campo = st.sidebar.date_input(label='Selecione uma data')
  if barra == 'Categoria':
    campo = st.sidebar.selectbox(label='Seleção',placeholder='Selecione uma categoria',options=list(set([item.categoria for item in session.query(Historico).all()])),index=None)
  botao = st.sidebar.button('Aplicar Filtro')
  if botao:
    if campo:
      container_historico.dataframe(ver_historico_filtrado(barra,campo))
else:

  container_historico.divider()
  container_historico.dataframe(ver_historico(),hide_index=True)