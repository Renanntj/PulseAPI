import pytest


def test_ver_perfil_de_usuario(client):  
    payload = {
        "nome": "Renan",
        "usuario": "renan",
        "email": "renan@gmail.com",
        "senha": "123teste",
    }

    client.post("user/criar-usuario/", json=payload)    
    
    response = client.get(f"user/ver-perfil/{payload['usuario']}/")
    
    assert response.status_code == 200

def test_criar_usuario_com_dados_validos(client): # testa criação de usuario com dados validos  
    payload = {
        "nome": "Renan",
        "usuario": "renan",
        "email": "renan@gmail.com",
        "senha": "123teste",
    }

    response = client.post("user/criar-usuario/", json=payload)    
    
    assert response.status_code == 201
    
def test_criar_usuario_com_email_repetido(client): # testa criação de usuario com o mesmo email
    
    payload = {
        "nome": "Renan",
        "usuario": "renan",
        "email": "renan@gmail.com",
        "senha": "123teste",
    }
    client.post("user/criar-usuario", json=payload) # cria pela primeira vez o email
    
    response = client.post("user/criar-usuario", json=payload) # repete a criação com o mesmo email que resulta no erro [400]
    assert response.status_code == 400
    
def test_criar_usuario_com_username_invalido(client):
    payload = {
        "nome": "Renan",
        "usuario": "USUARIO INVALIDO", # Para validar o nome de usuario é preciso que ele seja todo minusculo, e somente letra, numeros e _, -, . são permitos.
        "email": "renan@gmail.com",
        "senha": "123teste",
    }
    
    response = client.post("user/criar-usuario", json=payload)
    
    assert response.status_code == 400
    

    
