while True:
    s = input()
    stack = []
    # 입력의 종료조건
    if s == ".":
        break

    for j in s:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                break
        elif j == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")

# 런타임 에러
# while True:
#     flag = 0
#     small = []
#     large = []
#     s = input()
#     for j in s:
#         if j == '(':
#             small.append(j)
#             flag = 1
#         elif j == ')':
#             if flag != 1:
#                 print("NO")
#                 break
#             else:
#                 if small:
#                     small.pop()
#                 else:
#                     print("NO")
#                     break
#         elif j == '[':
#             large.append(j)
#             flag = 2
#         elif j == ']':
#             if flag != 2:
#                 print("NO")
#                 break
#             else:
#                 if large:
#                     large.pop()
#                 else:
#                     print("NO")
#                     break
#     else:
#         if small or large:
#             print("NO")
#         else:
#             print("YES")
