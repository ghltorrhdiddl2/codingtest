a = 5
b = 3
result = 0
j = min(a,b)
k = max(a,b)

for i in range(j, k+1, 1):

    result += i
print(result)

def solution(a, b):
    answer = 0
    max1 = max(a,b)
    min2 = min(a,b)

    for i in range(min2, max1+1, 1):
        answer += i



    return answer

print(solution(3,5))