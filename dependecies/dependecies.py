from models.models import SessionLocal
from fastapi import HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
from models.models_user import User
from jose import jwt, JWTError 
from services.crypt_services import oauth2_schema
from services.importar_env import SECRET_KEY, ALGORITHM
# importações que não estão sendo utilizadas estão aqui para verificação futura de token

def abrir_sessao():
    try:
        session = SessionLocal() # abrir sessao no banco de dados e fecha-la independente de qualquer coisa
        yield session
    finally:
        session.close()
        
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(abrir_sessao)):
    try:
        dic = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_user = int(dic.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso negado")
    user = session.query(User).filter(User.id==id_user).first()
    if not user:
        raise HTTPException(status_code=400, detail="Usuario não encontrado")
    return user
