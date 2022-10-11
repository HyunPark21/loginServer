# This is a project to learn server and socket in python
import socket
# import socket
from socket import *
import sys
from Database import Database

# create socket of server
host = '127.0.0.1'
port = 8889
server = socket(AF_INET, SOCK_STREAM)  # create socket connecting internet, stream version
db = Database()
try:
    server.bind((host, port))  # use my ip address, port number = 8888
    server.listen(1)  # one can wait in line
    print('server start...')

    while True:
        conn, addr = server.accept()  # create another socket to communicate with client
        userID = conn.recv(1024).decode('utf-8')  # decode bye to string
        userPW = conn.recv(1024).decode('utf-8')  # decode bye to string
        pw = db.getpassword(userID)
        print(pw)
        print(userPW)
        if pw == userPW:
            print(userID + " is logged in")
            greeting = "Hello," + userID
            conn.send(greeting.encode('UTF-8'))
        else:
            print("Invalid attempt was made")
            conn.send("Invalid input".encode('UTF-8'))
except socket.error as err:
    print('Socket Error: ', err)
    sys.exit()
finally:
    server.close()
