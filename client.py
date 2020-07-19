

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= socket.gethostname()
ip = socket.gethostbyname(host)
server=(ip,8585)
s.connect(server)
connect=True
while connect:
    massage=s.recv(1024).decode()
    if massage=='0':
        connect=False
    else:
        print(massage)
        message = input('Your Message : ')
        s.send(message.encode())