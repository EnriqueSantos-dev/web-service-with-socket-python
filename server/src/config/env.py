import os

from dotenv import load_dotenv

load_dotenv()

env = {
    "server_port": int(os.environ.get('SERVER_PORT')) if os.environ.get('SERVER_PORT') else 8080,
    "server_host": os.environ.get('SERVER_HOST') or "localhost",
    "buffer_size": int(os.environ.get('BUFFER_SIZE')) if os.environ.get('BUFFER_SIZE') else 2048,
}
