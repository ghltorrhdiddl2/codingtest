def solution(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
    return sum

n = 12


#------------다른사람 풀이 ---------
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

print(sumDivisor(12))

#한 줄로 풀어 바로 return시켰다!