def solution(nums):
    answer = 0
    l = len(nums)
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    print(dic)
    answer = min(l//2, len(dic))
    return answer