
CREATE_ADDRESS = """
**Cadastrar um novo endereço**
\nRequisitos:

- `street`: Deve conter a rua do usuário.
- `num`: Deve conter o número da residência.
- `cep`: Deve conter o cep do endereço.
- `city`: Deve conter a cidade do usuário.
- `state`: Deve conter o estado do usuário.
- `userId`: Deve conter o id do usuário.


*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_ADDRESS = """
**Pesquisar endereços pelo id**
\nRequisitos:

- `id`: inserir id do endereço

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_ALL_ADDRESSES = """
**Pesquisar lista de endereços pelo id do usuário**
\nRequisitos:

- `userId`: inserir o id do usuário

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

DELETE_ADDRESS = """
**Deletar um endereço**
\nRequisitos:

- `id`: inserir o id do endereço

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

DELETE_ALL_ADDRESSES = """
**Deletar lista de endereços**
\nRequisitos:

- `userId`: inserir o id do usuário


*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""
