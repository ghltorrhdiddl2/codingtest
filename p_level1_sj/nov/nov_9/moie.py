def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]; result = []

    for i, v in enumerate(answers):
        if v == s1[i%len(s1)]:
            score[0] += 1
        if v == s2[i%len(s2)]:
            score[1] += 1
        if v == s3[i%len(s3)]:
            score[2] += 1

    for j, v in enumerate(score):
        if v == max(score):
            result.append(j+1)
    return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))