def solution(n, m):
    arr = []
    if n < m:
        for i in range(m-1, 1, -1):
            if m % i == 0 and n % i == 0:
                arr.append(i)
                arr.append(m*n//i)
                return arr
        if len(arr) == 0:
            arr.append(1)
            arr.append(m*n//1)
            return arr
    else:
        for i in range(n-1, 1, -1):
            if m % i == 0 and n % i == 0:
                arr.append(i)
                arr.append(m*n//i)
                return arr
        if len(arr) == 0:
            arr.append(1)
            arr.append(m*n//1)
            return arr

print(solution(12, 3))
print(solution(2, 5))


#-------------------다시 푼 코드--------------------
def solution(n, m):
    arr = []
    a, b = max(n, m), min((n, m))

    for i in range(a - 1, 1, -1):
        if a % i == 0 and b % i == 0:
            arr.append(i)
            arr.append(a * b // i)
            return arr
    if len(arr) == 0:
        arr.append(1)
        arr.append(a * b // 1)
        return arr

print(solution(12, 16))
print(solution(2, 5))


#--------------------------다른 사람 풀이--------------------------
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    # c: 12, d: 3, t: 1
    while t > 0:
        t = c % d       #c: 12, d: 3, t: 0
        c, d = d, t     #c: 3, d: 0, t: 0
    answer = [c, int(a*b/c)]

    return answer

print(gcdlcm(3,12))
#유클리드 호제법
#대소비교할 때, a>b경우 구분하기보다는
#c, d = max(a, b), min(a, b)로 사용해서 if-else문 없애보자