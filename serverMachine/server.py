import socket
import os
import io
import PIL
from PIL import Image

def decim(dta):
    image = Image.open(io.BytesIO(dta))
    image.save("received.png")

soc = socket.socket() 
soc.bind(('', 9090)) 
soc.listen(1) 
conn, addr = soc.accept() 

print(addr, " connected")

while True:
    try:
        data = conn.recv(10485760) #receiving 10Mb of data
    except ConnectionAbortedError:
        print("Client disconnected")
        break
    except KeyboardInterrupt:
        print ("Server stopped")
    try:
        ddata = data.decode("utf-8")
        conn.send(data.upper())
    except UnicodeDecodeError:
        decim(data)
    except KeyboardInterrupt:
        print ("Download stopped")
    if not data:
        print ("Connection interrupted")
        break
    
conn.close() 