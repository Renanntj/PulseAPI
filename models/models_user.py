from models.models import Base, user_games_association
from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.associations import likes_association



class User(Base):
    __tablename__ = "usuario"
    
    #usuario deve ter nome, usuario (unico), email (unico), senha e seu catalogo de jogos
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    admin = Column(Boolean, default=False)  
    nome = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    senha = Column(String, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now()) # adicionar foto de perfil

    # relacionamentos, para puxar os jogos e as publicações
    jogos = relationship("Jogos", secondary=user_games_association, back_populates="usuarios")
    publicacoes = relationship("Publicacoes", back_populates="autor")
    
    
    posts_curtidos = relationship(
        "Publicacoes", 
        secondary=likes_association, 
        back_populates="curtidas_por"
    )
    def __init__(self, nome, usuario, email, senha, admin=False):
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.admin = admin

    
    