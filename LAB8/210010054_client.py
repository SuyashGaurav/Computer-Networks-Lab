import socket
from base64 import b64encode
import ssl

# Add in prompt
userEmail = "smtplab23@gmail.com"
userPassword = "lmvgusmmhxkmzoti"
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")
msg = '{}.\r\n I love computer networks!'.format(userBody)


# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailserver = ("smtp.gmail.com", 587)
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Account authentication
clientSocket.send("STARTTLS\r\n".encode())
clientSocket.recv(1024)
sslClientSocket = ssl.wrap_socket(clientSocket)
sslClientSocket.send("AUTH LOGIN\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userEmail.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userPassword.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
print("Logged In!!")

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = "MAIL FROM: <{}>\r\n".format(userEmail)
sslClientSocket.send(mailFromCommand.encode())
print("MAIL FROM command: " + sslClientSocket.recv(1024).decode())
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <{}>\r\n".format(userDestinationEmail)
sslClientSocket.send(rcptToCommand.encode())
print("RCPT TO command: " + sslClientSocket.recv(1024).decode())
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
sslClientSocket.send(dataCommand.encode())
print("DATA command: " + sslClientSocket.recv(1024).decode())
# Fill in end

# Send message data.
#Fill in start
subject = "Subject:"+userSubject+"\r\n\r\n" 
sslClientSocket.send(subject.encode())
sslClientSocket.send((msg+"\r\n").encode())
#Fill in end

# Message ends with a single period.
# Fill in start
sslClientSocket.send(".\r\n".encode())
print(sslClientSocket.recv(1024).decode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
sslClientSocket.send(quitCommand.encode())
print(sslClientSocket.recv(1024).decode())
# Fill in end

sslClientSocket.close()