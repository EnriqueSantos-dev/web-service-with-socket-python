import os

from dotenv import load_dotenv

load_dotenv()

env = {
    "server_port": 8080,
    "server_host": os.environ.get('SERVER_HOST') or "localhost",
    "buffer_size": int(os.environ.get('BUFFER_SIZE') or 2048),
}
