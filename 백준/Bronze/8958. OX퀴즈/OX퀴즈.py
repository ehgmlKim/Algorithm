n=int(input())


for i in range(n):
    sum = 0
    arr=input()
    score = 0
    for e in range(len(arr)):
       if arr[e] == 'O':
             score += 1
             sum += score
       else:
             score = 0
    print(sum)
        