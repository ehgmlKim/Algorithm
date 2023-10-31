import sys
input = sys.stdin.readline

n = int(input())
r = 0
answer = 0

m = n
while n>0:
  n = n//10
  r += 1


for i in range(1, r+1):
  answer += i*9*(10**(i-1))

answer -= (10**r-1-m)*r
print(answer)