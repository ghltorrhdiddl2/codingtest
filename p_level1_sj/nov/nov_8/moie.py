#---------------------------런타임 에러--------------------------
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    result = []; scoreA = 0; scoreB = 0; scoreC = 0;
    for i, v in enumerate(answers):
        if v == a[i]:
            scoreA += 1
        if v == b[i]:
            scoreB += 1
        if v == c[i]:
            scoreC += 1
    maxS = max(scoreA,scoreB,scoreC)
    if scoreA == maxS:
        result.append(1)
    if scoreB == maxS:
        result.append(2)
    if scoreC == maxS:
        result.append(3)
    return result

# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))


#-------------------다른 사람 풀이-------------------
def solutionn(answers):
    s1 = [1, 2, 3, 4, 5]  # 5개
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개
    score = [0, 0, 0]
    winner = []

    for i, v in enumerate(answers):
        if v == s1[(i % len(s1))]:   # 반복주기 5
            score[0] += 1
        if v == s2[(i % len(s2))]:
            score[1] += 1
        if v == s3[(i % len(s3))]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            winner.append(idx + 1)

    return winner

print(solutionn([1,2,3,4,5]))
print(solutionn([1,3,2,4,2]))