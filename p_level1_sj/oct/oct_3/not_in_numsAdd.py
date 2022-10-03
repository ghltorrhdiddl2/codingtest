def solution(numbers):
    sumN = 0
    for i in range(1,10):
        if i not in numbers:
            sumN += i
    return sumN

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))


#------------다른 사람 풀이----------------
def solution(numbers):
    return 45 - sum(numbers)

#1~9까지 더한 합인 45에 list에 들어있는 값들의 합을 빼주면
#list에 없는 값들의 합이 남는다