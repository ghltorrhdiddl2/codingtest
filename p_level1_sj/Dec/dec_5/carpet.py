def solution(brown, yellow):
    tiles = brown+yellow
    w = 0; h = 0; a = []
    for i in range(1,tiles):
        if tiles % i == 0:
            a.append(i)
    if len(a) % 2 != 0:
        idx = len(a)//2+1
        w = a[idx]
        h = tiles//w
    else:
        idx = len(a)//2
        w = a[idx]
        h = tiles//w

    return [w,h]

print(solution(10, 2))    # [4,3]
print(solution(8, 1))     # [3,3]
print(solution(24, 24))   # [8,6]

# 가로 >= 세로 길이
