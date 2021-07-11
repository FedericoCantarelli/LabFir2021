# Second example: see readme.txt for details
from socket import *

serverName = 'localhost' # Name for 127.0.0.1
serverPort = 12000 # Free to use port number

clientSocket = socket(AF_INET, SOCK_DGRAM)      # AF_INET -> ipv4  
                                                # SOCK_DGRAM -> UDP

message = input('Insert string: ') # Client asks user for a string

clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort)) # Send the binary string
clientSocket.settimeout(10) # Set a time-out


try:
      # With .rcvfrom() method client waits for the server
      count, serverAddress = clientSocket.recvfrom(2048)     # 2048 is the max dim in bytes
                                                            # both modMessage and server address are returned from the method

      # Note that recvfrom() does not explicit IP address                              
      print("The consonants are: " + count.decode('utf-8'), "\nGet from ", serverAddress)

except:
      print("An error occured: timeout exceeded")
clientSocket.close() # Client socket is now closed
