import logging
from test_route_main import client

logging.basicConfig(level=logging.INFO, filename= "route_tests.log")

# Teste para criar um usuario e se há outro usuario com o mesmo ID retorna falha
def test_create_user_same_id():
    data = {"id": 1, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    response = client.post('/user', json=data)
    assert response.json().upper() == "FALHA"

# se o email não tiver o @ retornar falha
def test_email_incorrect():
    data = {"id": 1, "name": "fulano", "email": "aaaabbbbb.com", "password": "12"}
    response = client.post('/user', json=data)
    assert response.json().upper() == "FALHA"

# senha tem que ser maior a 3 caracteres,
def test_incorrect_password():
    data = {"id": 1, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    response = client.post('/user', json=data)
    assert response.json().upper() == "FALHA"

# Criar um usuário
def test_create_user():
    data = {"id": 5, "name": "beltrano", "email": "aaaa@bbbbb.com", "password": "123"}
    response = client.post('/user', json=data)
    assert response.json().upper() == "OK"


# Se o id do usuário existir, retornar os dados do usuário
def test_get_user_by_id():
    data = {"id": 8, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    client.post('/user', json=data)
    response = client.get('/user?id=8')
    assert response.json()['nome'] == "fulano"

# Se não existir retornar falha
def test_get_user_incorrect_id():
    response = client.get('/user?id=4')
    assert response.json().upper() == "FALHA"


# Se existir um usuario com o mesmo nome, retorna os dados do usuario
def test_get_user_by_name():
    data = {"id": 5, "nome": "Beltrano", "email": "aa@bb.com", "password": "123456"}
    client.post('/user', json=data)
    response = client.get('/user/nome?nome=Beltrano')
    assert response.json() == {"id": 5, "name": "Beltrano", "email": "aa@bb.com", "password": "123456"}

# Se não existir retornar falha
def test_dont_get_user_by_incorrect_name():
    response = client.get('/user/nome?nome=Sicrano')
    assert response.json().upper() == "FALHA"

# Se o id do usuário existir, deletar o usuário e retornar OK
def test_delete_user_by_id():
    data = {"id": 80, "name": "Fulano", "email": "aa@aa.com", "password": "1234"}
    client.post('/user', json=data)
    response = client.delete('/user/?id=80')
    assert response.json().upper() == "OK"
    response = client.get('/user?id=80')
    assert response.json().upper() == "FALHA"

# Se não existir retornar falha
def test_delete_user_by_invalid_id():
    response = client.delete('/user/?id=42')
    assert response.json().upper() == "FALHA"


def test_show_email():
        users = [
            {"id":291, "name": "fulano", "email": "aaaa@email.com", "password": "321"},
            {"id":292, "name": "beltrano", "email": "bbbbb@email.com", "password": "432"},
            {"id":294, "name": "sicrano", "email": "cccc@dotemail.com", "password": "421"},
        ]
        for user in users:
            client.post("/user", json=user)
        
        # Retornar todos os emails que possuem o mesmo domínio
        response = client.get("/users/emails/?dominio=email")
        assert len(response.json()) == 2
        
        # Se não existir retornar falha
        response = client.get("/users/emails/?dominio=doemail")
        assert response.json().upper() == "FALHA"