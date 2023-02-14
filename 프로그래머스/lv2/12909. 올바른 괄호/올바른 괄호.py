def solution(s):
    stack=[]
    for i in s :
        if i == ')':
            if len(stack) == 0:
                return False
            else :
                x = stack.pop()
                if x != '(' :
                    return False
        else :
            stack.append(i)
    if len(stack) != 0:
        return False
    return True