import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
time = 0
for i in range(n):
  time += sum(arr[:i+1])

print(time)