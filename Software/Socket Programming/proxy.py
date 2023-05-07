import socket
import threading
import os 
import datetime
import pickle

PORT = 9999                                          
SERVER_ADDRESS= socket.gethostbyname(socket.gethostname())  #get the ip address of the current system
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #server socket created 
server_socket = (SERVER_ADDRESS,PORT)                        #creating a socket
server.bind(server_socket)  

MAIN_SERVER = socket.gethostbyname(socket.gethostname()) #stores the address of the local system.
PROXY_PORT = 9997
SERVERA_SOCKET = (MAIN_SERVER,PROXY_PORT)    

servera_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #client socket 
cache={}



def comm_handler(conn,addr):
    print(f"Proxy Connected to {addr}")
    servera_socket.connect(SERVERA_SOCKET)

    while True:
        message=""
        client_message = conn.recv(20480).decode("utf-8")
        #print(len(client_message))
        if(len(client_message) > 0):
            print(client_message)
            cmsplit = client_message.split(" ")
            if(cmsplit[0] == "PUT"):
                print("Put recieved"+str(len(cmsplit)))

                servera_socket.send(bytes(client_message,'utf-8'))
                result = servera_socket.recv(20480).decode('utf-8')
                cache.clear()
                message = result
            elif(cmsplit[0] == "GET"):
                print("Get recieved")
                if(len(cmsplit) < 2):
                    message+="Invalid get parameters"
                else:
                    if(not(client_message in cache.keys())):
                        servera_socket.send(bytes(client_message,'utf-8'))
                        result = servera_socket.recv(20480).decode('utf-8')
                        cache[client_message] = result
                    
                    message = cache[client_message]
                    
            elif(cmsplit[0] == "DUMP"):
                if(not(client_message in cache.keys())):
                        servera_socket.send(bytes(client_message,'utf-8'))
                        result = servera_socket.recv(20480).decode('utf-8')
                        cache[client_message] = result;
                    
                message = cache[client_message]
        conn.send(message.encode())              



def server_Start():
    server.listen()
    print("Server Started")
    while True:
        conn, addr = server.accept()                        #accepts the client connection
        server1_thread = threading.Thread(target = comm_handler, args = (conn,addr))       #creating a thread to handle the communication with client
        server1_thread.start()

server_Start()