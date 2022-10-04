def solution(n):
    nList = list(map(int, str(n)))
    nList.reverse()
    return nList

n = 12345
print(solution(n))


#---------------------------------------------
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
