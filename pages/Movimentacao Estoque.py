import streamlit as st 
from database.engine.database import *
from functions.storage_functions.movimentacoes.movimentacoes import *
from pathlib import Path
logo_path = Path('./images/') / 'logo.jpg'
st.image(str(logo_path))
st.logo(str(logo_path),size='large')

aba = st.sidebar.pills(label='Selecione a aba',options=['Movimentações','Ver meu estoque'])
if aba == 'Movimentações':
  container_movimentacao = st.container(border=True)
  container_movimentacao.title('Movimentações no Estoque')
  
  codigo_produto = container_movimentacao.selectbox(label='Produto',options=[produto.codigo_produto for produto in session.query(Cadastro_Protudos).all()],index=None,placeholder='Selecione um código')
  tipo_movimentacao = container_movimentacao.segmented_control(label='Selecione o tipo de Movimentação',options=['Entrada','Saida','Alteração de posição/quantidade'])
  if tipo_movimentacao != 'Alteração de posição/quantidade':
    quantidade_produto = container_movimentacao.slider(label='Selecione a quantidade')
    destino_origem = container_movimentacao.text_input(label='Destino/Origem',placeholder='Insira o destino/Origem')
    observacoes = container_movimentacao.text_area(label='Observações',placeholder='Insira a suas observações')
    botao_movimentacoes = container_movimentacao.button('Realizar movimentação')
    if botao_movimentacoes:
      if not tipo_movimentacao or not codigo_produto or not quantidade_produto or not destino_origem:
        container_movimentacao.error("Ainda restam campos a serem preenchidos")
      else:
        if adicionar_nova_movimentacao(tipo_movimentacao,codigo_produto,quantidade_produto,destino_origem,observacoes):
          container_movimentacao.success(f"Movimentação do tipo : {tipo_movimentacao} do produto: {codigo_produto} foi registrada para o destino: {destino_origem} na quantidade: {quantidade_produto}")
        else:
          container_movimentacao.error(f'Erro ao realizar a movimentação do produto: {codigo_produto}')
  else:
    posicao_origem = container_movimentacao.selectbox(label='Local',placeholder='Selecione um local de origem',options=[produto.destino_origem for produto in session.query(Movimentacao_estoque).filter(Movimentacao_estoque.codigo_produto == codigo_produto).all()],index=None)
    posicao_fim = container_movimentacao.text_input(label='Final',placeholder='Selecione o local final')
    quantidade_alteracao = container_movimentacao.slider(label='Quantidade')
    botao_alteracao = container_movimentacao.button('Fazer alteração')
    if botao_alteracao:
      if not posicao_origem or not posicao_fim or not quantidade_alteracao or not codigo_produto:
        container_movimentacao.error('Ainda restam campos a serem preenchidos')
      else:
        if alterar_produto_ou_quantidade(codigo_produto,tipo_movimentacao,quantidade_alteracao,posicao_fim,posicao_origem):
          container_movimentacao.success(f"Alteração realizada com sucesso para o produto: {codigo_produto}")
        else:
          container_movimentacao.error(f"Erro ao realizar a alteraçã no estoque para o produto: {codigo_produto}")
if aba == 'Ver meu estoque':
  container_estoque = st.container(border=True)
  container_estoque.title('Movimentações de estoque')
  container_estoque.divider()
  container_estoque.download_button('Faça o download da tabela de estoque para excel',data=convert_df_to_excel(ver_movimentacoes(),'Estoque'),
    file_name=f"Tabela de Produtos.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                                    )
  container_estoque.dataframe(ver_movimentacoes(),hide_index=True)