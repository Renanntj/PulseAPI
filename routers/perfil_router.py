from fastapi import APIRouter
from schemas.usuario import CriarUsuarioSchema, LoginSchema
from fastapi import HTTPException, Depends, status
from dependecies.dependecies import abrir_sessao, verificar_token
from sqlalchemy.orm import Session
from models.models_user import User
from services.crypt_services import gerar_senha_hash
from services.verificar_nome import verificar_usuario_valido
from fastapi.security import OAuth2PasswordRequestForm
from services.criar_token import criar_token, autenticacao_user
from datetime import timedelta


router_user = APIRouter(prefix="/user", tags=["user"])

# criçao de user para exemplo, por enquanto so um teste, sem login

@router_user.post("/criar-usuario", status_code=status.HTTP_201_CREATED)
async def criar_user(usuario_schema: CriarUsuarioSchema, session: Session = Depends(abrir_sessao)): # criar usuario
    verificar_usuario = session.query(User).filter(User.email==usuario_schema.email).first()
     
    if verificar_usuario:
        raise HTTPException(status_code=400, detail="Email de usuario existente")
    
    else:
        verificar_username = session.query(User).filter(User.usuario==usuario_schema.usuario).first()
        if verificar_username:
            raise HTTPException(status_code=400, detail="Nome de usuario existente")
        
        elif not verificar_usuario_valido(usuario_schema.usuario):
            raise HTTPException(status_code=400, detail=
                "Nome de usuario deve ser minusculo, ter apenas letras, numero e '_', '-' e '.'"
            )
        senha_segura = gerar_senha_hash(usuario_schema.senha)
        novo_usuario = User(usuario_schema.nome, usuario_schema.usuario, usuario_schema.email, senha_segura)
        session.add(novo_usuario)
        session.commit()
        return {
            "message": f"Usuario adicionado com sucesso!",
            "nome": usuario_schema.nome,
            "email": usuario_schema.email 
        }

@router_user.get("/ver-perfil/{username}")
async def ver_perfil_publico(username: str, session: Session = Depends(abrir_sessao)): # aqui será para ver o perfil (visita de perfil)
    perfil = session.query(User).filter(User.usuario==username).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    
    return {
        "Nome": perfil.nome,
        "Usuario": perfil.usuario
    }
    

@router_user.post("/login")
async def login_user_auth(user_schema: LoginSchema, session: Session = Depends(abrir_sessao)):
    user = autenticacao_user(user_schema.email, user_schema.senha, session)
    if not user:
        raise HTTPException(status_code=400, detail="Email ou senha invalidos")
    else:
        access_token = criar_token(user.id)
        refresh_token = criar_token(user.id, duration_token=timedelta(days=7))
        return {"access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer"
        }
        
@router_user.post("/login-form")
async def login_user_auth(dados_form : OAuth2PasswordRequestForm = Depends(), session: Session = Depends(abrir_sessao)):
    user = autenticacao_user(dados_form.username, dados_form.password, session)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou senha invalidos")
    else:
        access_token = criar_token(user.id)
        return {"access_token": access_token,
                "token_type": "Bearer"
                }
 
@router_user.get("/refresh")
async def refresh_roter_auth(user: Session = Depends(verificar_token)):
    access_token = criar_token(user.id)
    return {"access_token": access_token,
            "token_type": "Bearer"
        }
# @router_user.delete("/deletar-user")
# async def deletar(email_user: str, session: User = Depends(abrir_sessao)):
    
#     usuario = session.query(User).filter(email_user==User.email).first()
    
#     session.delete(usuario)
#     session.commit()