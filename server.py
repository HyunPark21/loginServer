# This is a project to learn server and socket in python
import socket
# This project only deal with one client

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
        print("User is connected")
        while True:
            data = conn.recv(1024).decode('UTF-8')  # while connected to a user
            if data:
                if data == "1":
                    id1 = conn.recv(1024).decode('UTF-8')
                    pw1 = conn.recv(1024).decode('UTF-8')
                    b = Database.sign_up(db, id1, pw1)
                    if b:
                        print("Sign up success, need to be approved")
                        conn.send("Successfully added to database, wait until approved".encode('UTF-8'))
                    else:
                        print("Sign up failed")
                        conn.send("Use other userName".encode('UTF-8'))

                if data == '2':
                    id1 = conn.recv(1024).decode('UTF-8')
                    pw1 = conn.recv(1024).decode('UTF-8')
                    get_pass = db.getpassword(id1)
                    if get_pass is None:
                        conn.send("No id on database".encode('UTF-8'))
                    if pw1 == get_pass:
                        conn.send("Hi user".encode('UTF-8'))
                    else:
                        conn.send("incorrect password".encode('UTF-8'))
            else:
                break
        print("disconnected from a user")
        conn.close()
except EOFError:
    print("Error on System")
    sys.exit()
finally:
    server.close()
