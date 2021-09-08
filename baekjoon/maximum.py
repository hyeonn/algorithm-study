a = [0 for i in range(9)]
for i in range(9):
    a[i] =int(input())
m = max(a)
print(m)
print(a.index(m)+1)