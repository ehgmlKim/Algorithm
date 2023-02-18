a,b,c = map(int, input().split())
answer = a//(c-b)+1 if c>b else -1
print(answer)