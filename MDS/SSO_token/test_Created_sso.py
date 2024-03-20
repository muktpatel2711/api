import requests
import json

sso_token =None

def test_ssoToken():
    global sso_token
    url = "https://api.uat.bapsapps.org/sso/api/auth/secured/requesttoken"

    payload = json.dumps({
        "resourceUri": "auth/login"
    })
    headers = {
        'Client-ID': '279842DC-0A21-41EE-B44D-9E44AA838802',
        'Client-Secret': '30915098-1C86-4D19-85A9-64DC0E2075BC',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    sso_token = response.json().get("requestToken")
    print("Request_Token:",sso_token)

def test_token():
    url = "https://api.uat.bapsapps.org/sso/api/user/login"

    payload = json.dumps({
        "userName": "muktpatel2711@gmail.com",
        "password": "Mahantraj@1",
        "applicationId": "88EE59E0-2E01-41D9-AF90-2A1C3B5FD904"
    })
    headers = {
        'Authorization': sso_token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json().get("token")
    print("Token:" ,token)
    return token

test_ssoToken()
token_name = test_token()