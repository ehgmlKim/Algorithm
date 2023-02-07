def solve(n):
    cnt = 99
    if n<100:
        return n
    else:
        for i in range(n, 100, -1):
            arr = [int(n) for n in str(i)]
            if arr[1]*2==arr[0]+arr[2]:
                cnt += 1
        return cnt
n=int(input())
print(solve(n))
