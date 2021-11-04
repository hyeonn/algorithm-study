N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for p in people:
    rank = 1
    for n in people:
        if (p[0] != n[0]) & (p[1] != n[1]):
            if (p[0] < n[0]) & (p[1] < n[1]):
                rank += 1

    print(rank)