c=int(input())
for i in range(c):
    cnt = 0
    arr=list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0]
    for i in range(arr[0]):
        if arr[i+1] > avg:
            cnt += 1
        rate = cnt/arr[0]*100
    print('{:.3f}%'.format(rate))