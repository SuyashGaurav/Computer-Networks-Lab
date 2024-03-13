import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(2)
print("Listening on port 9999")

c1, addr1 = s.accept()
c1.send("Stone, Paper, Scissors".encode())
c2, addr2 = s.accept()
c2.send("Stone, Paper, Scissors".encode())

while True:
    data1 = c1.recv(1024).decode()
    data2 = c2.recv(1024).decode()
    print(data1, data2)

    if data1 == "QUIT" or data2 == "QUIT":
        break
    
    if (data1 == "Stone" and data2 == "Paper") or (data1 == "Paper" and data2 == "Scissors") or (data1 == "Scissors" and data2 == "Stone"):
        c1.send("You lose".encode())
        c2.send("You win".encode())
    elif data1 == data2:
        c1.send("It's a tie.".encode())
        c2.send("It's a tie.".encode())
    else:
        c1.send("You win".encode())
        c2.send("You lose".encode())
    

c1.close()
c2.close()

s.close()

