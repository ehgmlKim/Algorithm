def solution(emergency):
    answer = sorted(emergency)
    array=[]
    for e in answer:
        array.append(len(emergency)-emergency.index(e))
    return array