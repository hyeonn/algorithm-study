# 시간복잡도
# Worst O(n^2), Average : O(nlogn), Best - O(nlogn)

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 정석적인 방식
def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗 => 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


# 파이썬의 장점을 살린 quick sort
def quick_sort_py(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

a = arr # 복제

# 정석적인 방식
quick_sort(a, 0, len(a) - 1)
print(a)

# 파이썬의 장점을 살린 방식
print(quick_sort_py(arr))



