import sys
n = int(sys.stdin.readline())
arr = [0] * 10000 # 수의 최댓값만큼 배열 생성
for _ in range(n):
  arr[int(sys.stdin.readline())-1] += 1

for i in range(10000):
  if arr[i]:
    for _ in range(arr[i]):
      print(i+1)