def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i+1 > c:
            return i
    return len(citations)

print(solution([3, 0, 6, 1, 5]))   # 3
print(solution([6, 5, 5, 5, 3, 2, 1, 0]))  # 4
print(solution([4, 4, 4]))  # 3


#-----------------다른 사람이 푼 코드--------------------------
def ssolution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(ssolution([3, 0, 6, 1, 5]))   # 3
print(ssolution([6, 5, 5, 5, 3, 2, 1, 0]))  # 4
print(ssolution([4, 4, 4]))  # 3