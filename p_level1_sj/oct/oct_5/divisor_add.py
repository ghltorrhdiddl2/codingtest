# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
#약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
def solution(left, right):
    result = 0
    for i in range(left, right+1):
        divi = []   #각 약수 담을 리스트
        for j in range(1, i+1):
            if i % j == 0:
                divi.append(j)
        if len(divi) % 2 == 0:
            result += j
        else:
            result -= j
    return result

print(solution(13,17))
print(solution(24,27))


#---------------다른 사람 풀이-------------------
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        #제곱수의 약수는 홀수 개! 그외는 짝수 개
        #루트 씌워서 그 수가 정수면 제곱수
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
