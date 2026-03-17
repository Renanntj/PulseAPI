from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from models.models_post import Publicacoes
from schemas.posts import PublicacaoSchema
from dependecies.dependecies import abrir_sessao


router = APIRouter(prefix="/principal", tags=["principal"])

@router.get("/imagem/{pub_id}")
def get_imagem_publica(pub_id: int, db: Session = Depends(abrir_sessao)):
    pub = db.query(Publicacoes).filter(Publicacoes.id == pub_id).first()
    
    if not pub or not pub.imagem:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    
    return Response(content=pub.imagem, media_type="image/png")

@router.get("/publicacoes", response_model=List[PublicacaoSchema])
def listar_publicacoes(db: Session = Depends(abrir_sessao)):
    publicacoes = db.query(Publicacoes).all()
    return publicacoes
