def solution(arr):
    min_v = min(arr)
    arr.remove(min_v)
    if len(arr):
        return arr
    else:
        return [-1]
