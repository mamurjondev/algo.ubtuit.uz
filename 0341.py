n = int(input())
a=list(map(int, input().split()))
mu=0
ma=0
for i in a:
    if i%2==0:
        ma+=1
    elif i%2==1:
        mu+=1
print(ma)
print(mu)    
