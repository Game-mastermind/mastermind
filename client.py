import socket

counter=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= socket.gethostname()
ip = socket.gethostbyname(host)
server=(ip,8585)
s.connect(server)
connect=True
while connect:
    H=s.recv(1024).decode()
    if counter>0:
        M=[0]*4
        M=H
        print(H) 
        print(M[3])
        if M[3]=='0':
            s.send("0000".encode())
            P=s.recv(1024).decode()
            print(P)
            connect=False 
                  
       
    if connect:
        A = input('please enter 3 number ')
        A=int(A)
        if counter<7:
            massage=(A*10)+1
        else :
            massage=A*10  
        massage=str(massage)      
        s.send(massage.encode())
        counter=counter+1
        if counter==8:
            M=s.recv(1024).decode()
            print(M)
            connect=False
