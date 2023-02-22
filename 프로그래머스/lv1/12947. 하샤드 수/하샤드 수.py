def solution(x):
    if x%sum([int(i) for i in str(x)]):
        return False
    return True