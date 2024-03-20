from MDS.SSO_token.test_Created_sso import test_token

import schedule

import time

folder_path = "/Users/mukund/PycharmProjects/api/MDS/SSO_token"
file_name = "sso_token_updated"
file_path = f"{folder_path}/{file_name}"

def write_token_to_file():
    token_name = test_token()
    with open (file_path,"w") as file:
        file.write(token_name)
    print("Token updated successfully.")

write_token_to_file()

schedule.every(24).hours.do(write_token_to_file)

while True:
    schedule.run_pending()
    time.sleep(1)

