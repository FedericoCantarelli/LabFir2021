# Persistent client socket

from socket import *

# Welcome socket
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)  
clientSocket.connect((serverName, serverPort))



while 1:

      message = input("Insert string (. to end connection): ")
      clientSocket.send(message.encode('utf-8'))
      if message == '.':
            print("Connection ended by user")
            clientSocket.close()
            break

      modifiedMessage = clientSocket.recv(1024)       

      print("Modified string is ", modifiedMessage.decode('utf-8'))  


