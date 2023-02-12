def solution(numlist, n):
    answer = []
    numlist = sorted(numlist, reverse = True)
    numlist = sorted(numlist, key = lambda x : abs(n-x))
    return numlist