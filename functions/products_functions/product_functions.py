import streamlit as st
from database.engine.database import *
import pandas as pd
from io import BytesIO
from functions.historico.historico import registrar_novo_fato
import datetime

def registrar_produto(nome:str,codigo:str,categoria:str,unidade:str,fabricante:str,registro:str,validade:str,fornecedor:str):
    try:
      novo_produto = Cadastro_Protudos(nome_produto = nome,codigo_produto = codigo,categoria = categoria,unidade_medida = unidade,fabricante = fabricante,registro_anvisa = registro,validade = validade,fornecedor=fornecedor)
      session.add(novo_produto)
      session.commit()
      session.close()
      registrar_novo_fato(data=str(datetime.datetime.today().date()),descricao=f'Cadastro do Produto: {codigo}',categoria='Cadastro de Produtos')
      return True
    except:
      session.rollback()
      session.close()
      return False
    
def ver_produtos():
  produtos = session.query(Cadastro_Protudos).all()
  lista = [{
     "Código do Produto":produto.codigo_produto,
     "Nome do Produto":produto.nome_produto,
     "Categoria":produto.categoria,
     "unidade de Medida":produto.unidade_medida,
     "Fornecedor":produto.fornecedor,
     'Fabricante':produto.fabricante,
     "Registro ANVISA":produto.registro_anvisa,
     "Validade":produto.validade
  } for produto in produtos]
  return pd.DataFrame(lista)

def atualizar_produtos(codigo:str,campo:str,alteracao:str):
  produto = session.query(Cadastro_Protudos).filter(Cadastro_Protudos.codigo_produto == codigo).first()
  if produto:
    if campo =='Nome':
      produto.nome_produto = alteracao
    elif campo =='Categoria':
      produto.categoria = alteracao
    elif campo == 'Unidade de Medida':
      produto.unidade_medida = alteracao
    elif campo == 'Fornecedor':
      produto.fornecedor = alteracao
    elif campo == 'Fabricante':
      produto.fabricante = alteracao
    elif campo == 'Registro Anvisa':
      produto.registro_anvisa = alteracao
    elif campo == 'Validade':
      produto.validade = alteracao
    session.commit()
    session.close()
    registrar_novo_fato(data=str(datetime.datetime.today().date()),descricao=f'Produto: {codigo} atualizado no campo: {campo} para o valor de: {alteracao}',categoria='Cadastro de Produtos')
    return True
  else:
    return False

def excluir_produto(codigo:str):
  produto = session.query(Cadastro_Protudos).filter(Cadastro_Protudos.codigo_produto == codigo).first()
  if produto:
    session.delete(produto)
    registrar_novo_fato(data=str(datetime.datetime.today().date()),descricao=f'Produto: {codigo} foi excluido',categoria='Cadastro de Produtos')
    return True
  else:
    return False
    
@st.dialog('Deseja realizar essa ação?')
def warning_exclusao(codigo:str):
  if str(st.text_input(placeholder='Digite "sim" para confirmar',label='',value='')).casefold().strip() == 'sim':
        if excluir_produto(codigo):
          return st.success(f'Produto: {codigo} excluido com sucesso')
        else:
          return st.error(f'Produto: {codigo} não pode ser excluido')
        
@st.cache_data
def convert_df_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            processed_data = output.getvalue()
            return processed_data    