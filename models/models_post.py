from models.models import Base
from sqlalchemy import Column, String, Integer, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from models.associations import likes_association
class Publicacoes(Base):
    __tablename__ = "publicacoes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    imagem = Column(LargeBinary, nullable=True)
    descricao = Column(String, nullable=True)
    autor_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    autor = relationship("User", back_populates="publicacoes")
    # likes
    
    curtidas_por = relationship(
        "User", 
        secondary=likes_association, 
        back_populates="posts_curtidos"
    )
    