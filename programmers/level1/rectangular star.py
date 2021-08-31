# map과 print의 end옵션 공부해보기
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print('*', end="")
    print()