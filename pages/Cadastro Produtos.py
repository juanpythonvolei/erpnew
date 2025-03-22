import streamlit as st 
from functions.products_functions.product_functions import*

side_bar_tab_selection = st.sidebar.selectbox(label='Selecionar Aba',options=['Adicionar Produtos','Ver produtos','Modificar Produtos'])

if side_bar_tab_selection == 'Adicionar Produtos':
  container_form = st.container(border=True)
  container_form.title('Cadastro de Produtos')
  container_form.divider()
  
  nome_produto = container_form.text_input(label='Nome',placeholder='Insira o nome do produto',key='nome')
  codigo_produto = container_form.text_input(label='Código',placeholder='Insira o Código do produto',key='codigo',value=None)
  categoria_produto = container_form.text_input(label='Categoria',placeholder='Insira a categoria do produto',key='categoria')
  unidade_produto = container_form.text_input(label='Unidade de Medida',placeholder='Insira a unidade do produto',key='unidade')
  fornecedor_produto = container_form.text_input(label='Fornecedor',placeholder='Insira o fornecedor do produto',key='fornecedor')
  fabricante_produto = container_form.text_input(label='Fabricante',placeholder='Insira o fabricante do produto',key='fabricante')
  registro_produto = container_form.text_input(label='Registo Anvisa',placeholder='Insira o registro do produto',key='registro')
  validade_produto = container_form.date_input(label='Validade',value=None)
  botao_cadastro = container_form.button('Cadastrar Produto')
  if botao_cadastro:
    if not nome_produto or not codigo_produto or not categoria_produto or not unidade_produto or not fabricante_produto or not registro_produto or not validade_produto:
      container_form.error('Ainda há campos a serem preenchidos')
    else:
      if registrar_produto(nome_produto,codigo_produto,categoria_produto,unidade_produto,fabricante_produto,registro_produto,str(validade_produto),fornecedor_produto):
        container_form.success(f'Produto: {nome_produto} cadastrado com sucesso')
      else:
        container_form.error(f'Erro ao cadastrar o produto: {nome_produto}')
elif side_bar_tab_selection == 'Ver produtos':
  container_product = st.container(border=True)
  container_product.title('Produtos Cadastrados')
  container_product.divider()
  container_product.download_button(
    label=f"Faça o download da tabela de Produtos cadastrados no formato Excel",
    data=convert_df_to_excel(ver_produtos()),
    file_name=f"Tabela de Produtos.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

  container_product.divider()
  container_product.dataframe(ver_produtos(),hide_index=True)
else:
  container_update = st.container(border=True)
  container_update.title('Altere as informações do produto')
  container_update.divider()
  produto_a_se_alterar = container_update.selectbox(label='Produto',placeholder='Selecione um de seus produtos',index=None,options=[produto.codigo_produto for produto in session.query(Cadastro_Protudos).all()])
  informacao_a_se_alterar = container_update.selectbox(label='Campo',placeholder='Selecione o campo a ser alterado',options=['Nome','Categoria','Código','Unidade de Medida','Fornecedor','Fabricante','Registro Anvisa','Validade'],index=None)
  if informacao_a_se_alterar == 'Validade':
    valor_a_se_alterar = container_update.date_input(label='Nova Validade',value=None)
  else:
    valor_a_se_alterar = container_update.text_input(label='Valor',placeholder='Insira um novo valor')
  if produto_a_se_alterar:
    alteracao = container_update.button(f'Alterar Produto de Código: {produto_a_se_alterar}')
    exclusao = container_update.button(f'Excluir Produto de Código: {produto_a_se_alterar}')
    if exclusao:
      warning_exclusao(produto_a_se_alterar)
    if alteracao:
      if not produto_a_se_alterar or not informacao_a_se_alterar or not valor_a_se_alterar:
        container_update.error('Ainda faltam campos a serem preenchidos')
      else:
        if atualizar_produtos(produto_a_se_alterar,informacao_a_se_alterar,valor_a_se_alterar):
          container_update.success(f'Produto: {produto_a_se_alterar} no campo: {informacao_a_se_alterar} foi modificado para o valor de {valor_a_se_alterar}')
        else:
          container_update.error(f'Erro ao modificar o campo: {informacao_a_se_alterar} para o produto: {produto_a_se_alterar}')