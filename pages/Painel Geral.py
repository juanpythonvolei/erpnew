import streamlit as st 
from database.engine.database import *
from functions.historico.historico import *
from pathlib import Path
from functions.tables.tabela_geral import gerar_relatorio_final
logo_path = Path('./images/') / 'logo.jpg'
st.image(str(logo_path))
st.logo(str(logo_path),size='large')


st.title('Seja bem vindo Usuário')
st.subheader('Selecione ao lado os resumos do seu negócio')
with st.sidebar.popover(label='Fazer download de relatório geral'):
  st.download_button(label='📂',data=gerar_relatorio_final(),file_name=f"Relatorio Geral.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    
toggle_estoque = st.sidebar.toggle('Ver Estoque')
toggle_cadastro = st.sidebar.toggle('Ver Cadastramento')
toggle_producao = st.sidebar.toggle('Ver Produção')
if toggle_estoque:
  container_estoque = st.container(border=True)
  container_estoque.subheader('Estoque')
  container_estoque.divider()
  container_estoque.metric(label='Total de itens',value=sum(item.quantidade for item in session.query(Movimentacao_estoque).all()))
  container_estoque.metric(label='Total de Códigos diferentes em estoque',value=len(list(set([item.codigo_produto for item in session.query(Movimentacao_estoque).all()]))))
if toggle_cadastro:
  container_cadastro = st.container(border=True)
  container_cadastro.subheader('Cadastro de Produtos')
  container_cadastro.divider()
  container_cadastro.metric(label='Total de itens cadastrados',value=len(list(set(session.query(Cadastro_Protudos).all()))))
  container_cadastro.metric(label='Total de Fabricantes cadastrados',value=len(list(set(session.query(Cadastro_Protudos.fabricante).all()))))
  container_cadastro.metric(label='Total de Fornecedores cadastrados',value=len(list(set(session.query(Cadastro_Protudos.fornecedor).all()))))
if toggle_producao:
  container_cadastro = st.container(border=True)
  container_cadastro.subheader('Produção')
  container_cadastro.divider()
  container_cadastro.metric(label='Total de itens em Produção',value=sum([item.quantidade_na_prducao for item in session.query(Producao).all()]))
  container_cadastro.metric(label='Total de Itens Prontos',value=len(list(set(session.query(Producao).filter(Producao.status == 'Concluido').all()))))
  container_cadastro.metric(label='Total de Itens Aguardando liberação',value=len(list(set(session.query(Producao).filter(Producao.status == 'Aguardando liberação').all()))))
