from test_route_main import client
import logging

logging.basicConfig(level=logging.INFO, filename= "route_tests.log")

def test_create_product():
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
    
    #cria um produto e retornar OK
    response = client.post("/products/", json=product)
    assert response.json().upper() == "OK"
    
    # Se tiver outro produto com o mesmo ID retornar falha
    response = client.post("/products/", json=product)
    assert response.json().upper() == "FALHA"
    

def test_delete_product():
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
    
    client.post("/products/", json=product)
    # deleta produto correspondente ao id_produto e retornar OK
    response = client.delete("/products/123456/")
    assert response.json().upper() == "OK"
    
    # Se não existir produto com o id_produto retornar falha
    response = client.delete("/products/123456/")
    assert response.json().upper() == "FALHA"
    
    # Se não existir produto com o id_produto retornar falha
    response = client.delete("/products/56/")
    assert response.json().upper() == "FALHA"
    