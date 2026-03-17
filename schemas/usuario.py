from pydantic import BaseModel, ConfigDict
from typing import Optional

class CriarUsuarioSchema(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    nome : str
    usuario : str
    email : str
    senha : str
    admin : bool | None = False
    
    
class LoginSchema(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    email: str
    senha: str
    
class EditarUsuario(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    nome : Optional[str] = None
    usuario : Optional[str] = None
     
    
    
        
