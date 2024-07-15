import requests
import random
import httpx

def make_request(path):
    with httpx.Client(
        # enable HTTP2 support
        http1=False,
        http2=True
    ) as client:
        base_url = f'http://nginx-1.25/{path}'
        headers = {'X-Custom': 'from-request'}
        response = client.get(f'{base_url}?{random.randint(1, 1000)}')
        return response
