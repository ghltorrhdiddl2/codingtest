# 정확성 69.2%
def solution(brown, yellow):
    tiles = brown + yellow
    w = 0;
    h = 0;
    a = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            a.append(i)
    if len(a) % 2 != 0:
        idx = len(a) // 2
        w = a[idx]+2
        h = tiles // w
    else:
        idx = len(a) // 2
        w = a[idx-1]+2
        h = tiles // w
    return [h,w]

print(solution(10, 2))    # [4,3]
print(solution(8, 1))     # [3,3]
# print(solution(24, 24))   # [8,6]
print(solution(14, 6))   # [5,4]


#----------------다른 사람 풀이----------------------
def ssolution(brown, yellow):
    answer = []
    yellow_x = 0; yellow_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                return sorted(answer, reverse=True)

    return answer


print(ssolution(10, 2))    # [4,3]
print(ssolution(8, 1))     # [3,3]
# print(ssolution(24, 24))   # [8,6]
print(ssolution(14, 6))   # [5,4]

# 거의 근접했었다.
# 다름 풀이 때 좀 더 생각해 보기
