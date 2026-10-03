import os
from dotenv import load_dotenv

load_dotenv()

class Config :
    FERNET_KEY = os.getenv('FERNET_KEY').encode()
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE = os.getenv('DATABASE', 'message.db')