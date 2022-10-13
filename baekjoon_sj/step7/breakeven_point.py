#손익분기점
#---------------시간 초과-------------------
a, b, c = map(int, input().split())
n = 1

while True:
    if (a+b*n) < c*n:
        print(n)
        break
    else:
        if b > c:
            print(-1)
            break
    n += 1


#----------------다른 사람 풀이------------------
#수학식 사용!!
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))   # A + B*N < C*N : 손익분기점
    #+1을 해줘야 수입=비용에서 수입>비용 이 된다

# N을 출력해야 하므로,  A = C*N - B*N  ->  A = N*(C - B)
# ->  N = A/(C - B)     N은 정수여야 하므로 int()씌워준다


#---------------------------------------------
a, b, c = map(int,input().split())
print(-1 if b >= c else a//(c-b)+1)