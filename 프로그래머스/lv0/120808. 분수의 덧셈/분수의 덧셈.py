def yak(num1, num2) :
    answer=[]
    min = num1 if num1<num2 else num2
    for i in range(1, min+1):
        if num1%i==0 and num2%i==0 :
            answer.append(i)
    return max(answer)
def solution(numer1, denom1, numer2, denom2):
    d= yak(denom1, denom2)
    denom3 = denom1*denom2//d
    numer3 = (denom3//denom1)*numer1 + denom3//denom2*numer2
    y = yak(denom3, numer3)
    return [numer3//y, denom3//y]