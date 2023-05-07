# Name: Siddhrajsinh Pradumansinh Solanki
# Mav ID: 1001957988

'''References
1) https://fastapi.tiangolo.com/
2) https://github.com/sumanentc/python-sample-FastAPI-application
3) https://dassum.medium.com/building-rest-apis-using-fastapi-sqlalchemy-uvicorn-8a163ccf3aa1
'''

# Import the required modules
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, constr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from fastapi import Request
import re


# Create the FastAPI app
app = FastAPI()

# Create the SQLite database engine
engine = create_engine("sqlite:///phonebook.db", echo=True)

# Create the base class for the database models
Base = declarative_base()

# Create the PhoneBook model class
class PhoneBook(Base):
    __tablename__ = "phonebook"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone_number = Column(String)
    token = Column(String)

'''def __repr__(self):
        return f"<PhoneBook(id={self.id}, full_name={self.full_name}, phone_number={self.phone_number})>" '''

# Create the database schema
Base.metadata.create_all(engine)

# Create the session class for database operations
Session = sessionmaker(bind=engine)

# Define a custom type for phone number with a regex pattern
fn = r"^([A-Z][a-z]+) ([A-Z][a-z]+)$|^([A-Z][a-z]+), ([A-Z][a-z]+)$|^([A-Z][a-z]+), ([A-Z][a-z]+) ([A-Z][a-z]+)$|^[a-zA-Z]+([ \'-][a-zA-Z]+)*,\s[a-zA-Z]+([ \'-][a-zA-Z]+)*\.?$|^[a-zA-Z]+(([ ]{1}[a-zA-Z]+)$|^([\'][a-zA-Z]+))*([-][a-zA-Z]+)$|^([A-Z][a-z]+)$"
FullName = constr(regex=r"^([A-Z][a-z]+) ([A-Z][a-z]+)$|^([A-Z][a-z]+), ([A-Z][a-z]+)$|^([A-Z][a-z]+), ([A-Z][a-z]+) ([A-Z][a-z]+)$|^[a-zA-Z]+([ \'-][a-zA-Z]+)*,\s[a-zA-Z]+([ \'-][a-zA-Z]+)*\.?$|^[a-zA-Z]+(([ ]{1}[a-zA-Z]+)$|^([\'][a-zA-Z]+))*([-][a-zA-Z]+)$|^([A-Z][a-z]+)$")

# Define a custom type for full name with a regex pattern
ph = r"^[1-9]\d{4}$|^\([1-9]\d{2}\)\d{3}\-\d{4}$|^[1-9]\d{2}\-\d{4}$|^\+[1-9]\(\d{3}\)\d{3}-\d{4}$|^\+[1-9]?[0-9]\s\(\d{2}\)\s\d{3}-\d{4}$|^([1-9])\([0-9]{3}\)[.-]?[0-9]{3}[.-]?[0-9]{4}$|^\d{3}\s\d{3}\s\d{3}\s\d{4}$|^\d{5}\.\d{5}$|^\d{3}\s\d{1}\s\d{3}\s\d{3}\s\d{4}$"
PhoneNumber = constr(regex =r"^[1-9]\d{4}$|^\([1-9]\d{2}\)\d{3}\-\d{4}$|^[1-9]\d{2}\-\d{4}$|^\+[1-9]\(\d{3}\)\d{3}-\d{4}$|^\+[1-9]?[0-9]\s\(\d{2}\)\s\d{3}-\d{4}$|^([1-9])\([0-9]{3}\)[.-]?[0-9]{3}[.-]?[0-9]{4}$|^\d{3}\s\d{3}\s\d{3}\s\d{4}$|^\d{5}\.\d{5}$|^\d{3}\s\d{1}\s\d{3}\s\d{3}\s\d{4}$")

Token=constr()

# Create the Pydantic model class for request and response data
class Person(BaseModel):
    full_name: FullName = Query()
    phone_number: PhoneNumber = Query()
    token: Token = Query()

# Create a logger object
logger = logging.getLogger("phonebook_api")

# Set the logging level to INFO
logger.setLevel(logging.INFO)

# Create a file handler object
file_handler = logging.FileHandler("phonebook_api.log")

