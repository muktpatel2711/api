
import requests
from MDS.SSO_token.test_Created_sso import test_token

file_path = "/Users/mukund/PycharmProjects/api/MDS/SSO_token/sso_token_updated"
with open(file_path,"r") as file:
     token_sso = file.read()

print("Token:",token_sso)
token_string = "Baerer "+ token_sso
Base_url = "https://api.dev.bapsapps.org/mds"
post_endpoint = "/locations"
get_endpoint = "/locations/{}"
headers = {"Content-Type": "application/json",
           "x-app-auth-secret":"secret",
           "x-app-auth-id":"demo",
           "Authorization":token_string,
          #"Authorization":"Baerer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik5vbmUiLCJyZXF1ZXN0b3JpZCI6Ik5vbmUiLCJyZXNvdXJjZXVyaSI6IiIsImFkZGl0aW9uYWxpbmZvIjoiTm9uZSIsIm5vbmNlIjoiTm9uZSIsInVpZCI6ImYxZmYxNWFmLTIzNjYtNGEyMy1iZWFjLTQ1OWExYWU1MDUzYyIsInNpZCI6IjFlODNlNzg1LWJlMzctNDVjNC05YjJhLTNmMjRiZmRhNTRlNSIsImFpZCI6ImEzNDQwODI2LWM5NzItNGMzNC05ZGMxLThjM2QxMzMxM2UxNSIsImNpZCI6IjI3OTg0MkRDLTBBMjEtNDFFRS1CNDRELTlFNDRBQTgzODgwMiIsImF1dGgiOiJ2ZXJpZmllZCIsImZuIjoiTXVrdW5kIiwibG4iOiJQYXRlbCIsInBpZCI6IjIxMTMxMDgiLCJjdCI6ImF0Iiwicm9sZSI6IlVuZGVmaW5lZCIsIm5iZiI6MTcwNjEzMjExMiwiZXhwIjoxNzA2OTk2MTEyLCJpYXQiOjE3MDYxMzIxMTIsImlzcyI6Imh0dHBzOi8vYmFwcy5vcmciLCJhdWQiOiJNZW1iZXJzIn0.OK7h4FR2noMQs93eg4VSrCCqT63fwjvtq6yZefACjsI",
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

