import pytest

import requests

def test_country_delete():

    header = {
        'Content-type': 'application/json'
            }

    base_url='https://api.qa.bapsapps.org/mds/countries'

    resource = requests.put(url=base_url , headers=header)

    assert 200 == resource.status_code
    print(resource.text)