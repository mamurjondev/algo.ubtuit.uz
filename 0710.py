s = int(input())
q = ''
a = str(s)
for i in a:
    q += str(i) + " "
if len(str(s)) == 0:
    print(s)
else:
    print(q.strip(" "))    
