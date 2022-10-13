from test_route_main import client, TestClient
import logging 

logging.basicConfig(level=logging.INFO, filename= "route_tests.log")

# Teste para validar id do endereço 
def test_doesnt_create_address_by_invalid_id():
    data = { 
            "id":2,
            "street": "rua rua",
            "num": "200",
            "cep": "5555555",
            "city": "cidade",
            "state": "estado"
            }
    response = client.post("/address/1/", json=data)
    assert response.json().upper() == "FALHA"
    
# senão cria um endereço, vincula ao usuário e retornar OK
def test_create_address_by_id():
    data =  {"id": 1, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    client.post('/user', json=data)    
    data = { 
            "id":5,
            "street": "rua rua",
            "num": "200",
            "cep": "5555555",
            "city": "cidade",
            "state": "estado"
            }
    response = client.post("/address/1/", json=data)
    assert response.json().upper() == "OK"
    
# Se não existir usuário com o id_usuario retornar falha
def test_doesnt_get_address_by_invalid_id():
    response = client.get("/user/42/address")
    assert response.json().upper() == "FALHA"

# caso o usuário não possua nenhum endereço vinculado a ele, retornar uma lista vazia
def test_get_address_of_user_without_address():
    new_user = {"id": 3, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    client.post("/user", json=new_user)
    response = client.get("/user/3/address")
    assert response.json() == []
    
    

# senão retornar uma lista de todos os endereços vinculados ao usuário
def test_get_address_of_user_with_one_address():
    response = client.get("/user/1/address")
    assert len(response.json()) == 1

def test_get_address_of_user_with_two_address():
    data = { 
            "id":6,
            "street": "rua rua rua",
            "num": "22000",
            "cep": "777777",
            "city": "cidade",
            "state": "estado estado"
            }
    client.post("/address/1/", json=data)
    response = client.get("/user/1/address")
    assert len(response.json()) == 2
    

# Se não existir endereço com o id_endereco retornar falha,
def test_dont_delete_address_by_invalid_address_id():
    response = client.delete("/address/7894/")
    assert response.json().upper() == "FALHA"
    

# senão deleta endereço correspondente ao id_endereco e retornar OK
def test_dont_delete_address_by_invalid_address_id():
    new_user = {"id": 1, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    client.post("/user", json=new_user)
    data = { 
            "id":6,
            "street": "rua rua rua",
            "num": "22000",
            "cep": "777777",
            "city": "cidade",
            "state": "estado estado"
            }
    client.post("/address/1/", json=data)
    response = client.delete("/address/6/")
    assert response.json().upper() == "OK"
    
    #Se não retorna falha
    response = client.delete("/address/6/")
    assert response.json().upper() == "FALHA"
    
