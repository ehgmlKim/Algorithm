n = int(input())
answer = 0

for _ in range(n):
    str = input()
    dict = {}
    find = True # 그룹단어인지 체크하는 변수
    for s in str:
        # 해당 단어가 문자열에 2번 이상 나오면
        if str.count(s)>1:
            # 단어가 첫번째로 나온 부분부터 나온 횟수만큼 문자열을 잘라 연속인지 판단
            if str[str.index(s):str.index(s)+str.count(s)] != s*str.count(s) :
              find = False # 연속이 아니라면 find의 값이 fase로 바뀐다
              break
    if find: # 그룹 단어이면 +1
      answer += 1
              
    
print(answer)