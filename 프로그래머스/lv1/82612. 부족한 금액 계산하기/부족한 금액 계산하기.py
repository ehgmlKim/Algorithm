def solution(price, money, count):
    need = sum([price*i for i in range(1, count+1)])
    return 0 if need<money else need-money