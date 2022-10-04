#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
def solution(s):
    return s[int(len(s)//2)] if len(s) % 2 != 0 else s[int(len(s)//2-1):int(len(s)//2+1)]

print(solution("abcde"))
print(solution("qwer"))


#--------다른 사람 풀이-----------------------
def string_middle(str):
     return str[(len(str)-1)//2:len(str)//2+1]

print(string_middle("power"))
print(solution("qwer"))
#짝수, 홀수 구분없이 [:]에서 몫을 구해 슬라이싱했다.
#슬라이싱 할 때 인덱스의 어디에서부터 어디까지 필요한지 생각해보기
