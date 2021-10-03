def merge_sort(arr):
    n = len(arr)
    # 정렬할 리스트의 자료 개수가 1개 이하일 때 리턴
    if n <= 1:
        return arr

    # 리스트를 반으로 나누어 각각 다시 머지소트
    mid = n // 2
    a = merge_sort(arr[:mid]) # 앞부분 정렬 (재귀)
    b = merge_sort(arr[mid:]) # 앞부분 정렬 (재귀)

    result = [] # merge된 결과 저장

    # 하나가 빌 때 까지 반복
    while a and b:
        # 작은 값을 리스트에 저장
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

        # 하나의 리스트가 비면 남아있는 리스트를 순서대로 추가해줌
        while a:
            result.append(a.pop(0))
        while b:
            result.append(b.pop(0))
        return result

d = [4,2,6,7,9,3,8,1,10,5]
print(merge_sort(d))
