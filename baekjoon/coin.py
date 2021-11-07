N,K = map(int, input().split())

w = []
for _ in range(N):
  w.append(int(input()))

count = 0
i = N-1
while K != 0:
  count += K//w[i]
  K %= w[i]
  i -= 1

print(count)