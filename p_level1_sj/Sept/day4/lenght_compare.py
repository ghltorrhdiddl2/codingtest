def solution(s):
    s = s.lower()

    pCont = s.count('p')
    yCont = s.count('y')

    if pCont == yCont:
        return True
    else:
        return False

s = 'pPoooyY'
s2 = 'Pyy'

print(solution(s))


#---------------------------
##Tru, False 직접 쓰지 않고 == 로 Boolean 출력
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

print( numPY("pPoooyY") )
print( numPY("Pyy") )
