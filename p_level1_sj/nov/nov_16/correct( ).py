# 정확도 54.1
def solution(s):
    if s.startswith(')'):
        return False
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt != 0:
        return False
    return True

# print(solution("()()"))
# print(solution("(())()"))
# print(solution(")()("))
# print(solution("(()("))


#-----------스택 활용----------------------------------------
def ssolution(s):
    answer=True
    arr = []
    for i in s:
        if i == '(':
            arr.append('(')
        else:
            if arr == []:
                return False
            else:
                arr.pop()
    if arr != []:
        answer=False

    return answer

print(ssolution("()()"))
print(ssolution("(())()"))
print(ssolution(")()("))
print(ssolution("(()("))


#--------다른 사람 풀이--------------------------------
def is_pair(s):
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        elif c == ')':
            open_cnt -= 1
            if open_cnt < 0:  # ')'로 시작하는 경우를 for-if문 안에 넣었다
                return False
    return open_cnt == 0