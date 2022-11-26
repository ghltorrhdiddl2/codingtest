# 정수를 이어 붙여 만들 수 있는 가장 큰 수
# numbers 원소는 최대 세 자릿 수
# 정확도 53.3%
def solution(numbers):
    answer = []; result = []
    for i, v in enumerate(numbers):
        if v < 10:  # 한 자릿수 경우
            answer.append((i, v, v, v))
        elif v < 100:   # 두 자릿수 경우
            answer.append((i, v//10, v%10, v%10))
        else:  # 세 자릿수 경우
            answer.append((i, v//100, (v-v//100*100)//10, v%10))

    answer.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    for i, v, v2, v3 in answer:
        result.append(numbers[i])
    result2 = ''.join(map(str, result))
    return ''.join(map(str, result))

# 앞자리 볼 필요 있음
# print(solution([6, 10, 2]))   # 6210
# print(solution([3, 30, 34, 5, 9]))  # 9 5 34 3 30
# print(solution([323, 300, 34, 5, 9]))  # 9 5 34 323 300


#---------------------------다른 사람 풀이----------------------------
def ssolution(numbers):
    numbers = list(map(str, numbers))    # -> 문자열로 만들어서 비교연산 -> 아스키 코드값 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(ssolution([6, 10, 2]))   # 6210
print(ssolution([3, 30, 34, 5, 9]))  # 9 5 34 3 30
print(ssolution([323, 300, 34, 5, 9]))  # 9 5 34 323 300