## Web service com Python e Sockets

## Descrição do sistema:

O sistema trata-se de um web service feito com o módulo **socket** do **python**. Se tratadando de persistência de dados o sistema utiliza banco de dados em memória para armazenar os dados dos usuários, o seu comportamento é baseado em um CRUD de usuários, onde é possível criar, listar, atualizar e deletar usuários, com funcionamento semelhante a uma **Api Rest** e com o protocolo de **Resquest** e **Response** semelhante ao **HTTP**. Ademais, para a comunicação entre o cliente e o servidor as mensagens são enviadas em formato **JSON** e recebidas como **JSON** também.

## Docker images

Esse projeto possui duas imagens docker, uma para o servidor e outra para o cliente, para que o projeto possa ser executado é necessário ter o docker instalado na máquina.

### Imagem para o servidor

```docker
docker pull dockerhubenrique/dockerhub:server_socket
```

### Imagem para o client

```docker
docker pull dockerhubenrique/dockerhub:client_socket
```

## Como rodar o projeto com o docker compose

```docker
docker compose up --remove-orphans
```

A imagem do cliente necessita de interatividade no terminal para funcionar corretamente, por isso é necessário rodar o comando abaixo em outra aba do terminal para que o cliente possa ser executado corretamente.

```docker
docker exec -it client python src/app.py
```

## Como rodar o projeto sem o docker compose e conectar os containers manualmente

### Criar uma network para conectar os containers

```docker
docker network create app-socket
```

### Servidor

```docker
 docker run --rm \
    --network=app-socket \
    --name server \
    -p 8080:8080 \
    -e SERVER_HOST=server \
    dockerhubenrique/dockerhub:server_socket

```

### Cliente

```docker
docker run --rm \
    --network=app-socket \
    --name client \
    -d \
    -e SERVER_HOST=server \
    dockerhubenrique/dockerhub:client_socket;

docker exec -it client python src/app.py
```
