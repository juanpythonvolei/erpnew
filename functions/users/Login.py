from database.engine.database import *
def login(email:str,senha:int):

   if session.query(Usuario).filter(Usuario.email == email,Usuario.senha == senha).first():
      session.close()
      return True
   else:
      session.rollback()
      return False