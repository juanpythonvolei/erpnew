from database.engine.database import *
import streamlit as st 
import datetime
from functions.historico.historico import registrar_novo_fato
import pandas as pd
from io import BytesIO

def registrar_producao(data:str,codigo:str,quantidade:int,lote:str,ordem:str,status:str):
  nova_producao = Producao(data=str(data).replace('/','-'),codigo_produto=codigo,nome_produto=session.query(Cadastro_Protudos).filter(Cadastro_Protudos.codigo_produto==codigo).first().nome_produto,quantidade_na_prducao = quantidade,lote=lote,ordem_producao = ordem,status=status)
  if nova_producao:
    session.add(nova_producao)
    session.commit()
    session.close()
    registrar_novo_fato(data=str(datetime.datetime.today().date()),descricao=f'Produção de ordem: {ordem} e de lote: {lote} para o produto: {codigo} com status: {status}',categoria='Produção')
    return True
  else:
    return False

def alterar_registro(data:str,codigo:str,campo:str,valor:str):
  registro = session.query(Producao).filter(Producao.data == data,Producao.codigo_produto == codigo).first()
  if registro:
    if campo == 'Quantidade de Produção':
      registro.quantidade_na_prducao = int(valor)
    elif campo == 'Lote':
      registro.lote = valor
    elif campo =='status':
      registro.status = valor
    session.commit()
    session.close()
    registrar_novo_fato(data=str(datetime.datetime.today().date()),descricao=f'Produção do produto: {codigo} na data de: {data} foi alterada no campo: {campo} para o valor de: {valor}',categoria='Produção')
    return True
  else:
    return False 
  
def ver_Producao():
  produtos = session.query(Producao).all()
  lista = [{
     "Data":produto.data,
     "Código do Produto":produto.codigo_produto,
     "Nome do Produto":produto.nome_produto,
     "Quantidade na Produção":produto.quantidade_na_prducao,
     'Lote':produto.lote,
     "Ordem de Produção":produto.ordem_producao,
     "Status":produto.status
  } for produto in produtos]
  return pd.DataFrame(lista)

@st.cache_data
def convert_df_to_excel(df,nome):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=f'{nome}')
            processed_data = output.getvalue()
            return processed_data 