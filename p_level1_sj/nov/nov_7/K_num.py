def solution(array, commands):
    arr = []
    for i in range(len(commands)):
        answer = array[commands[i][0]-1:commands[i][1]]
        answer.sort()
        arr.append(answer[commands[i][2]-1])
    return arr

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


#------------------------다른 사람 풀이-----------------------
def ssolution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        # print(i,j,k)   # 2 5 3
        answer.append((sorted(array[i-1:j]))[k-1])
    return answer
print(ssolution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#----------------------------------------------------------
def solutionn(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solutionn([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))