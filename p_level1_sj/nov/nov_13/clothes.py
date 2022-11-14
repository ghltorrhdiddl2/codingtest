def solution(n, lost, reserve):
    lost_del=set(lost)-set(reserve)
    reserve_del=set(reserve)-set(lost)

    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)

    return n-len(lost_del)

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))