from fastapi import APIRouter, status
from fastapi import HTTPException, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from dependecies.dependecies import abrir_sessao, verificar_token
from typing import Optional
from models.models_post import Publicacoes
from models.models_user import User
from schemas.posts import EditarPost
router_posts = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(verificar_token)])



@router_posts.post("/criar-post", status_code=201)
async def criar_post(
    titulo: str = Form(...),
    descricao: Optional[str] = Form(None),
    arquivo: UploadFile = File(None),
    db: Session = Depends(abrir_sessao),
    usuario_logado: User = Depends(verificar_token) 
):
    conteudo_binario = await arquivo.read() if arquivo else None
        
    nova_pub = Publicacoes(
        titulo=titulo,
        descricao=descricao,
        imagem=conteudo_binario, 
        autor_id=usuario_logado.id  
    )
    
    db.add(nova_pub)
    db.commit()
    db.refresh(nova_pub)
    return nova_pub

@router_posts.patch("/editar-post/{post_id}")
async def editar_post(
    post_id: int, 
    dados_editados: EditarPost,
    session: Session = Depends(abrir_sessao), 
    user_logado: User = Depends(verificar_token)
):
    
    post = session.query(Publicacoes).filter(Publicacoes.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")


    if post.autor_id != user_logado.id:
        raise HTTPException(
            status_code=403, 
            detail="Você não tem permissão para editar este post"
        )

    update_data = dados_editados.dict(exclude_unset=True)
    for campo, valor in update_data.items():
        setattr(post, campo, valor)

    try:
        session.add(post)
        session.commit()
        session.refresh(post)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Erro ao atualizar o post")

    return {
        "mensagem": "Post atualizado com sucesso",
        "post_id": post.id,
        "campos_alterados": list(update_data.keys())
    }

@router_posts.post("/{publicacao_id}/like")
async def dar_like(
    publicacao_id: int, 
    db: Session = Depends(abrir_sessao),
    usuario_atual: User = Depends(verificar_token)
):
    
    publicacao = db.query(Publicacoes).filter(Publicacoes.id == publicacao_id).first()
    
    if not publicacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Publicação não encontrada"
        )

    # Verifica se o usuário já está na lista de quem curtiu
    if usuario_atual in publicacao.curtidas_por:
        # Se já curtiu, removemos a relação (Descurtir)
        publicacao.curtidas_por.remove(usuario_atual)
        acao = "removido"
    else:
        # Se não curtiu, adicionamos a relação (Curtir)
        publicacao.curtidas_por.append(usuario_atual)
        acao = "adicionado"

    db.commit()
    
    total_de_likes = len(publicacao.curtidas_por)

    return {
        "mensagem": f"Like {acao} com sucesso",
        "total_likes": total_de_likes,
        "curtido_pelo_usuario": acao == "adicionado" # Retorna True se curtiu, False se tirou
    }