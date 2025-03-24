from database.engine.database import *
def login(email:str,senha:int):
   try:
      session.query(Usuario).filter(Usuario.email == email,Usuario.senha == senha)
      session.close()
      return True
   except:
      session.rollback()
      return False