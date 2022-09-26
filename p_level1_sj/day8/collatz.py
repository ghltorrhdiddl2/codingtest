#콜라츠 추측
def solution(num):
    cnt = 0
    if num == 1:
        return 0

    while num != 1:
        if cnt == 500:
            return -1

        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        cnt += 1

    return cnt

print(solution(626331))

#num=1 일때와 반복횟수가 500회 이상이면 -1리턴을 return으로 더 이상의 연산 없이 바로 값 출력(효율성)
