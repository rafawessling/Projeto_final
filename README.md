# Carrinho de compras - Limpeza

<p align="center"><a href = "#"><img src = "imageLuizaCode.png" height=450 /></a></p>

> O objetivo deste projeto foi criar um sistema de **carrinho de compras** e **pedidos** utilizando _Python, FastAPI e MongoDB_, trazendo informações de usuário, endereço e produtos, com foco na categoria de **Limpeza**.

> Esta entrega engloba o **CRUD** _(criação, leitura, atualização e remoção dos dados)_ para usuário, endereço, produto, carrinho de compras e pedido, bem como o _tratamento de exceções, validações e testes unitários_. O projeto também contempla a hospedagem e disponibilização da aplicação pelo _Render_ e documentação utilizando o _Swagger_.

- A aplicação está disponível no _link_ abaixo:
  - https://shoppingcart-cleaning.onrender.com/docs#/

---

**Índice**

1.  [Instalação](#instalacao)
2.  [Tecnologias utilizadas](#tecnoutilizadas)
3.  [Bibliotecas utilizadas](#bibliotecasutilizadas)
4.  [Desenvolvimento do projeto](#desenvolvimentoprojeto)
5.  [Desenvolvedoras do projeto](#desenvolvedoras)

---

<div id='instalacao'/>

## 1. Instalação:

- Criar e ativar o ambiente virtual:

  ```
  $ python3 -m venv venv
  ```

  Linux:

  ```
  $ source venv/scripts/activate
  ```

  Windows:

  ```
  $ .\venv\Scripts\activate
  ```

  <p></p>

- Instalar os requirements:

  ```
  $ pip install -r requirements.txt
  ```

  <p></p>

- Criar arquivo que contenha as variáveis de ambiente:

  ```
  $ touch .env
  ```

  No arquivo `.env`, adicionar a seguinte variável:

  ```
  DATABASE_URI = "link para conexão com o bando de dados"
  ```

  <p></p>

- Executar a aplicação:

  ```
  $ uvicorn source.main:app --reload
  ```

  <p></p>

- Routes:

  ```
  url: http://localhost:8000/docs
  ```

  <p></p>

- _Link_ para consultar a aplicação hospedada pelo _Render_:
  ```
  url: https://shoppingcart-cleaning.onrender.com/docs#/
  ```

<div id='tecnoutilizadas'/>

## 2. Tecnologias utilizadas:

Na realização deste trabalho, foram utilizadas as seguintes tecnologias:

- Git e GitHub
- Python v3.10.4
- Framework FastAPI
- MongoDB
- Docker
- Render
- Swagger

<div id='bibliotecasutilizadas'/>

## 3. Bibliotecas utilizadas:

As bibliotecas utilizadas para o desenvolvimento deste projeto foram:

- fastapi v0.85.0
- uvicorn v0.18.3
- motor v3.0.0
- pydantic v1.10.2
- email-validator v1.2.1
- pymongo v4.2.0
- python-dotenv v0.21.0
- dnspython v2.2.1

<div id='desenvolvimentoprojeto'/>

## 4. Desenvolvimento do projeto:

Para o desenvolvimento deste projeto, foram levados em consideração os seguintes pontos:

- O usuário pode possuir mais do que um endereço cadastrado;
- O `code` informado para cadastro de produtos é o código informado pelo fornecedor/vendedor e que será utilizado para leitura, atualização e remoção do produto;
- Os produtos informados no momento de criação do carrinho de compras devem estar cadastrados no banco de dados;
- O usuário só pode ter um carrinho de compras vinculado à sua conta;
- O usuário pode ter mais do que um pedido vinculado à sua conta;
- Foi criado o _schema_ `order_items` para facilitar a criação do carrinho de compras e pedido, considerando que é o equivalente a cada linha de produtos diferentes no carrinho de compras ou pedido. Dessa forma, `order_items` informa o produto e a quantidade de itens daquele produto;
- Para armazenamento de dados, foi utilizada a opção _MongoDB_ disponível pela _cloud_ Atlas;
- Optou-se por aplicar a conteinerização neste projeto, em que a aplicação é executada dentro de um _Docker contêiner_;
- Foi decidido utilizar uma estratégia simples de _Continuos Delivery_, utilizando o _Render_ para hospedar e disponibilizar a aplicação;
- Optou-se por documentar a API utilizando o _Swagger._

<div id='desenvolvedoras'/>

## 5. Desenvolvedoras do projeto:

#### **Bruna Faleiros**

- **[*Linkedin*] : https://www.linkedin.com/in/bruna-faleiros-48a19573/**
- **[*GitHub*] : https://github.com/brufis**

#### **Giulia Gabriella**

- **[*Linkedin*] : https://www.linkedin.com/in/giulia-gabriella-de-lima-santos/**
- **[*GitHub*] : https://github.com/giugabriella**

#### **Nicole Maia**

- **[*Linkedin*] : https://www.linkedin.com/in/nicole-maia-bbb7aa17b/**
- **[*GitHub*] : https://github.com/nickmaia**

#### **Rafaela Wessling Oening**

- **[*Linkedin*] : https://www.linkedin.com/in/rafaela-wessling/**
- **[*GitHub*] : https://github.com/rafawessling**
