# 백트래킹 개념 찾아보고 공부하기

import sys
# 재귀 한도 에러가 뜨지 않도록 limit 설정하기
sys.setrecursionlimit(10000)


def serch(n):
    num = 1
    cnt = 0
    while True:
        num_to_str = str(num)
        flag = True
        # 길이가 1이면 무조건 감소하는 수
        if len(num_to_str) == 1:
            pass
        else:
            for i in range(1, len(num_to_str)):
                if int(num_to_str[i]) < int(num_to_str[i - 1]):
                    continue
                else:
                    s = num_to_str[:i - 1]
                    m = str(int(num_to_str[i - 1]) + 1)
                    e = '0' + num_to_str[i + 1:]
                    num = int(s + m + e)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1

n = int(sys.stdin.readline())
if n >= 1023:
    print(-1)
elif n == 0:
    print(0)
else:
    print(serch(n))