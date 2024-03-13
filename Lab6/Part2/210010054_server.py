import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = "210010054_server"
print("Socket Created")

s.bind(('localhost', 9999))
s.listen(1)
print("Waiting for the connections...")

while True:
    c, addr = s.accept()  #client, and its address
    name, rand_client_num = c.recv(1024).decode().split("|")
    rand_client_num = int(rand_client_num)
    try:
        if not (1 <= rand_client_num <= 100):
            print("Received random number out of range. Terminating server.")
            break
    except ValueError:
        print("Received non-integer value. Terminating server.")
        break

    print("Connected to the client ", addr, name, "|| Server Name: ", server_name)
    rand_server_num = random.randint(1, 100)
    print("Server Random Number: ", rand_server_num, " || ", "Client Random Number: ", rand_client_num, " || ", "Sum: ", int(rand_client_num)+rand_server_num)
    
    data_to_send = f"{server_name}|{rand_server_num}"
    c.send(bytes(data_to_send, 'utf-8')) 
    c.close()

print("Closing the socket")
s.close()