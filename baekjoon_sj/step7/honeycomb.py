#벌집
n = int(input())
cnt = 1; an = 1
while True:
    bn = 6*(cnt-1)
    an += bn

    if n <= an:
        print(cnt)
        break
    cnt += 1