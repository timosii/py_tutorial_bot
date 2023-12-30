import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    WHO_SEND_ID = os.getenv('WHO_SEND_ID')

settings = Settings()
