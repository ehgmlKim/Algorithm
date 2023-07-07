def solution(citations):
    answer = 0
    l = len(citations)
    citations=sorted(citations, reverse = True)
    h = citations[0]
    for i in range(h, 0, -1):
        len1 = len([x for x in citations if x<=i])
        len2 = len([x for x in citations if x>=i])
        if len1<=i and len2 >= i:
            return i
        
    
    return answer