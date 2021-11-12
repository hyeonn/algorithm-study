n = int(input())
 
li = [] # 2차원리스트
for _ in range(n):
    xy = list(map(int,input().split()))
    li.append(xy)
    
li.sort()
for i in li:
    print(i[0],i[1])