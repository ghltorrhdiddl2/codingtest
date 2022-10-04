#두 정수 사이의 합
def solution(a, b):
    arr = []
    if a < b:
        for i in range(a, b+1):
            arr.append(i)
    elif a > b:
        for i in range(b, a+1):
            arr.append(i)
    else:
        return a
    return sum(arr)


print(solution(3, 5))  #12
print(solution(3, 3))  #3
print(solution(5, 3))  #12


#---------다른 사람 풀이-------------
def adder(a, b):
    if a > b: a, b = b, a    #a>b이면 a와 b의 값을 서로 바꿈
    return sum(range(a,b+1))

print(adder(3, 5))
print(adder(3, 3))
print(adder(5, 3))


#수학공식
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

print(adder(3, 5))


#min, max 이용
def adder(a, b):
    return sum(range(min(a,b),max(a,b)+1))

print(adder(3, 5))
