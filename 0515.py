ab = input().split(" ")
t = float(ab[0])
P = float(ab[1])
m = float(ab[2])
n = t+273
P = P*133
m = m/1000
v = (m*8.31*n)/(P*0.032)
print(f"{v:.4f}") 
