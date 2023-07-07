import itertools

def solution(numbers):
    answer = 0
    arr = set()
    for i in range(1, len(numbers)+1):
        for a in itertools.permutations(numbers, i):
            num = int(''.join(a))
            if num != 1 and num != 0:
                arr.add(num)
    for a in arr:
        b = True
        for i in range(2, int(a**(1/2))+1):
            if a%i==0:
                b = False
                break
        if b:
            answer += 1
    return answer