from database.engine.database import *
def login(email:str,senha:int):
   
   if session.query(Usuario).filter(Usuario.email == str(email),Usuario.senha == int(senha)).first():
         session.close()
         return True
   else:
      session.rollback()
      return False