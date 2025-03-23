from database.engine.database import *
import pandas as pd
from io import BytesIO
import streamlit as st

def adicionar_nova_movimentacao(data:str,tipo:str,codigo:str,quantidade:int,destino:str,observacoes:str = None):
  produto = session.query(Cadastro_Protudos).filter(Cadastro_Protudos.codigo_produto == codigo).first()
  nome = produto.nome_produto
  nova_movimentacao = Movimentacao_estoque(data=data,tipo_movimentacao=tipo,codigo_produto=codigo,nome_produto=nome,quantidade=quantidade,destino_origem=destino,observacoes=observacoes)
  if nova_movimentacao:
    session.add(nova_movimentacao)
    session.commit()
    session.close()
    return True
  else:
    return False
  
def alterar_produto_ou_quantidade(data:str,codigo_produto:str,tipo:str,quantidade:str,destino:str,origem:str,observacoes:str = None):
  produto_origem = session.query(Movimentacao_estoque).filter(Movimentacao_estoque.codigo_produto == codigo_produto, Movimentacao_estoque.destino_origem == origem).first() 
  if produto_origem:
    produto_origem.quantidade -= quantidade
    session.commit()
    produto_destino = session.query(Movimentacao_estoque).filter(Movimentacao_estoque.codigo_produto == codigo_produto, Movimentacao_estoque.destino_origem == destino).first() 
    if produto_destino:
      produto_destino.quantidade += quantidade
      session.commit()
    else:
      nova_movimentacao = Movimentacao_estoque(data=data,tipo_movimentacao=tipo,codigo_produto=codigo_produto,nome_produto=produto_origem.nome_produto,quantidade=quantidade,destino_origem=destino,observacoes=observacoes)
      session.add(nova_movimentacao)
      session.commit()
    session.close()
    return True
  else:
    return False
  
def ver_movimentacoes():
  produtos = session.query(Movimentacao_estoque).all()
  lista = [{
     "Data":produto.data,
     "Tipo da movimentação":produto.tipo_movimentacao,
     "Código do Produto":produto.codigo_produto,
     "Nome do Produto":produto.nome_produto,
     "Quantidade":produto.quantidade,
     'Destino/Origem':produto.destino_origem,
     "Observações":produto.observacoes,
  } for produto in produtos]
  return pd.DataFrame(lista)

@st.cache_data
def convert_df_to_excel(df,nome):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=f'{nome}')
            processed_data = output.getvalue()
            return processed_data 