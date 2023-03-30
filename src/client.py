import json
import socket
from config.env import env

PORT = env['server_port']
HOST = env['server_host']
BUFFER_SIZE = env['buffer_size']

create_user_data = {'id_operation': 'create_user', 'payload': {
    'name': 'Enrique Santos de Oliveira', 'email': 'santosenrique2121@gmail.com', 'age': 21}}

"a083e380-3104-4226-8bd2-23485b0bfd8d"

update_user_data_with_empty_payload = {
    'id_operation': 'update_user', 'payload': None}

get_users_data = {'id_operation': 'get_users'}
close_connection_data = {'id_operation': 'close_connection'}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    json_str = json.dumps(get_users_data)

    json_encoded = json_str.encode()
    s.sendall(json_encoded)
    response = s.recv(BUFFER_SIZE)

    json_response = json.loads(response.decode())
    print(json.dumps(json_response, indent=4))
