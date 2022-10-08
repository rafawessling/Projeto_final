CREATE_PRODUCT = """
**Cadastrar um novo produto**
\nRequisitos:

- `name`: Deve conter o nome do produto.
- `description`: Deve conter a descrição do produto.
- `code`: Deve conter o código do produto.
- `price`: Deve conter o preco do produto e deve ser maior ou igual a R$ 0.01.
- `image`: Deve conter a imagem do produto.
- `stock`: Deve conter o número de estoque do produto e deve ser maior ou igual a 1.
- `brand`: Opcionalmente pode conter a marca do produto.
- `color`: Opcionalmente pode conter a(s) cor(es) do produto.
- `material`: Opcionalmente pode conter o(s) material(is) do produto.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe o produto for cadastrado corretamente, retornará o status *"Product has been created"*
e os dados do produto cadastrado. 
Caso já exista um produto com o mesmo `code`, retornará o status *"Product already exists"*.
"""

GET_PRODUCT_NAME = """
**Pesquisar produtos pelo nome**
\nRequisitos:

- `name`: Deve conter o termo (nome ou parte do nome) que deseja realizar a pesquisa.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe forem encontrados produtos no banco de dados que possuem o termo pesquisado no 
campo `name`, retornará uma lista com esses produtos.
Caso não exista produto no banco 
de dados com o termo pesquisado, retornará o status *"No products found"*.
"""

GET_PRODUCT_CODE = """
**Pesquisar produtos pelo código**
\nRequisitos:

- `code`: Deve conter o `code` informado no cadastro do produto para encontrá-lo.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe for encontrado produto com o código informado, retornará os dados do produto. 
Caso não exista produto no banco de dados com o `code` informado, retornará o status
*"Product not found"*.
"""

DELETE_PRODUCT = """
**Deletar um produto**
\nRequisitos:

- `code`: Deve conter o `code` informado no cadastro do produto para deletá-lo.

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe o produto for deletado do banco de dados, retornará o status *"Deleted product"*.
Caso não exista produto no banco de dados  com o `code` informado, retornará o status 
*"Product not found"*.
"""

UPDATE_PRODUCT = """
**Atualizar os dados de um produto**
\nRequisitos:

- `name`: Opcionalmente pode conter o nome do produto para atualizá-lo.
- `description`: Opcionalmente pode conter a descrição do produto para atualizá-la.
- `code`: Deve conter o código do produto que se deseja fazer a alteração.
- `price`: Opcionalmente pode conter o preço do produto para atualizá-lo, devendo ser maior ou igual a R$ 0.01.
- `image`: Opcionalmente pode conter a imagem do produto para atualizá-la.
- `stock`: Opcionalmente pode conter o estoque do produto para atualizá-lo, devendo ser maior ou igual a 1.
- `brand`: Opcionalmente pode conter a marca do produto para atualizá-la.
- `color`: Opcionalmente pode conter a(s) cor(es) do produto para atualizá-la(s).
- `material`: Opcionalmente pode conter o(s) material(is) do produto para atualizá-lo(s).

*Código HTTP 200 OK: aplicação funcionou corretamente.*
\nSe o produto for atualizado com sucesso, retornará o status *"Updated product"*.
Caso não exista produto no banco de dados com o `code` informado ou os dados informados 
sejam iguais ao produto existente, retornará o status *"Product could not be updated"*.
"""
