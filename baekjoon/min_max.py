n = int(input())
# 리스트 요소 입력받을 때 => input.split() / 요소를 int로 입력받고 싶을 때 => map(int, input().split())
# 꼭 리스트로 형변환 해야함!!!
a = list(map(int, input().split()))
print(min(a))
print(max(a))