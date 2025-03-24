from sqlalchemy import create_engine, Column, Integer, String, BOOLEAN,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import streamlit as st
# Criar um engine para o banco de dados

# database = f'{os.getenv('database_url')}'
database = st.secrets['db']
engine = create_engine(database,echo=False)

# Definir a classe base do modelo
Base = declarative_base()
class Passe(Base):
    __tablename__ = 'Passes'
    chave = Column(String,unique=True,primary_key=True)
    id_usuario = Column(Integer)
# Definir a classe do modelo
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String)
    email = Column(String,unique=True)
    senha = Column(Integer) 
# Criar o banco de dados

class Cadastro_Protudos(Base):
    __tablename__ = 'Cadastro de produtos'
    id = Column(Integer, primary_key=True,autoincrement=True) 
    nome_produto = Column(String)
    codigo_produto = Column(String,unique=True)
    categoria = Column(String)
    unidade_medida = Column(String)
    fornecedor = Column(String)
    fabricante = Column(String)
    registro_anvisa = Column(String)
    validade = Column(String)

class Movimentacao_estoque(Base):
    __tablename__  = 'movimentação de estoque'
    id = Column(Integer, primary_key=True,autoincrement=True) 
    tipo_movimentacao = Column(String)
    codigo_produto = Column(String)
    nome_produto = Column(String)
    quantidade = Column(Integer)
    destino_origem = Column(String)
    observacoes = Column(String)

class Producao(Base):
    __tablename__ = 'producao'
    id = Column(Integer, primary_key=True,autoincrement=True)  
    data = Column(String)
    codigo_produto = Column(String)
    nome_produto = Column(String)
    quantidade_na_prducao = Column(Integer)
    lote = Column(String)
    ordem_producao = Column(String)
    status = (String)
class Controle_qualidade(Base):
    __tablename__ = 'controle de qualidade'
    id = Column(Integer, primary_key=True,autoincrement=True)  
    codigo_produto = Column(String)
    nome_produto = Column(String)
    lote = Column(String)
    status = Column(String)
    data_avaliacao = Column(String)
    observacoes = Column(String)
class Estoque_Final(Base):
    __tablename__ = 'estoque final'
    id = Column(Integer, primary_key=True,autoincrement=True)
    codigo_produto = Column(String)
    nome_produto = Column(String)
    lote = Column(String)
    quantidade_disponivel = Column(Integer)
    validade = Column(String)
    localizacao_estoque = Column(String)
    status_produto = Column(String)
class Historico(Base):
    __tablename__ = 'historico'
    id = Column(Integer, primary_key=True,autoincrement=True)
    data = Column(String)
    descricao = Column(String)
    categoria = Column(String)
    usuario = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()