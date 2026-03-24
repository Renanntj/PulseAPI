from sqlalchemy import Table, Column, Integer, ForeignKey
from models.models import Base # Onde está seu declarative_base

likes_association = Table(
    "likes",
    Base.metadata,
    Column("usuario_id", Integer, ForeignKey("usuario.id"), primary_key=True),
    Column("publicacao_id", Integer, ForeignKey("publicacoes.id"), primary_key=True)
)