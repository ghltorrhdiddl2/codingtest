# 행렬 덧셈
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수
def solution(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        arr.append(tmp)
    return arr
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))


#------------다른 사람 풀이----------------
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A


import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist() #.tolist()로 matrix형태 리스트로 변환시켜준다
