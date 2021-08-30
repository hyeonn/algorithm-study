def solution(price, money, count):
    answer = 0
    i = 1
    while i<=count:
        answer += price*i
        i += 1
        
    if answer < money:
        return 0
    else:
        return answer-money