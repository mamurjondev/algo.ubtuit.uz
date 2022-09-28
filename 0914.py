n = int(input())
q = 0
for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        q += 1
print(q)
