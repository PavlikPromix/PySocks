import socket

soc = socket.socket() #creating socket() object
soc.bind(('', 9090)) #binding our server to sertain type of connection (argument 1) and port (argiment 2)
soc.listen(1) #starting to listen port for incoming connections
conn, addr = soc.accept() #accepting incoming connections; method .accept() returns new socket (conn) and client's address (addr)

print(addr, " connected")

while True:
    data = conn.recv(1024) #receiving 1Kb of data
    print (data.decode('utf-8'))
    if not data:
        break
    conn.send(data.upper()) #sending answer
conn.close() #closing connection