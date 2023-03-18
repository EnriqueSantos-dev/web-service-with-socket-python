# web-service-with-socket-python

## Interfaces para request e response:

### Request:

A requisição é feita em formato JSON, e deve conter dois campos: **id_operation**: é a operação que está sendo executada, **payload**: um objeto que contém o payload da requisição, esse objeto pode se modificar de acordo com a operação.

```python
  { "id_operation":  str,  "payload": obj }
```

### Response:

A resposta pode ser de dois tipos: com **data** ou com **error**.

Data:

```python
  { "payload": obj, "code": int }
```

Error:

```python
  { "error": int, "error_message": str }
```

### Errors do sistema

**Error usuário não encontrado**: esse error ocorre quando não é encontrado um usuário que o client está buscando no sistema.

```python
  { "error": 404, "error_message": "User Not Found" }
```

**Internal Server Error**: esse error ocorre quando acontece algum error interno no servidor, quando uma chamada ao banco retorna algum erro nos mandamos erro para o client.

```python
  { "error": 500, "error_message": "Internal Server Error" }
```

## Operações do sistema:

### Listar usuários:

```python
  id_operation: "get_users" -> Lista todos os usuários.

  Request: { "id_operation": "get_users", "payload": {} }
  
  Response: {
    "payload": [
      {
        "id": int,
        "name": str,
        "email": str,
        "created_at": str,
      }
    ],
    "code": 200
  }

  Response: {
    "error": 404  | 500,
    "error_message": "User Not Found" | "Internal Server Error"
  }
```

### Buscar um único usuário:

```python
  id_operation: "get_user" -> Busca um usuário pelo id.

  Request: { "id_operation": "get_user", "payload": { "user_id": int } }
  
  Response: {
    "payload": {
      "id": int,
      "name": str,
      "email": str,
      "created_at": str,
    },
    "code": 200
  }
    
  Response: {
    "error": 404  | 500,
    "error_message": "User Not Found" | "Internal Server Error"
  }
```

### Deletar um usuário pelo id:

```python
  id_operation: "delete_user" -> Deleta um usuário pelo id.

  Request: { "id_operation": "delete_user", "payload": { "user_id": int } }
  
  Response: {
      "payload": {},
      "code": 200
  }
    
  Response: {
    "error": 404  | 500,
    "error_message": "User Not Found" | "Internal Server Error"
  }
```

### Criar um usuário:

```python
  id_operation: "create_user" -> Cria um usuário.

  Request: {
    "id_operation": "create_user",
    "payload": { "name": str, "email": str }
  }

  Response: {
    "payload": {
      "id": int,
      "name": str,
      "email": str,
      "created_at": str,
    },
    "code": 201
  }

  Response: {
    "error": 404  | 500,
    "error_message": "User Not Found" | "Internal Server Error"
  }
```

### Atualizar um usuário:

```python
  id_operation: "update_user" -> Atualiza um usuário.

  Request: {
    "id_operation": "update_user",
    "payload": { "user_id": int, "name": str, "email": str }
  }

  Response: {
    "payload": {
      "id": int,
      "name": str,
      "email": str,
      "created_at": str,
    },
    "code": 200
  }

  Response: {
    "error": 404  | 500,
    "error_message": "User Not Found" | "Internal Server Error"
  }
```
