import socket 

sock = socket.socket() #creating socket() obj
sock.connect(('localhost', 9090)) #connecting to 'localhost' with port 9090
sock.send('hello, world!') #sending message to 'localhost'

data = sock.recv(1024) #receiving message from 'localhost'
sock.close() #closing connection

print (data) 