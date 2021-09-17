a =set()

for i in range(10):
    n = int(input())
    a.add(n%42)
print(len(a))