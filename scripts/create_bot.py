#!/usr/bin/env python

import json
import logging
import requests

admin_name = "boss"
admin_password = "boss"

bot_name = "rasa_bot"
bot_password = "rasa_bot"
bot_email = bot_name + '@email.com'

host = "http://localhost:3000/"
user_header = None

path = "/api/v1/login"

def get_authentication_token():
    login_data = {"username": admin_name, "password": admin_password}
    response = requests.post(host + path, data=login_data)

    if response.json()["status"] == "success":
        logging.info("Login suceeded")

        authToken = response.json()["data"]["authToken"]
        userId = response.json()["data"]["userId"]
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json"
        }

        return user_header
    else:
        print(response)

def create_bot_user():
    user_info = {
        "name": bot_name,
        "email": bot_email,
        "password": bot_password,
        "username": bot_name,
        'requirePasswordChange': False,
        'sendWelcomeEmail': True, 'roles': ['bot']
    }

    create_user_response = requests.post(
        host + '/api/v1/users.create',
        data=json.dumps(user_info),
        headers=user_header
    )
    
    print(create_user_response)

if __name__ == '__main__':
    user_header = get_authentication_token()
    create_bot_user()
