import socket
import random
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost', 9999))
rand_num = str(random.randint(1, 100))
name = "Client-210010054"
data_to_send = f"{name}|{rand_num}"
c.send(bytes(data_to_send, 'utf-8'))

try:
    server_name, rand_server_num = c.recv(1024).decode().split("|") #buffer size
    print("Server name: ", server_name, "|| Random Server Integer Received: ", rand_server_num)
except:
    c.close()
c.close()
