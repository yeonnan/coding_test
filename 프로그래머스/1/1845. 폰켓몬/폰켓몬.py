def solution(nums):
    pocketmons = len(set(nums))
    select = len(nums) // 2
    return min(pocketmons, select)