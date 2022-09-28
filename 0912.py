n = int(input())
q = 0
for i in range(n,n+10):
	if i%3==0:
		q = int(i/3)
		break
print(q)  
