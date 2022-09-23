def solution(x, n):
    answer = []
    a= 0
    for i in range(n):
        if n == 0:
            a = x
            answer.append(a)
            continue
        a += x
        answer.append(a)
    return answer

print(solution(2, 4))


#---------다른 사람 풀이----------------
def number_generator(x, n):
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

#lsit안에 for문을 사용


#<<수열 공식>> an=3n 응용하는 방법
def number(x, n):
    return [i * x for i in range(1, n+1)]
print(number(3, 5))
