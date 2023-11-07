import pytest

import requests

def test_country_post():

    header = {
        'Content-type': 'application/json'
            }
    payload = {
        "countryId": "2",
        "countryCode": "AUS",
        "name": "Aus",
        "countryPhoneCode": "+41"

    }
    base_url='https://api.qa.bapsapps.org/mds/countries'

    resource = requests.post(url=base_url , headers=header , json=payload)

    assert 201 == resource.status_code
    print(resource.text)