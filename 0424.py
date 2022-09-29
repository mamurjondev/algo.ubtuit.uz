s = str(input())
q = 0
r = []
for i in s:
	if i=="1":
		q+=1
		r.append(q)
	elif i=="0":
		r.append(q)
		q=0
	else:
		r.append(q)
print(max(r))  
