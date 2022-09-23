def solution(x):
    nums = [int(x) for x in str(x)]
    return x % sum(nums) == 0

x = 120
x2 = 130

print(solution(x))
#x를 str로 for문 돌려 int형으로 list저장 후, sum()으로 합 구해 조건식

#---------다른 사람 풀이---------------------------
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

print(Harshad(18))