#음양 더하기
def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
            continue
    return sum(absolutes)

absolutes = [1,2,3]
signs = [False,False,True]
print(solution(absolutes, signs))


#-------------------다른 사람 풀이--------------------
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

absolutes = [4,7,12]
signs = [True,False,True]
print(solution(absolutes, signs))
#zip()함수는 두 개 이상의 변수를 병렬처리하여 반복자로 반환
#zip(A,B)이고 A=[1,2,3], B=['가','나','다']면
#튜플형으로 (1,'가'),(2,'나'),(3,'다') 반환
