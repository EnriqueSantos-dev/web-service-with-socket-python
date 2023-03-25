import json
from typing import Any


def build_success_response(payload: Any, code: int):
    json_data = {'payload': payload, 'code': code}
    encoded_data = json.dumps(json_data).encode()
    return encoded_data


def build_error_response(error_code: int, error_message: str):
    json_data = {'error': error_code, 'error_message': error_message}
    encoded_data = json.dumps(json_data).encode()
    return encoded_data
