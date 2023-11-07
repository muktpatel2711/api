import pytest

import requests

def test_country_put():

    header = {
        'Content-type': 'application/json'
            }
    payload = {
        "countryId": "2",
        "countryCode": "AFR",
        "name": "Aus",
        "countryPhoneCode": "+41"
    }
    base_url='https://api.qa.bapsapps.org/mds/countries'

    resource = requests.put(url=base_url , headers=header , json=payload)

    assert 200 == resource.status_code
    print(resource.text)