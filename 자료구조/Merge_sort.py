def merge_sort(arr):
    n = len(arr)
    # 정렬할 리스트의 자료 개수가 한 개 이하이면 리턴
    if n <= 1:
        return arr

    # 리스트를 반으로 나누어 각각 머지소트 호출
    mid = n // 2
    a = merge_sort(arr[:mid]) # 앞부분 정렬 (재귀)
    b = merge_sort(arr[mid:]) # 앞부분 정렬 (재귀)

    result = [] # merge된 결과 저장

    # 두 리스트에 모두 자료가 남아있는 동안 반복
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
