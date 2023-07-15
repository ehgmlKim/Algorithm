def solution(nums):
    answer = 0
    n = len(nums)//2
    dict = {}
    arr = set(nums)
    answer = min(n, len(arr))
    return answer