#"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
n = int(input())

for i in range(n):
    oxList = list(input())
    score = 0
    sumScore = 0 #새로운 ox리스트를 받으면 점수 합계 리셋

    for ox in oxList:
        if ox == 'O':
            score += 1 #'O'가 연속되면 점수가 1씩 커진다
            sumScore += score
        else:
            score = 0
    print(sumScore)

