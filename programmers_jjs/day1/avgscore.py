def solution(arr):
    answer = 0

    for i in arr:
        answer += i

    return answer / len(arr)


a = [1, 2, 3, 4]
n = solution(a)
print(n)
