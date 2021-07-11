UDP socket
No handshaking
Every segment has IP address and destination port
Server can obtain IP address and port of the sender from the recieved segments

First example:
Client sends a string to the server,
Server makes the strig uppercase and sends it back to the client
The client recieves the modified string and print the string.

 Tips:
 use $> netstat -na | grep "12000" once server is ready, to see if server is running.

Second example:
Client sends a string to the server,
Server counts consonants and send the number back to the client
The client recieves the number and print the number
