import pandas as pd
from functions.historico.historico import ver_historico
from functions.producao.functions_producao import ver_Producao
from functions.products_functions.product_functions import ver_produtos
from  functions.storage_functions.movimentacoes.movimentacoes import ver_movimentacoes
from io import BytesIO
import streamlit as st


planilha_historico = ver_historico()
planilha_produtos = ver_produtos()
planilha_movimentacoes = ver_movimentacoes()
planilha_producao = ver_Producao()

@st.cache_data
def gerar_relatorio_final():
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
              planilha_produtos.to_excel(writer,sheet_name='Cadastro Produtos',index=False)
              planilha_movimentacoes.to_excel(writer,sheet_name='Estoque',index=False)
              planilha_historico.to_excel(writer,sheet_name='Registros',index=False)
              planilha_producao.to_excel(writer,sheet_name='Producao',index=False)
            processed_data = output.getvalue()
            return processed_data 