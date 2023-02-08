def solution(my_string):
    answer = []
    for e in my_string:
        try :
            int(e)
            answer.append(int(e))
        except:
            pass
    return sorted(answer)