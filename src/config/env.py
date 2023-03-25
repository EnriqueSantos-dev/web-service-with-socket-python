import os

from dotenv import load_dotenv

load_dotenv()

env = {
    "server_port": int(os.environ.get('SERVER_PORT')),
    "server_host": os.environ.get('SERVER_HOST')
}
