n = int(input())
bi = bin(n)
q = 0
for i in str(bi):
	if i == '1':
		q+=1
print(q)    
