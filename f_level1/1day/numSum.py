def solution(n):
    arr = []
    answer = 0
    for i in str(n):
        arr.append(i)
    for j in arr:
        answer += int(j)

    return answer

n = 123
print(solution(n))


######sum으로 합산, 바로 뒤에 for문 배치
def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))

#####재귀함수 사용
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)

print("결과 : {}".format(sum_digit(123)));