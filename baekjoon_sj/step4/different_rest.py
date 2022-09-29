#첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
#첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

arr = []
for i in range(10):
    arr.append(int(input()))

rest = []
for j in arr:
    restN = j % 42

    if restN not in rest:
        rest.append(restN)
print(len(rest))


#------------다른 사람 풀이-------------------------
print(len(set({int(input()) % 42 for i in range(10)})))    # (안에 {사용})   {}없어도 코드 돌아감