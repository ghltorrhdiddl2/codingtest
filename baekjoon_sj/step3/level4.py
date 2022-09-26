#영수증
X = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a * b

print('Yes' if total == X else 'No')   #print문 안에 if삼항연산자 가능!