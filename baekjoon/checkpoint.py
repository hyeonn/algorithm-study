# 약수 리스트
def div(x):
    div_list = [x]
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x // i != i:
                div_list.append(x // i)
    div_list.sort()
    return div_list

# 유클리드 호제법
def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

if __name__ == "__main__":
    N = int(input())
    freight = []
    for _ in range(N):
        freight.append(int(input()))
    freight.sort(reverse=True)

    # 차이 입력
    diff = []
    for i in range(len(freight) - 1):
        diff.append(freight[i] - freight[i + 1])

    # 화물들 차이 구하기 - 최대공약수
    if len(diff) == 1:
        answer = diff[0]
    elif len(diff) == 2:
        answer = gcd(diff[0], diff[1])
    else:
        answer = diff[0]
        for i in range(1, len(diff)):
            answer = gcd(answer, diff[i])

        # 모든 약수 출력
    for i in div(answer):
        print(i, end=' ')