# A, B = map(int, input().split())
# if A>B:
#     print('>')
# elif A<B:
#     print('<')
# else:
#     print('==')


#삼항연산자로 풀이
A, B = map(int, input().split())
print('>') if A>B else (print('<') if A<B else print('=='))


#리스트와 T,F
a,b=map(int,input().split())
print(['><'[a<b],'=='][a==b])

#a==b가 T면 1, F면 0
#1이면 '==' 출력, 0이면 '><'로 넘어간다
#a<b가 T면 1, F면 0
#1이면 '<'출력, 0이면 '>'출력

#어려우니까 그냥 삼항 연산자 쓰자
