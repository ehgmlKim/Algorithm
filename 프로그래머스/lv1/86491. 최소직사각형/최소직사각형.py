def solution(sizes):
    answer = 0
    sizes = [sorted(x) for x in sizes]
    print(sizes)
    w = max([x[0] for x in sizes])
    h = max([x[1] for x in sizes])
    return w*h