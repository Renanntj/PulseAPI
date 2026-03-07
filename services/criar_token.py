from models.models_user import User
from .crypt_services import verificar_senha
from datetime import datetime, timedelta, timezone
from services.importar_env import ACCESS_TOKEN_MINUTES, SECRET_KEY, ALGORITHM
from jose import jwt

def autenticacao_user(email, password, session):
    user = session.query(User).filter(User.email==email).first()
    if not user:
        return False
    elif not verificar_senha(password, user.senha):
        return False
    return user


def criar_token(id_user, duration_token=timedelta(minutes=ACCESS_TOKEN_MINUTES)):
    date_exp = datetime.now(timezone.utc) + duration_token
    dic = {"sub": str(id_user), "exp": date_exp}
    jwt_code = jwt.encode(dic, SECRET_KEY, ALGORITHM)
    return jwt_code