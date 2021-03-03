import json


def build_response(status_code: int, body: dict) -> dict:
    response = {"statusCode": status_code, "body": json.dumps(body)}
    return response
