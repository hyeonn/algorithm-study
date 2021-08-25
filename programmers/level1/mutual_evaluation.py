def getGrade(ave):
    grade = 'F'
    if (ave>=90):
        grade = 'A'
    elif (ave>=80):
        grade = 'B'
    elif (ave>=70):
        grade = 'C'
    elif (ave>=50):
        grade = 'D'
        
    return grade

def solution(scores):
    answer = ""
    for i in range(len(scores)):
        arr = []
        for j in range(len(scores)):
            arr.append(scores[j][i])
        s = sum(arr)
        count = len(arr)
        if (arr[i] == min(arr) and arr.count(min(arr)) == 1):
            s -= arr[i]
            count -= 1
        elif (arr[i] == max(arr) and arr.count(max(arr)) == 1):
            s -= arr[i]
            count -= 1
                    
        answer += getGrade(s/count)

    return answer