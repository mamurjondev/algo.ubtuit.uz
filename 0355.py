ab=input().split(" ")
cd=input().split(" ")
xy=input().split(" ")
a = int(ab[0])**int(ab[1])
c = int(cd[0])**int(cd[1])
x = int(xy[0])**int(xy[1])
if max(a,c,x)==a:
	print(ab[0]+" "+ab[1])
elif max(a,c,x)==c:
	print(cd[0]+" "+cd[1])
else:
	print(xy[0]+" "+xy[1])
if min(a,c,x)==a:
	print(ab[0]+" "+ab[1])
elif min(a,c,x)==c:
	print(cd[0]+" "+cd[1])
else:
	print(xy[0]+" "+xy[1])
