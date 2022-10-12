#숫자 뒤집어 크기 비교
a, b = map(int, input().split())

a = int(str(a)[::-1])
b = int(str(b)[::-1])

print(a if a > b else b)


#------------다른 사람 코딩----------------
print(max(input()[::-1].split()))