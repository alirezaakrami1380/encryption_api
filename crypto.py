from cryptography.fernet import Fernet, InvalidToken
from config import Config

cipher = Fernet(Config.FERNET_KEY)

#-----------------------------رمزنگاری-------------------------------
def encrypt_text(text):
    token = cipher.encrypt(text.encode())
    return token.decode()

#-----------------------------رمزگشایی-------------------------------
def decrypt_token(token):
    try:
        text = cipher.decrypt(token.encode())
        return text.decode(), None
    except InvalidToken:
        return None, "توکن نامعتبر یا دستکاری شده است"
    except Exception as e:
        return None, f"{str(e)} : خطای غیر منتظره"