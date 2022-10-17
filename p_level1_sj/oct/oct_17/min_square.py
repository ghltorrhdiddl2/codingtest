# 모든 명함을 수납할 수 있는 가장 작은 지갑 크기
# 명함 눕힐 수 있음
def solution(sizes):
    max1=[]; max2=[]
    for i in range(0, len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        max1.append(sizes[i][0])
        max2.append(sizes[i][1])

    return max(max1)*max(max2)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))   #4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  #120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  #133


#----------------------다른 사람 풀이-------------------------
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:      # a = sizes[idx][0], b = sizes[idx][1]
        print(a, b)   # 60 50
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))   #4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  #120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  #133

# for a, b in sizes:  -> 이 방법도 있다!!   [1,2], [3,4]