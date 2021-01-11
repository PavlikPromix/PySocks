import socket
import os
import io
import PIL.Image as Image
from PIL import ImageFile
from array import array
ImageFile.LOAD_TRUNCATED_IMAGES = True

def decim(dta):
    image = Image.open(io.BytesIO(dta))
    image.save("received.png")

soc = socket.socket() #creating socket() object
soc.bind(('', 9090)) #binding our server to sertain type of connection (argument 1) and port (argiment 2)
soc.listen(1) #starting to listen port for incoming connections
conn, addr = soc.accept() #accepting incoming connections; method .accept() returns new socket (conn) and client's address (addr)

print(addr, " connected")

while True:
    data = conn.recv(10240000) #receiving 10Mb of data
    if not data:
        break
    if data.decode('utf-8') == 'img':
        data = conn.recv(10240000)
        decim(data)
        conn.send(bytes("Image received!", 'utf-8'))
    else:
        conn.send(data.upper()) #sending answer
conn.close() #closing connection