# Create a formatter object
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set the formatter for the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Define the API endpoints

@app.get("/PhoneBook/list")
def list_phonebook():
    # Get a new session
    session = Session()
    # Query all the records in the phonebook table
    phonebook = session.query(PhoneBook).all()
    # Close the session
    session.close()
    # Log the request and response
    logger.info(f"Received GET request for /PhoneBook/list")
    logger.info(f"Returned {len(phonebook)} records")
    # Return the list of records as JSON objects
    return phonebook

@app.post("/PhoneBook/add")
def add_person(person: Person):

    # Get a new session
    session = Session()
    # Check if the person already exists in the database by phone number or full name
    existing_person_by_number = session.query(PhoneBook).filter_by(phone_number=person.phone_number).first()
    existing_person_by_name = session.query(PhoneBook).filter_by(full_name=person.full_name).first()
    # If the person exists by either criteria, raise an exception
    if existing_person_by_number or existing_person_by_name:
        session.close()
        # Log the request and error
        logger.info(f"Received POST request for /PhoneBook/add with data {person}")
        logger.error(f"Person already exists in the database")
        raise HTTPException(status_code=400, detail="Person already exists in the database")
    # Otherwise, create a new PhoneBook record and add it to the database
    new_person = PhoneBook(full_name=person.full_name, phone_number=person.phone_number)
    session.add(new_person)
    session.commit()
    # Close the session
    session.close()
    # Log the request and success
    logger.info(f"Received POST request for /PhoneBook/add with data {person}")
    logger.info(f"Person added successfully")
    # Return a success message
    return {"message": "Person added successfully"}

@app.put("/PhoneBook/deleteByName")
def delete_by_name(full_name: FullName,request:Request):
    valToken(request)

    # Get a new session
    session = Session()
    # Query the person by full name in the database
    person = session.query(PhoneBook).filter_by(full_name=full_name).first()
    # If the person does not exist, raise an exception
    if not person:
        session.close()
        # Log the request and error
        logger.info(f"Received PUT request for /PhoneBook/deleteByName with data {full_name}")
        logger.error(f"Person not found in the database")
        raise HTTPException(status_code=404, detail="Person not found in the database")
    # Otherwise, delete the person from the database
    session.delete(person)
    session.commit()
    # Close the session
    session.close()
    # Log the request and success
    logger.info(f"Received PUT request for /PhoneBook/deleteByName with data {full_name}")
    logger.info(f"Person deleted successfully")
    # Return a success message
    return {"message": "Person deleted successfully"}
                            
@app.put("/PhoneBook/deleteByNumber")
def delete_by_number(phone_number: PhoneNumber,request:Request):
    valToken(request)

    # Get a new session
    session = Session()
    # Query the person by phone number in the database
    person = session.query(PhoneBook).filter_by(phone_number=phone_number).first()
    # If the person does not exist, raise an exception
    if not person:
        session.close()
        # Log the request and error
        logger.info(f"Received PUT request for /PhoneBook/deleteByNumber with data {phone_number}")
        logger.error(f"Person not found in the database")
        raise HTTPException(status_code=404, detail="Person not found in the database")
    # Otherwise, delete the person from the database
    session.delete(person)
    session.commit()
    # Close the session
    session.close()
     # Log the request and success
    logger.info(f"Received PUT request for /PhoneBook/deleteByNumber with data {phone_number}")
    logger.info(f"Person deleted successfully")
     # Return a success message
    return {"message": "Person deleted successfully"}

from Auth import Auth

@app.post("/PhoneBook/generateToken")
async def create_token(person:Person,request: Request):
    # Access request data
    data = await request.json()
    print(data)

    # Access request headers
    headers = request.headers
    tkn = Auth.generateToken(data["full_name"],data["phone_number"],Session())
    print(headers)
    if(tkn == None):
        logger.info(f"Received Invalid credentials for /PhoneBook/generateToken")
        return {"message": "Invalid User Credentials"}
    logger.info(f"Received valid credentials for /PhoneBook/generateToken:User created successfully")
    return {"message": "User created successfully","Token":tkn}

