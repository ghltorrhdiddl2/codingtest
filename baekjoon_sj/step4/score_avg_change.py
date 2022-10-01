#세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
#예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

N = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)
for i, s in enumerate(scores):
    scores[i] = s/maxScore*100
print(sum(scores)/N)


#-------------------다른 사람 풀이--------------------
N=int(input())
l=[*map(int, input().split())]
print(sum(l)/max(l)*100/N)

#여러 개 입력받을 때 *(변수) 형식으로 써 준다!
#전체의 평균을 구하는 것이므로 값 하나하나 구하지 않고 합에서 바로 식 적용해도 결과는 같다