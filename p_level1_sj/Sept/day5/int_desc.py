def solution(n):
    arr = [int(n) for n in str(n)]
    arr.sort()
    result = 0
    for dix, i in enumerate(arr):
        result += (10**dix)*i
    return result

n = 118372

# print(solution(n))


#-------------------------------------------
def ssolution(n):
    ls = list(str(n))  ##str을 list로 형변환하면 문자열의 문자들이 분리되어 리스트에 추가된다!!
    ls.sort(reverse = True)
    return int("".join(ls))

n = 118372

print(ssolution(n))
