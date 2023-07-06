def solution(phone_book):
    answer = True
    phone_book.sort()
    l = len(phone_book)
    for i in range(l-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer