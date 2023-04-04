import sys
input = sys.stdin.readline
n = input()
a = ''.join(sorted(list(n), reverse=True))
print(a)