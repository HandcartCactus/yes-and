from fastapi import Response
import json
import random

def random_status_code():
    return Response(content='Roses are red, violets are blue, your status code might not start with a 2!', status_code=random.randint(100, 599))




RESPONSE_STRATEGIES = [
    random_status_code,
]

def random_response():
    return random.choice(RESPONSE_STRATEGIES)()