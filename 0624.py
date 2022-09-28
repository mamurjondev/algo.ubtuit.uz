a = list(map(int, input().split(":")))
q = ''
for i in range(1,len(a)+1):
	q+=str(min(a))+" "
	a.remove(min(a))
print(q.strip(" "))    
