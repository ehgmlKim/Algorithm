dic = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
str = input()
answer = 0
for s in str:
    for k,v in dic.items():
        if s in k:
            answer += (v+1)
print(answer)