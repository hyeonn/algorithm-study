# 반복문에서의 else 사용:
# break로 빠져나오지 않았을 경우에만 실행
# 즉 break 되면 실행되지 않음!

n = int(input())
for i in range(n):
    stack = []
    s = input()
    for j in s:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
