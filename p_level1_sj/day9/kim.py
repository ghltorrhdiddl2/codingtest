def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return '김서방은 '+str(i)+'에 있다'

print(solution(["Jane", "Kim"]))


#------------다른 사람 풀이--------------
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(findKim(["Queen", "Tod", "Kim"]))

#seoul.index()로 'Kim'의 index값을 찾아 return 반환