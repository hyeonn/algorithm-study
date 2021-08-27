def solution(nums):
    answer = 0
    species = []
    for i in nums:
        if i not in species:
            species.append(i)
    # 포켓몬의 종류가 가져가는 포켓몬 보다 적으면 종류의 개수만큼 가져가는 것이 최대치
    # 종류가 더 많으면 가져가는 개수만큼이 최대치
    if len(species) < (len(nums)/2):
        return len(species)
    else:
        return len(nums)/2