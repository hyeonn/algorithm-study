# enumerate 함수 사용해보기, 정답 입력 부분 for 문으로 고쳐보기
def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            count[0] += 1
        if answers[i] == two[i%len(two)]:
            count[1] += 1
        if answers[i] == thr[i%len(thr)]:
            count[2] += 1
            
    win = max(count)
    if count[0] == win:
        answer.append(1)
    if count[1] == win:
        answer.append(2)
    if count[2] == win:
        answer.append(3)
        
    return answer