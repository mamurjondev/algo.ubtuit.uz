n = int(input())
arr=[]
arr.append(0)
arr.append(1)
a=0
a1=1
for i in range(1,n+1):
    a+=a1
    arr.append(a)
    a1+=a
    arr.append(a1)
print(arr[n-1])    
