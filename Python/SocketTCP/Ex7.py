# TCP server socket for first example

from socket import * 
# We don't need to specify serverAddress: by default is 127.0.0.1

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) # Welcome socket
serverSocket.bind(('',serverPort)) # Binding serverSocket to port number 12000

serverSocket.listen(1) # One is queue len

print('Server is ready.')
while 1:
      connectionSocket, clientAddress = serverSocket.accept()     # Welcome socket is waiting for connection request
                                                                  # Accept() has two output: the new socket and client IP addres (and port number)
      print(clientAddress, ' connected.')
      message = connectionSocket.recv(1024)
      message = message.decode('utf-8')
      modifiedMessage = message.upper()
      connectionSocket.send(modifiedMessage.encode('utf-8'))
      connectionSocket.close()
      print(clientAddress, ' disconnected')                                          