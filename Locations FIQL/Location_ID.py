import time

import requests

def test_location_id():
     #Base_url
    base_url="https://api.qa.bapsapps.org/mds";

    #Validate Response Time
    start_time = time.time() * 1000
    response = requests.get(base_url + "/locations?filter=locationid>0")
    end_time = time.time() * 1000
    total_time = end_time - start_time
    assert total_time <=500
    print(total_time)

    #Validate status code
    assert response.status_code==200
    json_data = response.json()
    print(json_data)

    #validate json value
    value = json_data.get("messages")[0].get("responseMessages")[0].get("type")
    assert value=="S"
    print(value)