from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) != 4:
    print("Not enough arguments.")
    sys.exit()

# client.py 'IP that was given from starting server.py' 'port number given by server.py' 'filename'
HOST_IP = sys.argv[1]
PORT = int(sys.argv[2])
request = ("Get /" + sys.argv[3] + " HTTP/1.1").encode()


#while True:
clientSocket.connect((HOST_IP, PORT))
clientSocket.send(request)
# clientSocket.send(sys.argv[3])
# clientSocket.send("Get /" + sys.argv[3].encode() + " HTTP/1.1")

response = clientSocket.recv(1024)
print (response)

while True:
    data = clientSocket.recv(1024).decode()
   # filename = data.split()
    
    if not data:
      break

clientSocket.close()
