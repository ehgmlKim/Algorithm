from itertools import permutations
import sys 
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]

for i in permutations(arr, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break