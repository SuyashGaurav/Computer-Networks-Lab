## Refer to README for details

import socket
import cv2
import pickle
import struct

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '10.200.243.123'      #####  YOUR SERVER'S IP ADDRESS  ###### 

port = 9999
client_socket.connect((host_ip, port))
data = b""
payload_size = struct.calcsize("Q")  # unsigned long long int (8 bytes)

vid = cv2.VideoCapture(0)

while True:
    # Capture and send client's video
    ret, client_frame = vid.read()
    client_frame = cv2.resize(client_frame, (320, 240))     #Adjusting frame size to improve quality
    data = pickle.dumps(client_frame)
    message = struct.pack("Q", len(data)) + data
    client_socket.sendall(message)

    # Receive and display server's video
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
    # cv2.imshow("RECEIVING VIDEO", frame)

    # Display received and local video
    cv2.imshow("RECEIVING VIDEO", frame)
    cv2.imshow("Me", client_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

client_socket.close()
