# Web Service With Python and Sockets
---

## Descrição do sistema:
O sistema trata-se de um web service feito com o módulo **socket** do **python**. Se tratadando de persistência de dados o sistema utiliza banco de dados em memória para armazenar os dados dos usuários, o seu comportamento é baseado em um CRUD de usuários, onde é possível criar, listar, atualizar e deletar usuários, com funcionamento semelhante a uma **Api Rest** e com o protocolo de **Resquest** e **Response** semelhante ao **HTTP**. Ademais, para a comunicação entre o cliente e o servidor as mensagens são enviadas em formato com **JSON** e recebidas como **JSON**.

## Interfaces para request e response:

### Request:

A requisição é feita em formato JSON, e deve conter dois campos: **id_operation**: é a operação que está sendo executada, **payload**: um objeto que contém o payload da requisição, esse objeto pode se modificar de acordo com a operação.

```python
  { "id_operation":  str,  "payload": obj }
```

### Response:

A resposta pode ser de dois tipos: com **Payload** ou com **Error**.

Payload:

```python
  { "payload": obj, "code": int }
```

Error:

```python
  { "error": int, "error_message": str }
```

### Erros do sistema

**Not Found**: esse error ocorre quando não é encontrado um rercuso no sistema.

```python
  { "error": 404, "error_message": "Not Found" }
```

**User Not Found**: esse error ocorre quando não é encontrado um usuário no sistema.

```python
  { "error": 404, "error_message": "User Not Found" }
```

**Internal Server Error**: esse error ocorre quando alguma exeption é lançada no servidor e acontece o tratamento dela.

```python
  { "error": 500, "error_message": "Internal Server Error" }
```

**Bad Request**: esse error ocorre quando o cliente envia uma requisição com um payload inválido.

```python
  { "error": 400, "error_message": "Bad Request" }
```

## Operações do sistema:

### Listar usuários:

```python
  Request: { "id_operation": "get_users", "payload": {} }

  Response:
  {
    "payload": [
      {
        "id": int,
        "name": str,
        "email": str,
        "age": int,
        "created_at": str,
        "updated_at": str
      }
    ],
    "code": 200
  }

  Response:
  {
    "error": 400 | 500,
    "error_message": "Internal Server Error" | "Bad Request"
  }
```

### Buscar um único usuário:

```python
  Request: { "id_operation": "get_user", "payload": { "user_id": int } }

  Response:
  {
     "payload": {
       "id": int,
       "name": str,
       "email": str,
       "age": int,
       "created_at": str,
       "updated_at": str
     },
    "code": 200
  }

  Response:
  {
    "error": 400 | 404 | 500,
    "error_message": "User Not Found" | "Internal Server Error" | "Bad Request"
  }
```

### Criar um usuário:

```python
  Request:
  {
    "id_operation": "create_user",
    "payload": {
      "name": str,
      "email": str,
      "age": int,
    }
  }

  Response:
  {
    "payload": {
      "id": int,
      "name": str,
      "email": str,
      "age": int,
      "created_at": str,
      "updated_at": str
    },
    "code": 201
  }

  Response:
  {
    "error": 400 | 500,
    "error_message": "Internal Server Error" | "Bad Request"
  }
```

### Deletar um usuário pelo id:

```python
  Request:
  { "id_operation": "delete_user", "payload": { "user_id": int } }

  Response:
  {
    "payload": {},
    "code": 204
  }

  Response:
  {
    "error": 400 | 404 | 500,
    "error_message": "User Not Found" | "Internal Server Error" | "Bad Request"
  }
```

### Atualizar um usuário:

```python
  Request:
  {
    "id_operation": "update_user",
    "payload": {
      "user_id": int,
      "data": {
        "name": str,
        "email": str,
        "age": int,
      }
    }
  }

  Response:
  {
    "payload": {
      "id": int,
      "name": str,
      "email": str,
      "age": int,
      "created_at": str,
      "updated_at": str
    },
    "code": 200
  }

  Response:
  {
    "error": 400 | 404 | 500,
    "error_message": "User Not Found" | "Internal Server Error" | "Bad Request"
  }
```
