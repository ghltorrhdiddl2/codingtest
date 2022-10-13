#10진법 -> 삼진법 뒤집기 -> 10진법 변환

def solution(n):
    three = ''; ten = 0
    while n > 0:
        n, mod = divmod(n, 3)
        three += str(mod)

    ten = int(three, 3)  #3진법 -> 10진법 변환
    # for i in range(0, len(three)):
    #     ten += int(three[i]) * 3**(len(three)-1-i)

    return ten

print(solution(45))
print(solution(125))


#--------------------다른 사람 풀이----------------------
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

print(solution(45))
print(solution(125))
# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
