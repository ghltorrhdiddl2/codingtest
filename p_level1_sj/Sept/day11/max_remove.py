#제일 작은 수 제거하기
def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]

print(solution([4,3,2,1]))
print(solution([10]))
