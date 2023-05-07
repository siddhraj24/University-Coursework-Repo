# Phone Book API Input Validation

This is a REST API that maintains a phone book of names and phone numbers. The program can receive and store a list of people with their full name and telephone. It includes the following API endpoints:

- `GET /PhoneBook/list`: Produce a list of the members of the database.
- `POST /PhoneBook/add`: Add a new person to the database. The argument is an object with name and phone number string elements represented in JSON.
- `PUT /PhoneBook/deleteByName`: Remove someone from the database by name. The argument is the name as a string.
- `PUT /PhoneBook/deleteByNumber`: Remove someone by telephone #. The argument is the phone number as a string.

## Implementation

The API is implemented using [Python 3](https://www.python.org/) and the [FastAPI](https://fastapi.tiangolo.com/) web framework. The phone book data is persisted in a SQLite database using the [SQLAlchemy](https://www.sqlalchemy.org/) ORM.

The input validation is done using regular expressions. The program uses the regular expressions for `<Person>` and `<Telephone #>` to verify that the user is supplying valid data. It allows for international or US format telephone numbers and for `<first middle last>`, `<first last>`, or `<last, first MI>` name formats.

An audit log is created that contains timestamped log entries written anytime a user adds a name, removes a name, or lists the names. For add/remove entries, the name of the person that was added/removed is included in the log.

The API is packaged as a Docker container for ease of deployment and testing. Automated security-focused unit tests are included to test all of the inputs provided in the assignment and verify proper handling of them along with some of your own inputs.

## Installation

1. Clone the repository to your local machine.
2. Create and activate a new virtual environment (Optional).
3. Install the required packages with the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. In the terminal, navigate to the folder containing your Python code.
2. To run the app, type the following command in the terminal:

   ```
   uvicorn app:app --reload
   ```

3. Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the API documentation.

## Docker

To run the app using Docker:

1. Build the Docker image:

   ```
   docker build -t phonebook .
   ```

2. Run the Docker container:

   ```
   docker run -p 8000:8000 phonebook
   ```

3. Open your web browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the API documentation.

## Authentication

The application requires users to authenticate using a token before they can create, read, update, or delete contacts. To obtain the token, send a POST request to `/auth/token` with valid full name and phone number. The token will be returned in the response, and you can use it in subsequent requests by setting the `Authorization` header with this value in postman.

## Logging

The application logs events using the Python logging module and saves them to a file called `phonebook_api.log`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## API Documentation

The API documentation is provided in the OpenAPI 3.0 format and can be viewed by opening the `PhoneBook.json` file.