def solution(common):
    if common[1]*2 ==common[0]+common[2] :
        return common[len(common)-1] + common[1] - common[0]
    if common[1]**2 == common[0]*common[2] :
        return common[len(common)-1] * (common[1]/common[0])