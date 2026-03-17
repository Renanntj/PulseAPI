from pydantic import BaseModel, ConfigDict
from typing import Optional

class AutorSchema(BaseModel):
    usuario: str 
    model_config = ConfigDict(from_attributes=True)

class PublicacaoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None


class PublicacaoSchema(PublicacaoBase):
    id: int
    autor: AutorSchema

    model_config = ConfigDict(from_attributes=True) 

class EditarPost(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    
    titulo: Optional[str] = None
    descricao: Optional[str] = None