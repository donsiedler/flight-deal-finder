import os
import requests

USERNAME = os.environ.get("SHEETY_USERNAME")
PROJECT_NAME = "flightDeals"
SHEET_NAME = "users"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

headers = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}


def add_new_user(user_data):
    response = requests.post(url=SHEETY_ENDPOINT, headers=headers, json=user_data)
    response.raise_for_status()


print("Welcome to Flight Club.")
print("We find the best flight deals and email them to you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

emails_match = False

while not emails_match:
    email = input("What is your email?\n")
    email_repeated = input("Type your email again.\n")
    if email == email_repeated:
        emails_match = True
        data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        add_new_user(data)
        print("You're in the club!")
    else:
        print("Sorry that didn't work! Emails have to match.")
