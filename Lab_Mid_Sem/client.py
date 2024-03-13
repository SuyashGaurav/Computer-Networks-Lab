import socket

c = socket.socket()
c.connect(("localhost", 9999))

while True:
    result = c.recv(1024).decode()
    print(result)

    data = input("Enter your choice:")
    if(data == "QUIT"):
        break
    c.send(data.encode())
    
c.close()