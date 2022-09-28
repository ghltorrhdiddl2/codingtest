#별찍기
N = int(input())

for i in range(1,N+1):
    for j in range(1,i+1):
        print('*', end='')
    print()


#------------다른 사람 풀이----------------
for i in range(1,int(input())+1):
    print('*'*i)