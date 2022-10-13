
CREATE_USER = """
**Cadastrar um novo usuário**
\nRequisitos:

- `name`: Deve conter o nome do usuário.
- `email`: Deve conter o email do usuário.
- `password`: Deve conter a senha do usuário.


*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_USER = """
**Pesquisar usuário pelo id**
\nRequisitos:

- `id`: inserir id do usuário

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_USERS = """
**Pesquisar lista de usuários**

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

GET_USERS_BY_EMAIL = """
**Pesquisar usuário pelo email**
\nRequisitos:

- `email`: inserir o email do usuário

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

UPDATE_USER = """
**Atualizar os dados de um usuário**
\nRequisitos:

- `name`: Opcionalmente pode conter o nome do usuário para atualizá-lo.
- `email`: Opcionalmente pode conter o email do usuário para atualizá-la.
- `password`: Opcionalmente pode conter a senha do usuário para que seja feita a alteração.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

DELETE_USER = """
**Deletar um usuário**
\nRequisitos:

- `user_id`: inserir o id do usuário

*Código HTTP 200 OK: aplicação funcionou corretamente.*
"""

