import random

x = random.randint(99, 1000) 
a=[0]*3
a[0]=x%10
a[1]=int((x/10)%10)
a[2]=int(x/100)
print(x)
y=input()
b=[0]*3
b[0]=x%10
b[1]=int((x/10)%10)
b[2]=int(x/100)

if y==x:
    print("yes babe")   
elif a[0]==b[0]:
    if a[1]==b[1]:
        print("last 2 number is correct")
    elif a[2]==b[2]:
        print("midell number is wrong")
    else:
        massage=str("0010")
elif a[1]==b[1]:
    if a[2]==b[2]:
        print(" last number is false")
    else:
        print("midell is correct")
elif a[2]==b[2]:
    print("firt number is correct")
else:
     massage=str("0000")
            