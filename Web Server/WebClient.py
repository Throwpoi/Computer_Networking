#import socket module


from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

clientSocket.connect((sys.argv[1],port))
clientSocket.send(str(sys.argv[3]))


server_info=clientSocket.recv(1000)
print server_info


clientSocket.close() 