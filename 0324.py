from math import cos
s = input().split(" ")
n = int(s[0])
x = float(s[1])
f = 0
for i in range(1,n+1,1):
    if i%2==1:
        f+=(1/i)*cos(x*i)
    else:
        f-=(1/i)*cos(x*i)
print(f"{f:.2f}")    
