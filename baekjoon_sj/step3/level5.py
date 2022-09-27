#여러 줄을 입력받거나 출력할땨 input()함수를 쓰면 시간초과가 발생할 수 있다.
#따라서 input() 대신 sys.stdin.readline()을 사용하자!

import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)