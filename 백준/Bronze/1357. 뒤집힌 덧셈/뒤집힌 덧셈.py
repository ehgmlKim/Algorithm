import sys
input = sys.stdin.readline

x,y = input().split()
def func(n):
  n = list(n)
  n.reverse()
  return ''.join(n)
print(int(func(str(int(func(x))+int(func(y))))))