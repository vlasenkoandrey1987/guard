import requests
from datetime import datetime, timedelta

origin = 'http://127.0.0.1:8000'

response = requests.post(
    f'{origin}/api/v1/api-token-auth/',
    data={
        'username': 'andrey',
        'password': '1',
    },
)
print(response.status_code, response.text)

token = response.json()['token']

response = requests.post(
    f'{origin}/api/v1/pass-holders/',
    headers={'Authorization': f'Token {token}'},
    json={
        'person': 1,
    },
)
print(response.status_code, response.text)

pass_holder_id = response.json()['id']

response = requests.get(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.get(
    f'{origin}/api/v1/pass-holders/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.post(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/',
    headers={'Authorization': f'Token {token}'},
    json={
        'pass_holder': pass_holder_id,
        'valid_from': str(datetime.now().astimezone() - timedelta(days=365)),
        'valid_until': str(datetime.now().astimezone() - timedelta(days=335)),
    },
)
print(response.status_code, response.text)

response = requests.post(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/',
    headers={'Authorization': f'Token {token}'},
    json={
        'pass_holder': pass_holder_id,
        'valid_from': str(datetime.now().astimezone()),
        'valid_until': str(datetime.now().astimezone() + timedelta(days=365)),
    },
)
print(response.status_code, response.text)

pass_id = response.json()['id']

response = requests.patch(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/{pass_id}/',
    headers={'Authorization': f'Token {token}'},
    json={
        'mfuid': '0123456789',
        'valid_until': str(datetime.now().astimezone() + timedelta(days=30)),
    },
)
print(response.status_code, response.text)

response = requests.get(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/{pass_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.get(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.delete(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.delete(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/passes/{pass_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)

response = requests.delete(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)
