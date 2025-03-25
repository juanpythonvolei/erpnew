import streamlit as st 
from database.engine.database import *
import pandas as pd
from io import BytesIO

def registrar_novo_fato(data:str,descricao:str,categoria:str,usuario:str = None):
  novo_registro = Historico(data=data.replace('/','-'),descricao=descricao,categoria=categoria,usuario=usuario)
  if novo_registro:
    session.add(novo_registro)
    session.commit()
    session.close()
    return True
  else:
    return False
    
def ver_historico():
  produtos = session.query(Historico).all()
  lista = [{
     "Data":produto.data,
     "Descrição":produto.descricao,
     "Categoria":produto.categoria,
     "Usuario":produto.usuario,
  } for produto in produtos]
  return pd.DataFrame(lista)

@st.cache_data
def convert_df_to_excel(df,nome):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=f'{nome}')
            processed_data = output.getvalue()
            return processed_data 

def ver_historico_filtrado(campo:str,valor:str):
    print(campo)
    if campo == 'Data':
      produtoss = session.query(Historico).filter(Historico.data == valor).all()
    elif campo == 'Categoria':
        produtoss = session.query(Historico).filter(Historico.categoria == valor).all()
    lista = [{
     "Data":produto.data,
     "Descrição":produto.descricao,
     "Categoria":produto.categoria,
     "Usuario":produto.usuario,
  } for produto in produtoss]
    return pd.DataFrame(lista)