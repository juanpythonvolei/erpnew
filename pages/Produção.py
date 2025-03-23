import streamlit as st
from functions.producao.functions_producao import *
from database.engine.database import *

st.sidebar.empty()
container_alteracao = st.sidebar.container(border=True)
container_alteracao.subheader('Alterações')
container_alteracao.divider()
 
opcoes = container_alteracao.pills(label='Selecione o campo de alteração',options=['Quantidade de Produção','Lote','status'])
item = container_alteracao.selectbox(label='Produto',options=[produto.codigo_produto for produto in session.query(Cadastro_Protudos).all()],index=None,placeholder='Selecione um código',key='alteracao')
  
if opcoes == 'Quantidade de Produção':
    valor_alteracao = container_alteracao.number_input(label='Insira a quantidade')
elif opcoes == 'status':
    valor_alteracao  = container_alteracao.pills(label='Selecione o status de produção',options=['Em produção','Aguardando liberação','Concluido'],key='status_alteracao')
else:
    valor_alteracao = container_alteracao.text_input(label='Novo valor',placeholder='Insira o novo valor',key='valor_alteracao')
data_registro = container_alteracao.date_input(label='Selecione a data do registro',key='Data alteracao',value=None)  
botao_altercao = container_alteracao.button('Realizar alteração')
if botao_altercao:
    if opcoes and item and valor_alteracao:
      if alterar_registro(data_registro,item,opcoes,valor_alteracao):
        container_alteracao.success('Alteração feita com sucesso')
      else:
        container_alteracao.error('Erro ao alterar registro')
    else:
      container_alteracao.error("Ainda restam campos a serem preenchidos")

container_producao = st.container(border=True)
container_producao.title('Registro de Nova produção')
container_producao.divider()
data = container_producao.date_input(label='Selecione a data')
codigo = container_producao.selectbox(label='Produto',options=[produto.codigo_produto for produto in session.query(Cadastro_Protudos).all()],index=None,placeholder='Selecione um código')
quantidade  = container_producao.slider(label='Quantidade Produção')
lote  = container_producao.text_input(label='Lote',placeholder='Lote da Produção')
ordem_producao = container_producao.text_input(label='Ordem de Produção',placeholder='Ordem de Produção')
status  = container_producao.pills(label='Selecione o status de produção',options=['Em produção','Aguardando liberação','Concluido'])
botao_nova_producao = container_producao.button('Registrar nova produção')
if botao_nova_producao:
  if not data or not codigo or not quantidade or not lote or not ordem_producao or not status:
    container_producao.error("Ainda restam campos a serem preenchidos")
  else:
    if registrar_producao(data,codigo,quantidade,lote,ordem_producao,status):
      container_producao.success("Sucesso ao registrar uma nova produção")
    else:
      container_producao.error("Erro ao registrar a produção")