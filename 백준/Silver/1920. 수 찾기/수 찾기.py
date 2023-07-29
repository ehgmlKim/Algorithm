import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dict = {x:0 for x in A}

m = int(input())
B = list(map(int, input().split()))

for a in B:
  if a in dict:
    print(1)
  else:
    print(0)
