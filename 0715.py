n = int(input())
array = list(map(int, input().split(" ")))
arr=[]
for i in range(1,n+1,1):
    arr.append(max(array))
    array.remove(max(array))
q = ''
for j in arr[::-1]:
    q+=" "+str(j)
print(q.strip(" "))    
