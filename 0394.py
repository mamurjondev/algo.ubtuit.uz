n = int(input())
q = 0
for i in str(n):
	q+=int(i)
w = 0
for j in range(n+1,n+10000):
	for k in str(j):
		w+=int(k)
	if w == q and 1<=n<10**6:
		print(j)
		break
	w = 0
    
