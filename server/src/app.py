import socket
import threading
import services.users_service as users_service
from config.env import env
from utils.responses import *

PORT = env['server_port']
HOST = env['server_host']
BUFFER_SIZE = env['buffer_size']

operations_allowed = ['get_users', 'create_user',
                      'update_user', 'delete_user', 'get_user', 'close_connection']


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.buffer_size = BUFFER_SIZE
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen()

        print(f'Server listener on {self.host}:{self.port}')

        while True:
            conn, addr = self.socket.accept()
            t = threading.Thread(target=self.handle_client, args=(conn, addr))
            t.start()

    @staticmethod
    def decode_data(data):
        try:
            raw_json = data.decode()
            if not raw_json:
                return None
            return json.loads(raw_json)
        except Exception as e:
            raise Exception('Error on decode data', e)

    def handle_client(self, client, addr):
        host_client, port_client = addr
        print(f"New connection from '{host_client}:{port_client}'")

        while True:
            try:
                data = client.recv(self.buffer_size)
                message = Server.decode_data(data)

                if message is None or message['id_operation'] is None:
                    client.sendall(build_error_response(400, 'Bad Request'))

                match message['id_operation']:
                    case 'close_connection':
                        print(f"Connection closed from '{host_client}:{port_client}'")
                        client.sendall(build_success_response({'message': 'Connection closed'}, 200))
                        client.close()
                        break
                    case 'get_user':
                        user_id = message['payload'].get('user_id')
                        data = users_service.get_user(user_id)
                        client.sendall(data)
                    case 'get_users':
                        client.sendall(users_service.get_users())
                    case 'update_user':
                        payload = message['payload']
                        if not payload:
                            client.sendall(build_error_response(400, 'Bad Request'))
                        data = users_service.update_user(payload.get('user_id'), payload['data'])
                        client.sendall(data)
                    case 'create_user':
                        payload = message['payload']
                        data = users_service.create_user(payload)
                        client.sendall(data)
                    case 'delete_user':
                        user_id = message['payload'].get('user_id')
                        data = users_service.delete_user(user_id)
                        client.sendall(data)
                    case _:
                        client.sendall(build_error_response(404, 'Not Found'))
            except Exception as e:
                client.sendall(build_error_response(500, 'Internal Server Error'))


if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.start()
