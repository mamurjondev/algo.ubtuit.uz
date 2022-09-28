n = int(input())
h = 0
k = 1
while n//(5**k)!=0:
    h+=(n//(5**k))
    k+=1
print(int(h))  
