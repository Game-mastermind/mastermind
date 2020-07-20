import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= socket.gethostname()
ip = socket.gethostbyname(host)
server=(ip,8585)
s.bind(server)
 
s.listen(10)

orginalConnection=True
while orginalConnection:
    c, addr = s.accept()
    x = random.randint(99, 1000) 
    a=[0]*3
    a[0]=x%10
    a[1]=int((x/10)%10)
    a[2]=int(x/100)
    print(x)

    print("we have a connection")
    h="you are connect" 
    c.send(h.encode())
    STRx=str(x)
    connection=True
    while connection:           

        m = c.recv(1028).decode()
        print(m)
        m = str(m)
        y=int(m)
        e=int(y%10)
        b=[0]*3
        b[0]=int(y/10)%10
        b[1]=int(y/100)%10
        b[2]=int(y/1000)%10
        y=int(y/10)
        if e==0:
            connection=False
            c.send(STRx.encode())
        else:
            if y==x:
                print("yes babe")
                massage=str("1110")
                c.send(massage.encode())
            elif a[0]==b[0]:
                if a[1]==b[1]:
                    print("last 2 number is correct")
                    massage=str("0111")
                    c.send(massage.encode())
                elif a[2]==b[2]:
                    print("midell number is wrong")
                    massage=str("1011")
                    c.send(massage.encode())
                else:
                    massage=str("0011")
                    c.send(massage.encode())
                    print("last number is correct")
            elif a[1]==b[1]:
                if a[2]==b[2]:
                    print(" last number is false")
                    massage=str("1101")
                    c.send(massage.encode())
                else:
                    print("midell is correct")
                    massage=str("0101")
                    c.send(massage.encode())
            elif a[2]==b[2]:
                print("firt number is correct")
                massage=str("1001")
                c.send(massage.encode())
            else:
                massage=str("0001")
                c.send(massage.encode())
                print("you gusse is wrong")            
    c.close()