# 정확도 83.3%
def solution(phone_book):
    flag = True

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] != phone_book[j]:
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    flag = False
                elif phone_book[j] == phone_book[i][:len(phone_book[j])]:
                    flag = False
    return flag

print(solution(["97674223", "1195524421","119"]))
print(solution(["123","456","789"]))
print(solution(["123","1235","567", "12","88"]))


#--방법1---------------다른 사람 풀이-------------------
# 시간초과 -> 이중for문 -> 양방향 비교
def solution(phone_book):
    # 비교할 A 선택
    for i in range(len(phone_book)):
        # 비교할 B 선택
        for j in range(i+1, len(phone_book)):
            # 서로가 서로의 접두어인지 확인
            if phone_book[i].startswith(phone_book[j]):
                return False
            elif phone_book[j].startswith(phone_book[i]):
                return False
    return True

print(solution(["97674223", "1195524421","119"]))
print(solution(["123","456","789"]))
print(solution(["123","1235","567", "12","88"]))


#--방법2---------------------------------------------------------
# sort()해서 단방향 검사로 for문 하나 줄이기    sorting 한 결과가 가장 효율이 좋다!
def ssolution(phone_book):
    phone_book.sort()    # ['12', '123', '1235', '567', '88']
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

print(ssolution(["123","1235","567", "12","88"]))


#--방법3----------------------------------------------------
# zip() 사용  sorting 한 결과가 가장 효율이 좋다!
def solutionn(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solutionn(["97674223", "1195524421","119"]))
print(solutionn(["123","456","789"]))
print(solutionn(["123","1235","567", "12","88"]))
# zip --> [('123', '1235'), ('1235', '567'), ('567', '12'), ('12', '88')]


#--방법4-------------------------------------------------
# Hash Map
def solution4(phone_book):
    # 1. Hash Map을 만든다
    hash_map={}
    for number in phone_book:
        hash_map[number]=1
    print(hash_map)
    # 2. 접두어가 Hash Map에 존재하는지 찾는다
    for num in phone_book:
        jubdoo=''
        for n in num:
            jubdoo += n
            # 3. 접두어를 찾는다 (기존번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != num:
                return False
    return True

print(solution4(["97674223", "1195524421","119"]))
print(solution4(["123","456","789"]))
print(solution4(["123","1235","567", "12","88"]))