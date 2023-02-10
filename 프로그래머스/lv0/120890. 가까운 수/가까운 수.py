def solution(array, n):
    array = sorted(array)
    min = (n-array[0])**2
    answer = array[0]
    for e in array :
        if (n-e)**2 < min :
            min = (n-e)**2
            answer = e
    return answer