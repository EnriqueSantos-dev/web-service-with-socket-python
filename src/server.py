import socket
import threading
import json
import services.users_service as users_service
from config.env import env
from utils.responses import *

PORT = env['server_port']
HOST = env['server_host']
BUFFER_SIZE = env['buffer_size']

operations_allowed = ['get_users', 'create_user',
                      'update_user', 'delete_user', 'get_user', 'close_connection']


class Server:
    def __init__(self, initial_socket) -> None:
        self.buffer_size = BUFFER_SIZE
        self.socket = initial_socket(socket.AF_INET, socket.SOCK_STREAM)

    def decode_data(self, data):
        try:
            raw_json = data.decode()
            if not raw_json:
                return None
            dict = json.loads(raw_json)
            return dict
        except Exception as e:
            raise Exception('Error on decode data', e)

    def on_connect(self, conn, address: str) -> None:
        while True:
            binary_data = conn.recv(self.buffer_size)
            message = self.decode_data(binary_data)

            if not message:
                conn.sendall(build_error_response(400, 'Bad Request'))
                break

            if (message['id_operation'] is None or message['id_operation'] not in operations_allowed):
                conn.sendall(build_error_response(405, 'Operation not found'))
                break

            match message['id_operation']:
                case 'close_connection':
                    conn.sendall(build_success_response(
                        {'message': 'Connection closed'}, '200'))
                    conn.close()

                case 'get_user':
                    id = message['payload'].get('id')
                    data = users_service.get_user(id)
                    conn.sendall(data)
                    break

                case 'get_users':
                    conn.sendall(users_service.get_users())
                    break

                case 'create_user':
                    payload = message['payload']
                    data = users_service.create_user(payload)
                    conn.sendall(data)
                    break

                case 'update_user':
                    payload = message['payload']

                    if (not payload):
                        conn.sendall(build_error_response(400, 'Bad Request'))
                        break

                    data = users_service.update_user(
                        payload.get('user_id'), payload['data'])

                    conn.sendall(data)

                case 'delete_user':
                    id = message['payload'].get('id')
                    data = users_service.delete_user(id)
                    conn.sendall(data)
                    break

        conn.close()
        print(f'Connection closed by {address}')

    def run(self, port: int, host: str) -> None:
        print(f'Server listener on {host}:{port}')
        self.socket.bind((host, port))
        self.socket.listen()

        while True:
            conn, addr = self.socket.accept()
            t = threading.Thread(target=self.on_connect, args=(conn, addr))
            t.start()


server = Server(socket.socket)
server.run(PORT, HOST)
