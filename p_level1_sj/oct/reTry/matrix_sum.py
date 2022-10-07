# def solution(arr1, arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr1[i])):
#             arr1[i][j] += arr2[i][j]
#     return arr1

def solution(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        tmp = []
        print(arr1[i])
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        arr.append(tmp)
    return arr

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
# print(solution([[1],[2]], [[3],[4]]))