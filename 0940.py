n = input().split(" ")
a = int(n[0])
b = int(n[1])
def dec(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal
q = str(bin(a)).split("b")
s = str(bin(b)).split("b")
w = q[1]+s[1]
print(dec(int(w)))
