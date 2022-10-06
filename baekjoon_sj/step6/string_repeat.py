#원래 코딩
t = int(input())
for i in range(t):
    r, s = map(str, input().strip().split())

    for j in s:
        print(j*int(r), end='')

#--->>입력과 출력 형식 맞추려면 프린트를 j 반복문에서 꺼내야 했다.
#고친 코딩
t = int(input())
for i in range(t):
    r, s = input().split()
    text = ''
    for j in s:
        text += int(r)*j
    print(text)

