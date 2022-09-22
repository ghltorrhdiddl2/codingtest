def solution(seoul):
    answer = ''
    for idx, k in enumerate(seoul):
        if k == 'Kim':
            answer = (f'김서방은 {idx}에 있다')
    return answer
print(solution(['jane','Kim']))