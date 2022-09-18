def solution(history, infected):
    start = history.index(infected)
    stop = history.index(-infected)
    overlap = history[start+1:stop]

    for i in range(len(overlap)):
        overlap[i] = abs(overlap[i])

    print(sorted(set(overlap)))

histroy = [3,2,-3,1,-1,-2,4,-4,1,-1]
infected = 2

if sum(histroy) == 0:
    solution(histroy, infected)
else:
    print('아직 건물 안에 사람이 남아있습니다.')