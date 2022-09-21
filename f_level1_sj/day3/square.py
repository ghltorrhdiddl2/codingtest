def solution(n):
    answer = n ** (1 / 2)
    if answer - int(answer) == 0:
        return (answer+1)**2
    else:
        return -1

print(solution(144))


#-----------------------------------------
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1
print(nextSqure(144))