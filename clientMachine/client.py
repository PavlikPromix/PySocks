import socket 
import os
import time

sock = socket.socket() #creating socket() obj
sock.connect(('localhost', 9090)) #connecting to 'localhost' with port 9090
uin = input("$ ")
if uin == 'img':
    img = open(input("File path or name: "), "rb")
    f = img.read()
    imb = bytearray(f)
    sock.send(bytes("img", 'utf-8')) 
    time.sleep(0.5)
    sock.send(imb)
else:
    sock.send(bytes(uin, 'utf-8')) #sending message to 'localhost'

data = sock.recv(10240000) #receiving message from 'localhost'
sock.close() #closing connection

print (data.decode('utf-8')) 
