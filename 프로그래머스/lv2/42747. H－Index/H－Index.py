def solution(citations):
    #인용수로 내림차순
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)