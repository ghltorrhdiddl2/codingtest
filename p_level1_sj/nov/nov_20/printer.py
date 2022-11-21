def solution(priorities, location):
    pri = [(i,v) for i, v in enumerate(priorities)]

    answer = 0
    while pri:
        a = pri.pop(0)
        if any(a[1] < other[1] for other in pri):
            pri.append(a)
        else:
            answer += 1
            if a[0] == location:
                break

    return answer

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))
