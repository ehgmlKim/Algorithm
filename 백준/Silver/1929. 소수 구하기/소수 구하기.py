m, n=map(int, input().split())
for i in range(m,n+1):
    cnt = 0
    for j in range(2, int(i**(1/2))+1):
        if i%j==0:
            cnt = 1
            break
    if i!= 1 and not cnt:
        print(i)