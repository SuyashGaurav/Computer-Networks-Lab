from datetime import datetime
from socket import *
from time import time

port = 12000
serverHost = "localhost"
serverAddr = (serverHost, port)
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1, 11):
    dt = datetime.now()
    msg = f'Ping {i} {dt}'
    print(f"{msg}")
    msg = msg.encode()
    clientSocket.sendto(msg, serverAddr)
    clientSocket.settimeout(1)

    try:
        newMsg, serverAddress = clientSocket.recvfrom(1024)
        dt2 = datetime.now()
        rtt = dt2 - dt
        rtt_seconds = rtt.microseconds / 1e6
        print(f"Response: {newMsg.decode()} RTT: {rtt_seconds:.10f} seconds\n")

    except timeout:
        print("Request time out!\n")
    if(i==10):
        clientSocket.close()
