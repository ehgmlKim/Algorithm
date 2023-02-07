N = int(input())
count = 0
O = N
while True:
    count = count + 1
    sum = N%10 + int(N/10) #자리수 합
    N = (N%10)*10 + sum%10
    if O == N:
        break
print(count)
     