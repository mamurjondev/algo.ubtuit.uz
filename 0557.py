n = list(map(int, input().split(" ")))
a = n[0]
b = n[1]
c = n[2]
d = n[3]
if a + b + c > d and a + c + d > b and a + b + d > c and b + c + d > a:
    print("Possible")
else:
    print("Impossible")    
