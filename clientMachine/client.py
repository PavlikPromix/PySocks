import socket 
import os
import time

sock = socket.socket() #creating socket() obj
sock.connect((input("Enter ip: "), 9090)) #connecting to 'localhost' with port 9090
uin = input("$ ")
sock.send(bytes(uin, 'utf-8')) 
if uin == 'img':
    img = open(input("File path or name: "), "rb")
    f = img.read()
    print (img.read())
    imb = bytearray(f)
    time.sleep(1)
    sock.send(imb)

data = sock.recv(10485760) #receiving message from 'localhost'
sock.close() #closing connection

print (data.decode('utf-8')) 
