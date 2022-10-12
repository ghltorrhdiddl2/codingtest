#각 단어의 짝수번째 알파벳은 대문자로,
#홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수

#------------------다른 사람 풀이-----------------------
def solution(s):
    answer = []
    words = s.split()   #공백을 없애면 안되므로

    for word in words:
        w = ""
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)
        # print(answer)
    return ' '.join(answer)   #공백 넣기

print(solution("try hello world"))