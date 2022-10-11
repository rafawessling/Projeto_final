CREATE_CART = """
**Criar um carrinho para o usuário**
\nRequisitos:

- `user_id`: Deve conter o id do usuário.
- `order_items`: Deve conter as informações de `product_code` e `quantity` de produtos a
a serem inseridos no carrinho.
- `total_price`: Deve conter o valor total do carrinho.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe o carrinho for criado corretamente, retornará o status *"Cart has been created"*
e os dados do produto cadastrado. 
Caso já exista um carrinho para o `user_id` informado ou se o `product_code` não existir no 
banco de dados, retornará o status *"Error to create cart"*.
"""

GET_CART_BY_USER_ID = """
**Pesquisar carrinho pelo id do usuário**
\nRequisitos:

- `user_id`: Deve conter o id do usuário.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe existir carrinho para o `user_id` informado, retornará o carrinho.
Caso não exista carrinho para esse usuário, retornará None.
"""

DELETE_CART = """
**Excluir o carrinho do usuário**
\nRequisitos:

- `user_id`: Deve conter o `user_id` para deletar o carrinho vinculado à ele.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe o carrinho for deletado do banco de dados, retornará o status *"Cart has been deleted"*.
Caso o usuário não possua carrinho, retornará o status 
*"It was not possible to delete the cart"*.
"""
