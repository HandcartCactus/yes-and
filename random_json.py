from fastapi import Response
import json
import random

def bad_json():
    return Response(content='{', media_type='application/json')

def wack_json():
    x = {'wack':'wack'}
    for i in range(random.randint(5,999)):
        x = {''.join(random.choices('!@#$%^&*()_+-=[]\{}|:";\'<>?,./', k=random.randint(0, 100))): x}
    return Response(content=json.dumps(x), media_type='application/json')



JSON_RESPONSE_STRATEGIES = [
    bad_json,
    wack_json,

]