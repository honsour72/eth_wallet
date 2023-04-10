import requests


host = "http://localhost:8000/api/v1/wallets"


def test_create_wallet_currency_upper_case_success():
    data = {"currency": 'ETH'}
    r = requests.post(host, data=data)
    assert r.status_code == 200
    response = r.json()
    assert isinstance(response['id'], int)
    assert isinstance(response['public_key'], str)
    assert response['currency'] == "ETH"


def test_create_wallet_currency_lower_case_success():
    data = {"currency": 'eth'}
    r = requests.post(host, data=data)
    assert r.status_code == 200
    response = r.json()
    assert isinstance(response['id'], int)
    assert isinstance(response['public_key'], str)
    assert response['currency'] == "ETH"


def test_create_wallet_wrong_currency():
    data = {"currency": 'btc'}
    r = requests.post(host, data=data)
    assert r.status_code == 400
    response = r.json()
    assert isinstance(response['error'], str)


def test_get_all_wallets():
    r = requests.get(host)
    assert r.status_code == 200
    response = r.json()
    assert isinstance(response, list)
    first = response.pop()
    assert isinstance(first, dict)
