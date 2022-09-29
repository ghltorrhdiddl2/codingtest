#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#3, 29, 38, 12, 57, 74, 40, 85, 61이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#입력:첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
import sys

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

maxN = 0; idx = 0
for i, j in enumerate(arr):
    if maxN < j:
        maxN = j
        idx = i+1
print(maxN)
print(idx)


#---------다른 사람 풀이--------------------
num_list = []
for i in range(9):
    num_list.append(int(input()))  			# num_lst 안에 입력된 값들 차례대로 넣기

print(max(num_list))						# max()사용
print(num_list.index(max(num_list))+1)      # index()사용