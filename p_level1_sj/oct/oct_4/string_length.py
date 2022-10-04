#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
# s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴

def solution(s):
    n = 0
    if len(s) == 4 or len(s) == 6:
        for i in s:
            num = i.isdigit()
            if num == False:
                n += 1
        if n == 0:
            return True
        else: return False
    else:
        return False

print(solution("2A34"))
print(solution("1234"))


#--------------다른 사람 풀이---------------
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

#s.isdigit()로 1차 T,F 나누고 and 조건으로 1차T & 2차T만 T로 출력됨
#len(s)가 4이거나 6
print( alpha_string46("a234") )
print( alpha_string46("1234") )


#-------------------------------------------
def alpha_string46(s):
    try:
        int(s)
    except:
        return False   #int(s)가 요류일 경우, 즉 s가 str일 경우
    return len(s) == 4 or len(s) == 6  #이면 True

print(alpha_string46("a234") )
print(alpha_string46("1234") )


