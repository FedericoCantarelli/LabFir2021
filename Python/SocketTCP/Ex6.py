# TCP client for first example

from socket import *

# Welcome socket
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) # AF_INET --> ipv4, SOCK_STREAM --> TCP 
clientSocket.connect((serverName, serverPort)) # Client asks for connection to welcome socket

message = input("Insert string: ")

clientSocket.settimeout(5)
try:
      clientSocket.send(message.encode('utf-8'))      # Note: just send not sendto, because of persistent connection 
                                                      # we don't know server ip address yet, 
                                                      # we just know welcome socket IP

      modifiedMessage = clientSocket.recv(1024)       # Because of persistent connection, we
                                                      # don't need server address

      print("Modified string is ", modifiedMessage.decode('utf-8'))  

except:
      print("An error occured: connection timeout exceeded, check if server is busy")

finally:
      clientSocket.close()

