import requests

file_path = "/Users/mukund/PycharmProjects/api/MDS/SSO_token/sso_token_updated"
with open(file_path,"r") as file:
     token_sso = file.read()
token_string = "Baerer "+ token_sso
Base_url = "https://api.dev.bapsapps.org/mds"
post_endpoint = "/locations"
get_endpoint = "/locations/{}"
headers = {"Content-Type": "application/json",
           "x-app-auth-secret":"secret",
           "x-app-auth-id":"demo",
           "Authorization":token_string,
           "xx-auth-position-id":"55382",
           "xx-auth-role-id":"1"
           }
payload = {
        "data": [
            {
            "parents": [
                {
                    "parentId": 1003,
                    "isPrimaryParent": "false"
                }
            ],
            "locationLevelId":60,
            "countryCode": "IND",
            "locationTypeId": 120,
            "geographicAreaId": "null",
            "code": "KG",
            "uucode": "TEST-UUCODE",
            "name": "WWW-TES-qaa",
            "uuname": "TEST-UUNAME-qaa",
            "status": "ACTIVE",
            "addressLine1": "5678 Main St",
            "addressLine2": "8989 Road",
            "addressLine3": "00000 Test",
            "postalCode": "M5V2L-",
            "latitude": 43.653201,
            "longitude": -79.383201,
            "phonePrimary": "888888881",
            "emailPrimary": "toronto@example.com"
        }
    ]

}

location_id = None

def test_01_post():
    global location_id
    url = Base_url + post_endpoint
    response= requests.post(url , json=payload, headers=headers)
    print("Post_response:",response.json())
    status_code = response.status_code
    print("Post_statuscode:",status_code)
    if response.status_code==201:
        location_id = response.json().get("data")[0].get("locationId")
        message_type = response.json().get("messages")[0].get("responseMessages")[0].get("type")
        print("locationId:",location_id)
        print(message_type)
        assert message_type == "S"
        return location_id
def test_02_get():
    global location_id
    url = Base_url + get_endpoint.format(location_id)
    response = requests.get(url,headers=headers)
    print("Get_response:", response.json())
    status_code = response.status_code
    print("Get_statuscode:", status_code)
    if response.status_code==200:
        location_id = response.json().get("data")[0].get("locationId")
        print("locationId:",location_id)
        name_value = response.json().get("data")[0].get("name")
        print(name_value)
        assert status_code==200

def test_03_patch():
    global location_id
    if location_id is not None:
        url = Base_url + get_endpoint.format(location_id)
        current_data = requests.get(url, headers=headers).json()

        # Update only the 'name' field
        name_update_payload = {
            "data": [
                {
                    "name": "test08"
                }
            ]
        }

        patch_url = Base_url + get_endpoint.format(location_id)
        patch_response = requests.patch(patch_url, json=name_update_payload, headers=headers)
        print("Patch_response:", patch_response.json())
        status_code = patch_response.status_code
        print("Patch_statuscode:", status_code)
        if patch_response.status_code == 200:
            location_id = patch_response.json().get("data")[0].get("locationId")
            print("locationId:", location_id)
        assert status_code==200


def test_04_Get_patch():
    global location_id
    url = Base_url + get_endpoint.format(location_id)
    response = requests.get(url, headers=headers)
    print("Get_Patch_response:", response.json())
    status_code = response.status_code
    print("Get_Patch_statuscode:", status_code)
    if response.status_code == 200:
        location_id = response.json().get("data")[0].get("locationId")
        print("locationId:", location_id)
        name_value = response.json().get("data")[0].get("name")
        assert name_value=="test08"
        print("Updated_value:",name_value)

def test_05_Delete():
    global location_id
    url1 = Base_url + get_endpoint.format(location_id) + "/parent-relations/1003"
    print(url1)
    resource1 =requests.delete(url1, headers=headers)
    status_code = resource1.status_code
    print(status_code)
    url= Base_url + get_endpoint.format(location_id)
    print(url)
    resource = requests.delete(url,headers=headers)
    Deleted_status_code = resource.status_code
    print("Status code:",Deleted_status_code)
    assert status_code==204

def test_06_get_deleted():
    global  location_id
    url = Base_url + get_endpoint.format(location_id)
    resource = requests.get(url,headers=headers)
    status_code = resource.status_code
    print("status_code:",status_code)
    message_text = resource.json().get("messages")[0].get("responseMessages")[0].get("text")
    print("Response message_text:",message_text)
    assert message_text == "Location is deleted."









