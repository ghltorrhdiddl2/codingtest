N = int(input())
nums = list(input())  #입력: 1234, 출력:['1','2','3','4'] 형태 int()해도 결과 같음
sumN = 0
for i in nums:
    sumN += int(i)  #int로 변환해 더해준다
print(sumN)


#-------------다른 사람 풀이-------------
input();print(sum(map(int, input())))