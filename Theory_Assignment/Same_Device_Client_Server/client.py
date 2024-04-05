## Refer to README for details

import socket
import cv2
import pickle
import struct

#create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

port = 9999
client_socket.connect((host_ip, port))
data = b""
payload_size = struct.calcsize("Q")  #unsigned long long int (8 bytes)

while(True):
    while(len(data) < payload_size):
        packet = client_socket.recv(4096)
        if not packet:
            break
        data = data + packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    
    while(len(data) < msg_size):
        data = data + client_socket.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
client_socket.close()
