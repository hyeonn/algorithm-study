def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0
    # progresses 가 빌 때 까지 (FIFO)
    while progresses:
        if progresses[0] + day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer