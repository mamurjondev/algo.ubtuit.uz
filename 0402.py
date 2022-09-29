n = int(input())
a=list(map(int, input().split()))
mu=0
ma=0
for i in a:
    if i>0:
        ma+=1
    elif i<0:
        mu+=1
print(mu*ma)   
