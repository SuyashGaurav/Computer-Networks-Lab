## Refer to README for details

import socket
import cv2
import pickle
import struct

#creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

print("Host IP: ", host_ip)
port = 9999
socket_address = (host_ip, port)

#socket bind
server_socket.bind(socket_address)

#socket listen
server_socket.listen(5)
print("Listening on port: ", socket_address)

#socket accept
while True:
    client_socket, addr = server_socket.accept()
    print("Got connection from: ", addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            image, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()



