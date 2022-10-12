#연속 같은 값 제거, 순서유지
def solution(arr):
    arr2 = []
    arr2.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            arr2.append(arr[i])
    return arr2

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))