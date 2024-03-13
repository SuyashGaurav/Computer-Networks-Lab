# python 210010054_webserver.py    [Terminal]
# http://127.0.0.1:9998/HelloWorld.html    [Browser]

import socket
port = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', port))   #we can use our IP instead of localhost.
s.listen(1)

print ('Listening on the port: ', port)

while True:
    c, addr = s.accept()
    try:
        message = c.recv(1024).decode()
        filename = message.split("/")[1].split()[0]
        input = open(filename)
        result =input.read()
        result = 'HTTP/1.1 200 OK\n\n'+result
        print(result.encode())
        c.sendall(result.encode())
    except:
        result = 'HTTP/1.1 404 Not Found\n\n404 Not Found'
        c.sendall(result.encode())
    c.close()

s.close()

