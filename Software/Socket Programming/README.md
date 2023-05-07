
# Socket Programming: Client-Server Architecture with Caching

This project is an introduction to socket programming using client-server architecture and caching. It involves creating a continuously running client-server based application (along with a proxy server) that retrieves key-value pairs using socket programming. The server facilitates service for commands like GET, PUT, and DUMP, for the corresponding multiple pair (of key-value) stored. The project has been implemented using Python and the following libraries: socket.

## Problem Statement

The project involves implementing the following four commands on the server:

1. **PUT**: This command is used to store a key-value pair on the server. The syntax for this command is `PUT [key] = [value]`.

2. **GET**: This command is used to retrieve the value of a key. The syntax for this command is `GET [key]`.

3. **DUMP**: This command is used to output all the keys that are present in the server. The syntax for this command is `DUMP`.

4. **GET (using proxy server)**: This is similar to the GET command, except that it is implemented using a proxy server. The first time a GET request is made, the value is fetched from the server. If the client makes a call to the same key again, the request is handled by the proxy server.

## Files

The project consists of the following files:

- `client.py`: This file contains the implementation of the client side of the application.

- `server.py`: This file contains the implementation of the server side of the application.

- `proxy.py`: This file contains the implementation of the proxy server.

## Usage

To run the application, follow these steps:

1. Run the server using the following command: `python server.py`.

2. Run the proxy server using the following command: `python proxy.py`.

3. Run the client using the following command: `python client.py`.


## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
