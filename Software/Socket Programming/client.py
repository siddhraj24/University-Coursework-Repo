import socket,pickle

SERVER_ADDRESS = socket.gethostbyname(socket.gethostname()) #stores the address of the local system.
PORT = 9996                                              #port at which client will make the connection  .
PROXY_PORT = 9999
SERVER_SOCKET = (SERVER_ADDRESS,PROXY_PORT)                       #socket at which the client will make a connection.


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #client socket 
client_socket.connect(SERVER_SOCKET)                                

#will take the input and check for the correct command 
while True:
    command = input("Type command: ")
    commands = command.split(" ")
    if(commands[0] == "PUT" or commands[0]=="GET" or commands[0]=="DUMP"):                                     
        client_socket.send(bytes(command,'utf-8'))                  #COmmand sent
        result = client_socket.recv(20480).decode('utf-8')          #wait for the server to send the data and stores it in result variable
        print(result)                                               
        # client_socket.close()                                     
        # break
    elif(command=="EXIT"):
        print("Terminating connection")
        client_socket.close()                                       #client closes the connection.
        break