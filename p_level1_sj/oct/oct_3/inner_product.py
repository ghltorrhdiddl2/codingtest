#내적
#a와 b의 내적은 1*(-3) + 2*(-1) + 3*0 + 4*2 = 3 입니다.

def solution(a, b):
    sumN = 0
    for idx, n in enumerate(a):
        sumN += n*b[idx]
    return sumN


# print(solution([1,2,3,4], [-3,-1,0,2]))
# print(solution([-1,0,1], [1,0,-1]))


#-----------다른 사람 풓이-------------
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])

#for문 돌려서 sum알아내기보다 sum()함수 써서 sum값 알아내기
#lsit에서 for문 안에 사용가능하다
#zip()함수: 길이가 같은 리스트 등의 요소들을 묶어주는 함수
arr= []
a=[1,2,3,4]; b=[2,2,2,2]
for x,y in zip(a,b):
    arr.append(x*y)
print(arr)              #[2, 4, 6, 8]
print(list(zip(a,b)))   #[(1, 2), (2, 2), (3, 2), (4, 2)]