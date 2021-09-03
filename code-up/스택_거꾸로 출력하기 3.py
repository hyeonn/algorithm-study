n = int(input())
# list 입력은 map 사용 map(int, input().split())
stack = list(map(int, input().split()))
for i in range(n):
    print(stack.pop(-1),end =" ")
