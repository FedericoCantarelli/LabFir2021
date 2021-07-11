from socket import * 

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort)) # The server is now running on serverPort
                                    # In client socket we were not interested in giving it a specific port number
print("Server is ready.")

while 1:                            # Server begins listening
      message, clientAddres = serverSocket.recvfrom(2048)
      message = message.decode('utf-8')

      print("Recieved message from ", clientAddres)
      modMessage = message.upper()

      serverSocket.sendto(modMessage.encode('utf-8'), clientAddres)
