## Refer to README for details

import socket
import cv2
import pickle
import struct

# Creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)   ##### WRITE THIS SERVER'S IP ADDRESS OBTAINED IN CLIENT.PY  ######

print("Host IP: ", host_ip)
port = 9999
socket_address = (host_ip, port)

# Socket bind
server_socket.bind(socket_address)

# Socket listen
server_socket.listen(5)
print("Listening on port: ", socket_address)

# Socket accept
client_socket, addr = server_socket.accept()
print("Got connection from: ", addr)
if client_socket:
    vid = cv2.VideoCapture(0)
    while True:
        # Receive and display client's video
        data = b""
        payload_size = struct.calcsize("Q")  # unsigned long long int (8 bytes)
        while len(data) < payload_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        # cv2.imshow('RECEIVING VIDEO', frame)

        # Capture and send server's video
        ret, server_frame = vid.read()
        server_frame = cv2.resize(server_frame, (320, 240))   #Adjusting frame size to improve quality
        data = pickle.dumps(server_frame)
        message = struct.pack("Q", len(data)) + data
        client_socket.sendall(message)

        cv2.imshow('RECEIVING VIDEO', frame)
        cv2.imshow("Me", server_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            client_socket.close()
            break

server_socket.close()
