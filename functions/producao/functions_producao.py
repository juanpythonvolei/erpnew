from database.engine.database import *
import streamlit as st 

def registrar_producao(data:str,codigo:str,quantidade:int,lote:str,ordem:str,status:str):
  nova_producao = Producao(data=data,codigo_produto=codigo,nome_produto=session.query(Cadastro_Protudos).filter(Cadastro_Protudos.codigo_produto==codigo).first().nome_produto,quantidade_na_prducao = quantidade,lote=lote,ordem_producao = ordem,status=status)
  if nova_producao:
    session.add(nova_producao)
    session.commit()
    session.close()
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
    return True
  else:
    return False 