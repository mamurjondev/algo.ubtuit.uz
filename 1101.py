a=input().split("\n")
n=int(a[0])
q=0
for i in a[1].split(" "):
    if int(i)%2==1:
        q+=1
print(q**2)    
