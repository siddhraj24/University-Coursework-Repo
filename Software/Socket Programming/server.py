import socket
import threading
import os 
import datetime
import pickle


PORT = 9997                                             
SERVER_ADDRESS= socket.gethostbyname(socket.gethostname())  #got the ip address of the current system
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #server socket created 
server_socket = (SERVER_ADDRESS,PORT)                        #creating a socket
server.bind(server_socket)  
dict={}



def comm_handler(conn,addr):
    print(f"Server Connected to {addr}")

    while True:
        message=""
        client_message = conn.recv(20480).decode("utf-8")
        #print(len(client_message))
        if(len(client_message) > 0):
            print(client_message)
            cmsplit = client_message.split(" ")
            if(cmsplit[0] == "PUT"):
                print("Put recieved"+str(len(cmsplit)))
                if(len(cmsplit) < 4):
                    message+="Invalid put parameters"
                elif(len(cmsplit) == 4):
                    print("inside put")
                    dict[cmsplit[1]] =cmsplit[-1] 
                    message+="Put success"
            elif(cmsplit[0] == "GET"):
                print("Get recieved")
                if(len(cmsplit) < 2):
                    message+="Invalid get parameters"
                else:
                    message += str(dict[cmsplit[1]]) 
            elif(cmsplit[0] == "DUMP"):
                print("Dump recieved")
                for key in dict:
                    print(key)
                    message += key+" "
        conn.send(message.encode())            



def server_Start():
    server.listen()
    print("Server Started")
    while True:
        conn, addr = server.accept()                        #accepts the client connection
        server1_thread = threading.Thread(target = comm_handler, args = (conn,addr))       #creating a thread to handle the communication with client
        server1_thread.start()

server_Start()