import sys

N = int(input())  #딱히 없어도 됨
n = list(map(int, sys.stdin.readline().split()))
print(min(n), max(n))


#-----다른 사람 풀이-------------------------------
#여러개 입력받을 때 *m,
input()
*m, = map(int, input().split())
print(min(m), max(m))
