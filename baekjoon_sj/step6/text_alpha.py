#시간초과, 결과는 맞게 나옴
s = input().upper()
arr={}; maxN = 0
for i, a in enumerate(s):
    cnt = 0
    for j in s:
        if a == j:
            cnt += 1
            arr[a] = cnt
    if maxN < arr[a]:
        maxN = arr[a]
print(arr)
alpha = []
for k, v in arr.items():
    if v == maxN:
        alpha.append(k)

print("?") if len(alpha) > 1 else print(alpha[0])


#---------------다른 사람 풀이-----------------
s = input().upper()
c = [s.count(chr(i)) for i in range(65, 91)]  #아스키코드로 A~Z 최빈값구하기알고리즘
# print(c)
m = max(c)
# print(m)
if c.count(m) == 1:
    # print(c.index(m))
    print(chr(c.index(m)+65))
else:
    print('?')


# 다시 풀어보기!!!

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
#위 코드 출처: https://ooyoung.tistory.com/70