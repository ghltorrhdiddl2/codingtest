# 시저 암호
#-----------------다른 사람 풀이---------------
def solution(s, n):
    low = "abcdefghtjilmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            idx = low.find(char) + n
            answer += low[idx % 26]
        elif char in up:
            idx = up.find(char) + n
            answer += up[idx % 26]
        else:
            answer += " "   #공백인 경우

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

#------------------아스키 코드 사용-------------------
def ceasar(s, n):
    s = list(s)    # ['a', ' ', 'B', ' ', 'z']

    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26 + ord('A'))   # Z -> A로 넘어가기 위해 %26
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26 +ord('a'))
    return ''.join(s)     # list -> str 변환

print(ceasar("AB", 1))
print(ceasar("z", 1))
print(ceasar("a B z", 4))


# 복습 필요!!