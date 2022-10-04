#길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
def solution(n):
    st = '수박' * n
    return st[:n]

print(solution(3))


#--------다른 사람 풀이-----------
#시간 복잡도 줄인 버젼
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

print("n이 5인 경우: " + water_melon(5))
print("n이 6인 경우: " + water_melon(6))

#수학적으로 좀 더 생각해보기(짝홀의 경우, 몫(//)과 나머지(%) 중요!)
