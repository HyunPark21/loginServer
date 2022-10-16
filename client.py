from socket import *
import sys
from time import sleep


# sign up
def signUp():
    send = "1"  # 1 means signup
    newID = ""
    newPassword = ""
    while newID == "":
        newID = input("Enter ID: ")
        if newID == "":
            print("invalid input")
    while newPassword == "":
        newPassword = input("Enter Password: ")
        if newPassword == "":
            print("invalid input")
    client.send(send.encode('UTF-8'))  # send + encode string to byte
    sleep(1)
    client.send(newID.encode('UTF-8'))  # send + encode string to byte
    sleep(1)
    client.send(newPassword.encode('UTF-8'))  # send + encode string to byte
    print(client.recv(1024).decode('utf-8'))


# sign in
def sign_in():
    send = "2"  # 2 is for sign in
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
    client.send(send.encode('UTF-8'))  # send + encode string to byte
    sleep(1)
    client.send(userID.encode('UTF-8'))  # send + encode string to byte
    sleep(1)
    client.send(userPassword.encode('UTF-8'))  # send + encode string to byte
    print(client.recv(1024).decode('utf-8'))


try:
    client = socket(AF_INET, SOCK_STREAM)  # create socket to connect
    client.connect(('127.0.0.1', 8889))  # connect to server
except:
    print("Fail to connect to the server")
    sys.exit()

user_input = 0  # what user wants to do
while user_input != '3':
    print("Hello, choose your option")
    print("1. sign up")
    print("2. sign in")
    print("3. terminate")
    user_input = input("Enter choice: ")
    if user_input == '1':
        signUp()
    if user_input == '2':
        sign_in()
# after sign in
client.shutdown(2)
client.close()
