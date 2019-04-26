import json


def hello2(event, context):
    body = {
        "message": "Hello Maicon Keller!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Hello Maicon Keller!",
        "event": event
    }
    """
