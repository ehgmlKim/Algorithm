def solution(answers):
    answer = []
    
    l = len(answers)
    
    o = l//5+1
    t = l//8+1
    th = l//10+1
    one = '12345'*o
    two = '21232425'*t
    three = '3311224455' * th
    
    dict = {1:0, 2:0, 3:0}
    for i in range(l):
        if answers[i] == int(one[i]):
            dict[1] += 1
        if answers[i] == int(two[i]):
            dict[2] += 1
        if answers[i] == int(three[i]):
            dict[3] += 1
    dict = sorted(dict.items(), key = lambda x : x[1], reverse = True)
    max = dict[0][1]
    for k, v in dict:
        if v == max:
            answer.append(k)
    return sorted(answer)