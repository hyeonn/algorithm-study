def solution(n):
    answer = ""
    while n > 0: 
        n, mod = divmod(n, 3) 
        answer = answer + str(mod) 
    answer = int(answer, 3)
    return answer