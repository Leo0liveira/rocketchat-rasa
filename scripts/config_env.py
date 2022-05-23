#!/usr/bin/env python

import json
import logging
import requests
from time import sleep

# == Log Config ==
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# == Admin Info == 
admin_name = "boss"
admin_password = "boss"

# == Bot Info == 
bot_name = "rasa_bot"
bot_password = "rasa_bot"
bot_email = bot_name + '@email.com'

# == Host Info ==
#host = http://rocketchat:3000/ # Rocketchat - Docker
host = "http://localhost:3000/" # Rockechat - Local
path = "/api/v1/login"
user_header = None


def get_authentication_token(user):
    login_data = {"username": user, "password": user}
    response = requests.post(host + path, data=login_data)

    if response.json()["status"] == "success":
        logger.info(f"Login succeed | Header = {user}")

        authToken = response.json()["data"]["authToken"]
        userId = response.json()["data"]["userId"]
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json"
        }

        return user_header
    else:
        logger.error(f"Login failed | {response}") 

def create_bot_user():
    user_info = {
        "name": bot_name,
        "email": bot_email,
        "password": bot_password,
        "username": bot_name,
        "requirePasswordChange": False,
        "sendWelcomeEmail": True, 
        "roles": ["bot", "livechat-agent"],
    }

    user_header = get_authentication_token(admin_name)

    create_user_response = requests.post(
        host + '/api/v1/users.create',
        data=json.dumps(user_info),
        headers=user_header
    )

    if create_user_response.json()["success"] == True:
        logger.info(f"Bot created | Bot = {bot_name}")
    else:
        logger.error(f"Unable to create bot  | {create_user_response}")

    
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
        logger.info(f"Avatar updated | User = {bot_name}")
    else:
        logger.error(f"Unable to create avatar | {set_avatar_response}")

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
        logger.info(f"Status ON | Bot = {bot_name}")
    else:
        logger.error(f"Unable to activate status | {set_user_status_response}")
    
def config_bot():
    create_bot_user()
    set_bot_avatar()
    set_bot_status_active()

if __name__ == '__main__':
    logger.info("===== Sara Mascot S2 =====")

    #rasa_url = "http://bot:5005/" # Rasa - Docker
    rasa_url = "http://localhost:5005/" # Rasa - Local


    response = False

    while(not response):
        try:
            response = requests.get(rasa_url)
            response = True
            logger.info("Rasa Server UP!")
            config_bot()
        except:
            logger.info("Rasa Server DOWN...") 
        finally:
            sleep(3)

    logger.info("===== END =====")
