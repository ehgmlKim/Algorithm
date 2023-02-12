def solution(my_string):
    answer = 0
    str = ''
    append=[]
    for i in range(len(my_string)) :
        if my_string[i].isalpha() != True  :
            str+=my_string[i]
            if i+1==len(my_string) or my_string[i+1].isalpha() == True :
                answer += int(str)
                str=''
    return answer