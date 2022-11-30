# 제한사항 확인! : numbers의 원소는 0 이상 1,000 이하입니다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# print(solution([6, 10, 2]))   # 6210
print(solution([3, 30, 34, 5, 9]))  # 9 5 34 3 30
# print(solution([323, 300, 34, 5, 9]))  # 9 5 34 323 300