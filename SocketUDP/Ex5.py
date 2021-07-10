# Second example: consonants counting
from socket import * 

vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ' ']
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print("Server is ready.")

while 1:
      cnt = 0
      message, clientAddres = serverSocket.recvfrom(2048)
      message = str(message.decode('utf-8'))
      print("Recieved message from ", clientAddres)

      for charac in message:
            if charac not in vocals:
                  cnt = cnt +1
      


      serverSocket.sendto(str(cnt).encode('utf-8'), clientAddres)
