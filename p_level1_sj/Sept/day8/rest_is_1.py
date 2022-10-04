#나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

print(solution(12))
#range에서 나머지가 나오려면 1과 자기자신은 for문 돌릴 필요가 없어 2부터 n-1까지로 잡았음

#------------다른 사람 풀이----------------------------
def solutionn(n):
    return [x for x in range(1,n+1) if n%x==1][0]
print(solutionn(12))
#list에서 [0]인덱스의 x꺼냄(x의 첫 번째 값)// [0]으로 값을 꺼내지 않으면 [11]로 []붙여진 list형태로 출력됨
#for문 if문 연달아 사용이 가능하다

