o = input().split(" ")
a = int(o[0])
b = int(o[1])
c = int(o[2])
if (a+b>c and a+c>b and b+c>a) and (a>0 and b>0 and c>0):
    if ((a**2 == b**2+c**2) or (b**2==c**2+a**2) or (c**2==a**2+b**2)):
        print(1)
    elif (a==b and b!=c) or (c==b and b!=a) or (a==c and b!=c):
        print(2)
    elif a == b == c:
        print(3)
    else:
        print(4)
    
