def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        phone = phone_book[i+1]
        if phone.startswith(phone_book[i]):
            return False
    return True