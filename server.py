from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

HOST_IP = gethostbyname(gethostname())
PORT = 1024

print("Server IP is: " + HOST_IP)
print("Port number is: " + str(PORT))

serverSocket.bind((HOST_IP, PORT))
serverSocket.listen()

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()

        # Debugging
        # print("The HTML file contains: ")
        # print(outputdata)

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n".encode())
        connectionSocket.send("404 Not Found".encode())
        connectionSocket.close()

    serverSocket.close()
    sys.exit()