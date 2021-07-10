TCP socket

1. Server starts a socket to catch client requests: this is called welcome socket and, like the UDP socket, can recieve from all the clients.
2. Client starts a solid connection with the server before it starts sending data
3. When the server get the connection requests, it creates a new socket for communication between server e client: each client has its own socket.

First example:
Client sends a string to the server,
Server makes the strig uppercase and sends it back to the client
The client recieves the modified string and print the string.


