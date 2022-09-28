n = int(input())
yig = 0
kop = 1
for i in str(n):
    yig += int(i)
    kop *= int(i)
print(f"{kop/yig:.3f}")    
