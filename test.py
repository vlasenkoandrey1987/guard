import requests

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

response = requests.delete(
    f'{origin}/api/v1/pass-holders/{pass_holder_id}/',
    headers={'Authorization': f'Token {token}'},
)
print(response.status_code, response.text)
