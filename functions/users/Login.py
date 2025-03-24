from database.engine.database import *
def login(email:str,senha:int):
  meu_usuario = st.secrets['meuusuario']
  minha_senha = st.secrets['minhasenha']
#   meu_usuario = os.getenv('meuusuario')
#   minha_senha = os.getenv('minhasenha')
  if email == str(meu_usuario) and senha == (minha_senha):
     return True
  else:
   try:
      session.query(Usuario).filter(Usuario.email == email,Usuario.senha == senha)
      return True
   except:
      return False