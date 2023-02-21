x, y, w, h = map(int, input().split())
answer = min(w-x, x, h-y, y)
print(answer)