from database.engine.database import *


def criar_usuario(nome:str,email:str,senha:int,passe:str):
  try:
    novo_usuario = Usuario(nome=nome,email=email,senha=senha)
    chave = session.query(Passe).filter(Passe.chave == passe).first()
    if not chave.id_usuario:
      if chave.chave == passe:
          session.add(novo_usuario)
          session.commit()
          chave.id_usuario = novo_usuario.id
          session.commit()
          session.close()
          return True
      else:
          return False
    else:
       return False
  except:
     session.rollback()
     session.close()
     return False
