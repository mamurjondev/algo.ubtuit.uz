n = input()
a=0
q=[]
for i in n:
    a+=1
    if i=="A" or i=="a":
        q.append(a)
z=''
for j in q:
    z+=" "+str(j)
print(z.strip(" "))    
