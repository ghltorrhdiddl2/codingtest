def solution(priorities, location):
    time = 0; pri = []
    pri = [(i, v) for i, v in enumerate(priorities)]


    while pri:
        a = pri.pop(0)
        if any(a[1] < other[1] for other in pri):
            pri.append(a)
        else:
            time += 1
            if a[0] == location:
                break
    return time

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))