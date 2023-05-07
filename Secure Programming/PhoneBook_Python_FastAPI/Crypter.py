from cryptography.fernet import Fernet
import base64
from jwt.exceptions import InvalidTokenError




class Crypter:
    #EK =  b"U6TbTmkfLdzcLg18D7n9HJ8G7CZfd2QZ"
    EK = Fernet.generate_key()
    cipher_suite = Fernet(EK)
    def __init__():
        pass
    @staticmethod
    def Encrypt(message: str):
        encoded_text = Crypter.cipher_suite.encrypt(message.encode())
        encoded_text =  base64.urlsafe_b64encode(encoded_text).decode()
        return encoded_text
    
    @staticmethod
    def Decrypt(decode_message:str):
        try:
            decoded_text = Crypter.cipher_suite.decrypt(base64.urlsafe_b64decode(decode_message.encode()))
        except InvalidTokenError:
            print("Tempered Token recieved")
            return None
        except Exception as ex:
            print(ex)
            return None
        print(type(decoded_text.decode()))
        return decoded_text.decode()
        