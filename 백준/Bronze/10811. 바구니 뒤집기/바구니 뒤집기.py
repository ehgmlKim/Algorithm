import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    for _ in range((j-i+1)//2):
        arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
        i += 1
        j -= 1
for a in arr:
    print(a, end=' ')
