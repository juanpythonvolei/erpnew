from database.engine.database import *
def login(email:str,senha:int):
   try:
      session.query(Usuario).filter(Usuario.email == email,Usuario.senha == senha)
      return True
   except:
      return False