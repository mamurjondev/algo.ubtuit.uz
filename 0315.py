import math
ab = input().split(" ")
a = int(ab[0])
b = int(ab[1])
if a>0 and b>0:
    print(f"{(a*b):.1f}")
elif a<0 and b<0:
    print(f"{((a+b)/2):.1f}")
else:
    print(f"{(abs(a)+abs(b)):.1f}")        
