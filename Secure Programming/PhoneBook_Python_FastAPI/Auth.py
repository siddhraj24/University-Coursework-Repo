import random
import string
import datetime
import time
from app import PhoneBook,Person
from Crypter import Crypter

class Auth:
    def __init__():
        pass
    @staticmethod
    def createToken():
        length = random.randint(8, 12) # choose length between 8 and 12 characters
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
    
    @staticmethod
    def generateToken(username,phone,session):
        tkn  = Auth.createToken()
        # Get the current date and time
        seconds_since_epoch = time.time()
        current_datetime = datetime.datetime.utcfromtimestamp(seconds_since_epoch)
        #"insert into tokenUser(username,password,token)"
        person = session.query(PhoneBook).filter_by(full_name = username).filter_by(phone_number = phone).first()
        if(person == None):
            return person
        
        person.token = tkn
        session.commit()
        # Close the session
        now = datetime.datetime.now()
        str_now = now.strftime('%Y-%m-%d %H:%M:%S')
        # dt_now = datetime.datetime.strptime(str_now, '%Y-%m-%d %H:%M:%S')
        Secret = person.full_name+"-@-"+person.phone_number+"-@-"+person.token+"-@-"+str_now
        session.close()
        finalToken = Crypter.Encrypt(Secret)
        print(finalToken)
        return finalToken
    
    
    @staticmethod
    def validateToken(token,session):
        if(token == None or len(token) == 0 ):
            return 0
        else:
            print("inside else in validatetoken")
            tokenDecoded = Crypter.Decrypt(token)
            print(tokenDecoded)
            if(tokenDecoded == None):
                return 4
            
            valu = tokenDecoded.split("-@-")
            print(valu)
            
            username = valu[0]
            phone = valu[1]
            tokenNumber = valu[2]
            
            
            person = session.query(PhoneBook).filter_by(full_name = username).filter_by(phone_number = phone).first()
            session.commit()
            persontoken = person.token
            session.close()
            
            if(person == None):
                return 1
            
            dt_now = datetime.datetime.strptime(valu[3], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            diff = now-dt_now
            print(diff.total_seconds())
            if(diff.total_seconds() <= 600 and persontoken == tokenNumber):
                session.close()
                return 3
            else:
                return 2
        
        