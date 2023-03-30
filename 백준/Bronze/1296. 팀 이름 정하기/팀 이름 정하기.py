import sys

input = sys.stdin.readline
name = input().rstrip()

N = int(input())
dict = {}
for i in range(N):
  team = input().rstrip()
  L = name.count('L') + team.count('L')
  O = name.count('O') + team.count('O')
  V = name.count('V') + team.count('V')
  E = name.count('E') + team.count('E')
  val = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
  dict[team] = val
  
dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(dict[0][0])