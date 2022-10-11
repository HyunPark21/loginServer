from socket import *

client = socket(AF_INET, SOCK_STREAM)  # create socket to connect
client.connect(('127.0.0.1', 8889))  # connect to server
userID = ""
userPassword = ""
while userID == "":
    userID = input("Enter ID: ")
    if userID == "":
        print("invalid input")
while userPassword == "":
    userPassword = input("Enter Password: ")
    if userPassword == "":
        print("invalid input")

client.send(userID.encode('UTF-8'))  # send + encode string to byte
client.send(userPassword.encode('UTF-8'))  # send + encode string to byte
print(client.recv(1024).decode('utf-8'))
client.close()