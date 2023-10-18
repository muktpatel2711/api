import requests

# API get request

url = "https://api.qa.bapsapps.org/mds/role-types?filter=roleTypeId>0"
# send get request

response = requests.get(url)

print(response)

