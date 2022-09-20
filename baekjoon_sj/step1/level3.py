#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#첫째 줄에 A+B를 출력한다.

A, B = input().split()   # 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장
# print(type(A)) #str 타입
print(int(A)+int(B))     #int() 함수로 A와 B를 정수로 변환 하고 두수의 합을 출력

A, B = map(int, input().split())
print(A+B)

#split()함수는 입력받은 '문자(str)'을 나눌 때 쓰는 함수(문자열 쪼개기)
# ()안 조건 없으면 공백을 기준으로 나눔
#따라서 int()로 숫자 변환시켜줘야 한다

#---------map(적용시킬함수, 적용할 값)활용-------------
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)

print(f'result1 : {result1}')


# map 함수 이용
def add_one(n):
    return n + 1

result2 = list(map(add_one, myList))  # map반환을 list 로 변환
print(f'result2 : {result2}')

#출처: https://blockdmask.tistory.com/531 [개발자 지망생:티스토리]
