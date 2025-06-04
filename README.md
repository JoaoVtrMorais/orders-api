# Orders API

API RESTful para gerenciamento de pedidos, desenvolvida com Flask e MongoDB.

## Sobre

Este projeto é uma API simples para operações de criação, leitura, atualização e exclusão (CRUD) de pedidos. Foi desenvolvida com Flask e utiliza MongoDB como banco de dados.

## Tecnologias

- Python 3.12  
- Flask  
- Flask-RESTful  
- Flask-PyMongo  
- pymongo  
- MongoDB

## Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/JoaoVtrMorais/orders-api.git
cd orders-api
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Certifique-se de que o MongoDB está rodando localmente (ou configure a URI no run.py).

5. Execute a aplicação:

```bash
python run.py
```
A API ficará disponível em http://localhost:5000/.

# Endpoints

- GET /orders – Lista todos os pedidos

- GET /orders/<order_id> – Retorna um pedido pelo ID

- POST /orders – Cria um novo pedido

- PUT /orders/<order_id> – Atualiza um pedido existente

- DELETE /orders/<order_id> – Deleta um pedido
