# 소수 찾기
from itertools import permutations
def solution(numbers):
    per = []
    for i in range(1,len(numbers)+1):
        per.append(list(permutations(numbers, i)))
    perNum = []
    for i in range(len(per)):
        for j in per[i]:
            perNum.append(int(''.join(j)))

    def isPrimeNumber(number):
        if number <= 1:
            return False
        else:
            for i in range(2, number // 2 + 1):
                if number % i == 0:
                    return False
            return True

    sosu = 0
    for p in list(set(perNum)):
        if isPrimeNumber(p):
            # print(p)
            sosu += 1
    return sosu

print(solution('17'))   # 3    7,17,71
print(solution('011'))  # 2    11,101
# print(solution('1234'))
# 3개중 하나 뽑, 3개중 두개 뽑, 3개 모두 뽑
# 순열

