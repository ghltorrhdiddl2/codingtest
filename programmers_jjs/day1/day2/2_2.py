a = -2
n = 5
answer = []

for i in range(1, n+1, 1):

    answer.append(a*i)

print(answer)

def solution(x, n):
    answer = []
    for i in range(1, n+1, 1):
        answer.append(x*i)
    return answer