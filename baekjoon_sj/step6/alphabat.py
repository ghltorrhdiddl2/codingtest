#각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를
#공백으로 구분해서 출력
#만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력

word = input()
alpha = list(range(97,123))  #아스키코드 숫자 범위(a~z)
for i in alpha:
    print(word.find(chr(i)), end=' ')

#find()함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력
#find()함수는 만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력
#find()함수는 문자열에서만 사용 가능한 함수
#char() 숫자(아스키코드)->문자; ord() 문자->숫자(아스키코드)


#--------------------다른 사람 풀이-------------------
print(*map(input().find,map(chr,range(97,123))))

print(*map(input().find,'abcdefghijklmnopqrstuvwxyz'))