#예산 최대한 많은 부서의 물품을 구매해 줄 수 있도록
def solution(d, budget):
    d.sort()
    cnt = 0

    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1

    return cnt

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))


#--------------다른 사람 풀이---------------
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# budget가 sum(d) 보다 클 때 까지 d를 pop()시킨다
# 그 후 남은 길이로 최대지원 부서 계산