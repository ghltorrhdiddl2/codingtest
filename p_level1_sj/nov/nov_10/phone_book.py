# 정확도 66.7%
def solution(phone_book):
    flag = True

    for i in range(len(phone_book)-1):
        for j in range(1,len(phone_book)):
            if phone_book[i] != phone_book[j]:
                if phone_book[i] in phone_book[j]:
                    flag = False
                elif phone_book[j] in phone_book[i]:
                    flag = False
    return flag

print(solution(["97674223", "1195524421","119"]))
print(solution(["123","456","789"]))
print(solution(["123","1235","567", "12","88"]))