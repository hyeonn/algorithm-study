import math, sys
# 재귀 한도 에러가 뜨지 않도록 limit 설정하기
sys.setrecursionlimit(10000000)

# 소수판별
def is_prime(num):
    n = int(num)
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def dfs(num):
    if len(num) == N:
        print(num)
        return
    for i in tail:
        if is_prime(num+i):
            dfs(num+i)

N = int(input())
head = ['2', '3', '5', '7']
tail = ['1', '3', '7', '9']

# head로 시작해야만 소수가 될 수 있음 (한 자리 수 소수)
for n in head:
    dfs(n)