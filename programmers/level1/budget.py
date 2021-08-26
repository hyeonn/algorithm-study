def solution(d, budget):
    answer = len(d)
    d.sort()
    # 예산보다 작아질 때 까지 큰 금액을 빼기
    while sum(d)>budget:
        d.pop()
        answer -= 1

    return answer