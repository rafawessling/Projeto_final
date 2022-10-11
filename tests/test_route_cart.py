
from test_route_main import client

def test_add_product_to_chart():
    product =  {
        
                "name": "Mop Perfect Pro Giratório 360 com 3 Refis Esfregão e Balde Cesto Inox",
                "description": "Com uma concepção inovadora, baseada na teoria da centrifugação, apresenta um excelente poder de limpeza e 100% de centrifugação. Com um fantástico dispositivo de centrifugação você pode controlar o percentual de umidade do mop facilmente. Produzido em microfibra, o mop apresenta um grande poder de absorção de poeira ou água com secagem fácil, limpando de forma segura e eficiente. Seu elegante design faz com que gire 360 graus e permite chegar em qualquer canto onde antes não era possível.\nVantagens: centrifuga inox removível; rolha de vedação para facilitar o escoamento da agua; alça para carregamento mais resistente; eixo interno para facilitar a lavagem do refil; cabo com inclinação de 180°; cabo com sistema de trava on/off para regulagem de altura e função giratória; remove rapidamente o excesso de agua; material, mais resistente e durável dentre todos da categoria.\nDimensões:\nCabo: Altura max: 1,60m;\nBalde: Altura: 24 cm; Largura: 28 cm; Comprimento: 46 cm.",
                "code": "123456",
                "price": 169.89,
                "image": "https://a-static.mlcdn.com.br/800x560/balde-mop-pro-esfregao-com-cesto-inox-cabo-160-metros-com-3-refis-1-microfibra-1-limpeza-po-1-limpeza-pesada-perfect/gahe/5916911504/e594d771b7140096b37d35479097d3e1.jpeg",
                "stock": 5,
                "brand": "MOP",
                "color": "Azul",
                "material": "Balde plástico com cesto inox, cabo inox e refis de microfibra."
            }
    
    # se existir um carrinho retorna Ok
    response = client.post("/products/", json=product)
    assert response.json() == "OK"
    
    # se não existir um carrinho vinculado ao usuário, crie o carrinho e retornar OK
    user = {"id": 1, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    response = client.post("/user", json=user)
    assert response.json() == "OK"
    
    #Se não retorna falha / id_cart = 598652
    response = client.post("/carrinho/1/598652/")
    assert response.json().upper() == "FALHA"
    
    #Se não retorna falha se não houver este produto no carrinho
    response = client.post("/carrinho/598652/123456/")
    assert response.json().upper() == "FALHA"
    
    # senão adiciona produto ao carrinho e retornar OK; id_user = 1 e id_produto = 123456
    response = client.post("/carrinho/1/123456/")
    assert response.json().upper() == "OK"


def test_get_chart_by_user_id():
    
    #Verificando se exite um carrinho
    response = client.get("/carrinho/659856846/")
    assert response.json().upper() == "FALHA"
    
    #Adicionando products 
    product1 =  {
        
                "name": "Mop Perfect Pro Giratório 360 com 3 Refis Esfregão e Balde Cesto Inox",
                "description": "Com uma concepção inovadora, baseada na teoria da centrifugação, apresenta um excelente poder de limpeza e 100% de centrifugação. Com um fantástico dispositivo de centrifugação você pode controlar o percentual de umidade do mop facilmente. Produzido em microfibra, o mop apresenta um grande poder de absorção de poeira ou água com secagem fácil, limpando de forma segura e eficiente. Seu elegante design faz com que gire 360 graus e permite chegar em qualquer canto onde antes não era possível.\nVantagens: centrifuga inox removível; rolha de vedação para facilitar o escoamento da agua; alça para carregamento mais resistente; eixo interno para facilitar a lavagem do refil; cabo com inclinação de 180°; cabo com sistema de trava on/off para regulagem de altura e função giratória; remove rapidamente o excesso de agua; material, mais resistente e durável dentre todos da categoria.\nDimensões:\nCabo: Altura max: 1,60m;\nBalde: Altura: 24 cm; Largura: 28 cm; Comprimento: 46 cm.",
                "code": "200",
                "price": 2000,
                "image": "https://a-static.mlcdn.com.br/800x560/balde-mop-pro-esfregao-com-cesto-inox-cabo-160-metros-com-3-refis-1-microfibra-1-limpeza-po-1-limpeza-pesada-perfect/gahe/5916911504/e594d771b7140096b37d35479097d3e1.jpeg",
                "stock": 6,
                "brand": "MOP",
                "color": "Azul",
                "material": "Balde plástico com cesto inox, cabo inox e refis de microfibra."
            }
    product2 =  {
        
                "name": "Mop Perfect Pro Giratório 360 com 3 Refis Esfregão e Balde Cesto Inox",
                "description": "Com uma concepção inovadora, baseada na teoria da centrifugação, apresenta um excelente poder de limpeza e 100% de centrifugação. Com um fantástico dispositivo de centrifugação você pode controlar o percentual de umidade do mop facilmente. Produzido em microfibra, o mop apresenta um grande poder de absorção de poeira ou água com secagem fácil, limpando de forma segura e eficiente. Seu elegante design faz com que gire 360 graus e permite chegar em qualquer canto onde antes não era possível.\nVantagens: centrifuga inox removível; rolha de vedação para facilitar o escoamento da agua; alça para carregamento mais resistente; eixo interno para facilitar a lavagem do refil; cabo com inclinação de 180°; cabo com sistema de trava on/off para regulagem de altura e função giratória; remove rapidamente o excesso de agua; material, mais resistente e durável dentre todos da categoria.\nDimensões:\nCabo: Altura max: 1,60m;\nBalde: Altura: 24 cm; Largura: 28 cm; Comprimento: 46 cm.",
                "code": "201",
                "price": 2000,
                "image": "https://a-static.mlcdn.com.br/800x560/balde-mop-pro-esfregao-com-cesto-inox-cabo-160-metros-com-3-refis-1-microfibra-1-limpeza-po-1-limpeza-pesada-perfect/gahe/5916911504/e594d771b7140096b37d35479097d3e1.jpeg",
                "stock": 6,
                "brand": "MOP",
                "color": "Azul",
                "material": "Balde plástico com cesto inox, cabo inox e refis de microfibra."
            }
    product3 =  {
        
                "name": "Mop Perfect Pro Giratório 360 com 3 Refis Esfregão e Balde Cesto Inox",
                "description": "Com uma concepção inovadora, baseada na teoria da centrifugação, apresenta um excelente poder de limpeza e 100% de centrifugação. Com um fantástico dispositivo de centrifugação você pode controlar o percentual de umidade do mop facilmente. Produzido em microfibra, o mop apresenta um grande poder de absorção de poeira ou água com secagem fácil, limpando de forma segura e eficiente. Seu elegante design faz com que gire 360 graus e permite chegar em qualquer canto onde antes não era possível.\nVantagens: centrifuga inox removível; rolha de vedação para facilitar o escoamento da agua; alça para carregamento mais resistente; eixo interno para facilitar a lavagem do refil; cabo com inclinação de 180°; cabo com sistema de trava on/off para regulagem de altura e função giratória; remove rapidamente o excesso de agua; material, mais resistente e durável dentre todos da categoria.\nDimensões:\nCabo: Altura max: 1,60m;\nBalde: Altura: 24 cm; Largura: 28 cm; Comprimento: 46 cm.",
                "code": "202",
                "price": 2000,
                "image": "https://a-static.mlcdn.com.br/800x560/balde-mop-pro-esfregao-com-cesto-inox-cabo-160-metros-com-3-refis-1-microfibra-1-limpeza-po-1-limpeza-pesada-perfect/gahe/5916911504/e594d771b7140096b37d35479097d3e1.jpeg",
                "stock": 6,
                "brand": "MOP",
                "color": "Azul",
                "material": "Balde plástico com cesto inox, cabo inox e refis de microfibra."
            }
    client.post("/products/", json=product1)
    client.post("/products/", json=product2)
    client.post("/products/", json=product3)

    #Vinculando user ao produto dentro do carrinho
    user = {"id": 2, "name": "fulano", "email": "aaaa@bbbbb.com", "password": "12"}
    client.post("/user", json=user)

    client.post("/carrinho/2/200/")
    client.post("/carrinho/2/201/")
    client.post("/carrinho/2/202/")

    #Teste componentes do carrinho
    response = client.get("/carrinho/2/")
    assert "total_price" in response.json()
    assert "id_products/code" in response.json()
    assert "id_user" in response.json()
    assert "stock" in response.json()
    assert response.json()['stock'] == 3
    assert response.json()['total_price'] == 20.0
    assert len(response.json()['id_products/code']) == 200


#Deletando carrinho
def test_delete_carrinho():
    # Se não existir usuário com o id_user retornar falha
    response = client.delete("/carrinho/1987635132/")
    assert response.json().upper() == "FALHA"
    
    #Se existir deletar e retornar OK
    response = client.delete("/carrinho/2/")
    assert response.json().upper() == "OK"
    
    #Se não retorna FALHA
    response = client.delete("/carrinho/2/")
    assert response.json().upper() == "FALHA"
