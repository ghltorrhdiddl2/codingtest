#-----정확성 37.5--------------------------------------------
def solution(arr, divisor):
    arr.sort()
    div = []
    for i in arr:
        if i % divisor == 0:
            div.append(i)

        else:
            if len(div) == 0:
                return [-1]

            # if not div:
            #     div = [-1]
            #----> div값이 없을 때 [-1]출력이므로 len()으로 div길이 구하는 것보다
            #if not div로 div가 Faluse면으로 조건을 걸어준다

    return div

print(solution([5, 9, 7, 10], 5))
print(solution([3,2,6], 10))


#-----------다른 사람 풀이------------------------------
def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return answer if len(answer) != 0 else [-1]   #삼항연산자 사용

#삼항연산자 사용 가능하다면 사용하자


#앞의 것이 참이면 or 앞까지만 출력, 거짓이면 or 뒤까지 출력
def solution(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]
print(solution([5, 9, 7, 10], 5))
print(solution([3,2,6], 10))


#list안데 for문 써서 바로 대입작성, return값 삼항연산자 사용
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]
