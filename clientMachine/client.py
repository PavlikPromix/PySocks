import socket 
import io
import os
from PIL import Image

sock = socket.socket() #creating socket() obj
sock.connect((input("Enter ip: "), 9090)) #connecting to 'localhost' with port 9090
uin = ''
while uin != 'exit()':
    uin = input("$ ")
    if uin == 'img':
        try:
            with open(input("Path to image: "), "rb") as image:
                f = image.read()
                b = bytearray(f)
                sock.send(b)
        except FileNotFoundError:
            print("This file isn't exists")
    else:
        sock.send(bytes(uin, 'utf-8')) 

data = sock.recv(10485760) #receiving message from 'localhost'
sock.close() #closing connection
