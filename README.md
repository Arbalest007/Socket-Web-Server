PUT NAMES AND EMAILS
# Socket-Web-Server

## Server
Navigate to the folder with the programs.

Run the command to start the server.
>python3 server.py


The terminal will tell you your IP address and a PORT number.

In the web browser, type the IP address and PORT number with a colon separating them and the html filename that is included.
(10.10.10:1024/HelloWorld.html)

You should receive this on your browser

<img src="https://github.com/Arbalest007/Socket-Web-Server/assets/47013008/929f22c3-fbd9-472f-b1c2-cfee678c6064" width="500" height="400">

You will get this if you type the filename wrong

<img src="https://github.com/Arbalest007/Socket-Web-Server/assets/47013008/ebc142b5-cbff-451b-8ee9-58aa21d9820c" width="500" height="400">


## Client
To test the client

Start the server with "python3 server.py"

Open another terminal window and type "python3 client.py IP PORT FILENAME"
(python3 client.py 10.10.10 1024 HelloWorld.html)

You will receive the server response in the terminal

<img src="https://github.com/Arbalest007/Socket-Web-Server/assets/47013008/b72415ef-9d93-4a22-8e4a-74eb859e204b" width="500" height="400">



