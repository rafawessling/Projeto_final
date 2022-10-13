
CREATE_ORDER = """
**Cria um order**
\nRequisitos:

- `userId`: Deve conter o id do usuário.
- `order_item`: Deve conter o order_item.
- `price`: calcula automaticamente o preço dos produtos no carrinho.
- `paid`: bool indicando o pagamento do order (permanentemente como falso).
- `created`: cria automaticamente o timestamp da data e hora de criação do order.
- `addressId`: Deve conter o id do endereço.


*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_ORDER = """
**Pesquisar o order pelo id**
\nRequisitos:

- `id`: inserir id do order

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""