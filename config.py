import os

class Settings:
    BOT_TOKEN = os.environ['BOT_TOKEN']
    WHO_SEND_ID = os.environ['WHO_SEND_ID']

settings = Settings()