import math
xy=input().split(" ")
x=int(xy[0])
y=int(xy[1])
S=abs(x-y+(abs(y)+2)**0.5-(x-(x+y)/(math.e**(y+1)-5)))+math.sin(x+y)/(x+y)**(1/3)
print(f"{S:.2f}")     
