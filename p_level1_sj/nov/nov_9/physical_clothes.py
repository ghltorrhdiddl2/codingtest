# 그리디 체육복
# 정확도 75%
def solution(n, lost, reserve):
    cnt = 0
    for i in range(len(lost)):
        # print(lost[i])
        # 자기 체육복 도난 학생
        if lost[i] in reserve:
            reserve.remove(lost[i])
            cnt += 1

        if lost[i]-1 in reserve or lost[i]+1 in reserve:
            if lost[i]-1 in reserve:
                reserve.remove(lost[i]-1)
            else:
                if lost[i]+1 in reserve:
                    reserve.remove(lost[i]+1)
            cnt +=1

    return n-(len(lost)-cnt)

# print(solution(5, [2,4], [1,3,5]))
# print(solution(5, [2,4], [3]))
# print(solution(3, [3], [1]))


#--------------------다른 사람 풀이-------------------
# set() 공콩요소 제거 사용, 집합
def ssolution(n, lost, reserve):
  # 자기 체육복 도난 학생 제거
    lost_del = set(lost) - set(reserve)
    reserve_del = set(reserve) - set(lost)

    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
    return n-len(lost_del)

print(ssolution(5, [2,4], [1,3,5]))
print(ssolution(5, [2,4], [3]))
print(ssolution(3, [3], [1]))