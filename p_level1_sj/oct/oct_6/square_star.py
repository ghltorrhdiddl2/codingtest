a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*'*a)


#--------------------다른 사람 풀이---------------------
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b    #for문 없이 \n으로 개행
print(answer)

