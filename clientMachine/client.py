import socket 
import io
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

sock = socket.socket() #creating socket() obj
sock.connect((input("Enter ip: "), 9090)) #connecting to 'localhost' with port 9090
uin = ''
while uin != '!exit':
    uin = input("$ ")
    if uin == '!img':
        try:
            byteImgIO = io.BytesIO()
            byteImg = Image.open(input("Path to image: "), "r")
            byteImg.save(byteImgIO, "PNG")
            byteImgIO.seek(0)
            byteImg = byteImgIO.read()
            sock.send(byteImg)
        except FileNotFoundError:
            print("This file isn't exists")
    elif uin == '!help':
        print ("\nHelp executed\n\n!img - starts image sending process\n\n!help - what is wrong with you!?\n\n!exit - will close this program\n")
    else:
        sock.send(bytes(uin, 'utf-8')) 

data = sock.recv(10485760) #receiving message from 'localhost'
sock.close() #closing connection
