def solution(nums):
    answer = 0
    pick = len(nums) // 2
    dup = len(set(nums))
    return min(pick, dup)