@app.post("/PhoneBook/valiateTokenTest")
def testValidateToken(token):
    
    result = validateToken(token)
    print(result)
    if(result == 0):
        logger.info(f"ERROR: Access denied. Token not found in header.")
        raise HTTPException(status_code=400, detail="Token not found")
    elif(result == 1 or result == 2):
        logger.info(f"ERROR:Expired Token")
        raise HTTPException(status_code=400, detail="Token not valid Either time has expired or token is old")
    elif(result == 4):
        logger.info(f"ERROR:Tampered Token.")
        raise HTTPException(status_code=400, detail="Token not valid. Tempered Token recieved")

    else:
        return {"message": "Token valid"}
    

def valToken(request:Request):
    header = request.headers
    if "Token" in header:
        token = header["Token"]
    else:
        token = None
    result = validateToken(token)
    print(result)
    if(result == 0):
        # return False
        
        raise HTTPException(status_code=400, detail="Token not found")
    elif(result == 1 or result == 2):
        # return False
        
        raise HTTPException(status_code=400, detail="Token not valid: Either time has expired or token is old.")
    elif(result == 4):
        # return False
        
        raise HTTPException(status_code=400, detail="Token not valid. Tempered Token recieved")


def validateToken(token):
    result = Auth.validateToken(token,Session())
        
    return result; 

def validate_input(input, pattern):
    # Try to match the input with the pattern
    match = re.match(pattern, input)
    # If there is a match, print the input and a message saying it is valid
    if match:
        return input + ": is a valid input."
    # Otherwise, print the input and a message saying it is invalid
    else:
        return input + ": is an invalid input."




# Define a path operation function that takes a Request object as a parameter
@app.post("/PhoneBook/Acceptable_Inputs_Name")
def acceptable_inputs_name(request : Request):
    # Acceptable inputs for name
    print("----------Acceptable inputs for name----------")
    #sample inputs
    t1 =validate_input("Bruce Schneier", fn) # Bruce Schneier is a valid input.
    t2 = validate_input("Schneier, Bruce", fn) # Schneier, Bruce is a valid input.
    #student inputs
    t3 = validate_input("Siddhraj Solanki", fn) # Siddhraj Solanki is a valid input.
    resultStr = str(t1+" "+t2+" "+t3)
    return {"Message":resultStr}

@app.post("/PhoneBook/Unacceptable_Inputs_Name")
def unacceptable_inputs_name(request : Request):
    print("----------Unacceptable inputs for name----------")
    #sample inputs
    t1=validate_input("Ron O’’Henry", fn) # Ron O’’Henry is an invalid input.
    t2=validate_input("L33t Hacker", fn) # L33t Hacker is an invalid input.
    #student inputs
    t3=validate_input("Siddhraj solanki", fn) # Siddhraj solanki is an invalid input.
    resultStr = str(t1+" "+t2+" "+t3)
    return {"Message":resultStr}

@app.post("/PhoneBook/Acceptable_Inputs_Phone")
def Acceptable_Inputs_Phone(request : Request):
    print("-----------Acceptable inputs for phone number----------")
    #sample inputs
    t1=validate_input("(703)111-2121", ph) # (703)111-2121 is a valid input.
    t2=validate_input("+32 (21) 212-2324", ph) # +32 (21) 212-2324 is a valid input.
    #student inputs
    t3=validate_input("+1(682)552-8101", ph) # +1(682)552-8101 is a valid input.
    resultStr = str(t1+" "+t2+" "+t3)
    return {"Message":resultStr}

@app.post("/PhoneBook/Unacceptable_Inputs_Phone")
def Unacceptable_Inputs_Phone(request : Request):
    print("-----------Unacceptable inputs for phone number----------")
    #sample inputs
    t1=validate_input("1234567890", ph) # 1234567890 is an invalid input.
    t2=validate_input("<script>alert(“XSS”)</script>", ph) # <script>alert(“XSS”)</script> is an invalid input.
    #student inputs
    t3=validate_input("SS 102-123-1234", ph) # SS 102-123-1234 is an invalid input.
    resultStr = str(t1+" "+t2+" "+t3)
    return {"Message":resultStr}
