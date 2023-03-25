def solution(citations):
    answer = []
    citations = sorted(citations)
    dict = {}
    for c in citations:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    print(dict)
    print(answer)