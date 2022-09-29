import math
xy=input().split(" ")
a=int(xy[0])
b=int(xy[1])
c=int(xy[2])
p=(max(a,b,c)+min(a,b,c))/2
print(f"{p:.1f}")       
