def cal(n):
    answer = 0
    i=0
    while n>0 :
        answer += (n%10)*(2**i)
        i += 1
        n = n//10
    return answer
def solution(bin1, bin2):
    answer = ''
    bin3 = str(bin(cal(int(bin1)) + cal(int(bin2))))
    return bin3[2::]