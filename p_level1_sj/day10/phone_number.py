#핸드폰 번호 가리기
def solution(phone_number):
    #4자리수 제외한 문자열 뽑아내기
    phone = phone_number[:-4]

    #뽑아낸 문자열을 '*'로 그 길이만큼 변환
    rePhone = phone_number.replace(phone, '*'*len(phone))
    return rePhone

print(solution("01033334444"))
print(solution("027778888"))


#-------------------------다른 사람 풀이-------------------------
def hide_numbers(s):
    #길이에서 -4만큼 '*'출력 + 뒤 4자리수 덧붙이기
    return "*"*(len(s)-4) + s[-4:]

print("결과 : " + hide_numbers('01033334444'))