#!/usr/bin/env python

import json
import logging
import requests

# == Log Config ==
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# == User Info == 
admin_name = "boss"
admin_password = "boss"

bot_name = "rasa_bot"
bot_password = "rasa_bot"
bot_email = bot_name + '@email.com'

host = "http://localhost:3000/"
user_header = None

path = "/api/v1/login"

def get_authentication_token(user):
    login_data = {"username": user, "password": user}
    response = requests.post(host + path, data=login_data)

    if response.json()["status"] == "success":
        logger.info(f"Login succeed | Header = {user}\n")

        authToken = response.json()["data"]["authToken"]
        userId = response.json()["data"]["userId"]
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json"
        }

        return user_header
    else:
        logger.error(f"Login failed | {response}\n") 

def create_bot_user():
    user_info = {
        "name": bot_name,
        "email": bot_email,
        "password": bot_password,
        "username": bot_name,
        "requirePasswordChange": False,
        "sendWelcomeEmail": True, 
        "roles": ["bot"],
    }

    user_header = get_authentication_token(admin_name)

    create_user_response = requests.post(
        host + '/api/v1/users.create',
        data=json.dumps(user_info),
        headers=user_header
    )

    if create_user_response.json()["success"] == True:
        logger.info(f"Bot created | Bot = {bot_name}\n")
    else:
        logger.error(f"Unable to create bot  | {create_user_response}\n")

    
def set_bot_avatar():
    avatar_config = {
        "username": bot_name,
        "avatarUrl": "https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png",
    }

    user_header = get_authentication_token(bot_name)

    set_avatar_response = requests.post(
        host + "api/v1/users.setAvatar",
        data=json.dumps(avatar_config),
        headers=user_header
    )

    if set_avatar_response.json()["success"] == True:
        logger.info(f"Avatar created | User = {bot_name}\n")
    else:
        logger.error(f"Unable to create avatar | {set_avatar_response}\n")

def set_bot_status_active():
    user_status = {
        "message": "My status update", 
        "status": "online" 
    }

    user_header = get_authentication_token(bot_name)

    set_user_status_response = requests.post(
        host + "/api/v1/users.setStatus",
        data=json.dumps(user_status),
        headers=user_header
    )

    if set_user_status_response.json()["success"] == True:
        logger.info(f"Status ON | Bot = {bot_name}\n")
    else:
        logger.error(f"Unable to activate status | {set_user_status_response}\n")
    

if __name__ == '__main__':
    create_bot_user()
    set_bot_avatar()
    set_bot_status_active()
