x = 18
strN = str(x)

def solution(x):
    answer = True
    strN = str(x)
    result = 0               #길이만큼 -> 0,1 돌고
    for i in range(len(strN)):
        result += int(strN[i]) #->int 변환
        #1+8 => 9
    # 18 % 9 -->
    if x % result == 0:
        answer = True
    else:
        answer = False


    return answer

print(solution(14))