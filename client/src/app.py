import json
import socket
from config.env import env

PORT = env['server_port']
HOST = env['server_host']
BUFFER_SIZE = env['buffer_size']

create_user_raw = {'id_operation': 'create_user', 'payload': {
    'name': 'Enrique Santos de Oliveira', 'email': 'santosenrique2121@gmail.com', 'age': 21}}
update_user_raw = {
    'id_operation': 'update_user', 'payload': {
        "user_id": None, 'data': {
            'name': None, 'email': None, 'age': None
        }
    }}
get_users_raw = {'id_operation': 'get_users'}
close_connection_data = {'id_operation': 'close_connection'}
get_user_raw = {'id_operation': 'get_user', 'payload': {'user_id': None}}
delete_user_raw = {'id_operation': 'delete_user', 'payload': {'user_id': None}}


class Client:
    def __init__(self, host: str, port: int, buffer_size: int) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer_size = buffer_size
        self.host = host
        self.port = port

    def connect(self):
        self.socket.connect((self.host, self.port))
        return self.socket

    def send_data(self, data):
        try:
            self.socket.sendall(json.dumps(data).encode())
            return json.loads(self.socket.recv(self.buffer_size).decode())
        except Exception as e:
            print(e)
            print('Error on send data')

    def close_connection(self):
        self.socket.sendall(json.dumps(close_connection_data).encode())
        print(
            f"{json.dumps(json.loads(self.socket.recv(self.buffer_size).decode()), indent=2)}")


if __name__ == '__main__':
    client = Client(HOST, PORT, BUFFER_SIZE)
    client.connect()

    while True:
        print('1 - Criar usuário')
        print('2 - Atualizar usuário')
        print('3 - Listar usuários')
        print('4 - Buscar um usuário')
        print('5 - Delete um usuário')
        print('6 - Fechar conexão')
        print('7 - Forçar erro no servidor')
        print('8 - Força erro de operação não encontrada')

        try:
            op = int(input('Digite a operação: '))

            match op:
                case 6:
                    client.close_connection()
                    break
                case 1:
                    res = input(
                        'Deseja criar o usuários com valores padrões? (y/n): ').strip().lower() == 'y'

                    if res:
                        print(json.dumps(client.send_data(
                            create_user_raw), indent=2))
                    else:
                        create_user_raw['payload']['name'] = input(
                            'Digite o nome: ').strip()
                        create_user_raw['payload']['email'] = input(
                            'Digite o email: ').strip()
                        create_user_raw['payload']['age'] = int(
                            input('Digite a idade: ').strip())
                        print(json.dumps(client.send_data(
                            create_user_raw), indent=2))
                case 2:
                    input('Deseja atualiar o nome do usuário? (y/n): ').strip().lower() == 'y' and \
                        update_user_raw['payload']['data'].update(
                            {'name': input('Digite o nome: ').strip()})
                    input('Deseja atualiar o email do usuário? (y/n): ').strip().lower() == 'y' and \
                        update_user_raw['payload']['data'].update(
                            {'email': input('Digite o email: ').strip()})
                    input('Deseja atualiar a idade do usuário? (y/n): ').strip().lower() == 'y' and \
                        update_user_raw['payload']['data'].update(
                            {'age': int(input('Digite a idade: ').strip())})

                    user_id = input('Digite o id do usuário: ').strip()
                    update_user_raw['payload']['user_id'] = user_id

                    print(json.dumps(client.send_data(update_user_raw), indent=2))
                case 3:
                    print(json.dumps(client.send_data(get_users_raw), indent=2))
                case 4:
                    user_id = input('Digite o id do usuário: ').strip()
                    get_user_raw['payload']['user_id'] = user_id
                    print(json.dumps(client.send_data(get_user_raw), indent=2))
                case 5:
                    user_id = input('Digite o id do usuário: ').strip()
                    delete_user_raw['payload']['user_id'] = user_id
                    print(json.dumps(client.send_data(delete_user_raw), indent=2))
                case 7:
                    print(json.dumps(client.send_data({}), indent=2))
                case 8:
                    print(json.dumps(client.send_data(
                        {'id_operation': 'not_found'}), indent=2))
                case _:
                    print('Operação não encontrada!')
        except KeyboardInterrupt:
            print('\nCliente desconectando devido a interrupção do usuário!')
            client.close_connection()
            exit(1)
