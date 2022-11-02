# 동명이인 경우
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(answer)
    return list(answer.keys())[0]

print(solution(["mislav","stanko","mislav","ana"], ["stanko","ana","mislav"]))

# Counter class는 상호간의 뺄셈 연산을 지원한다
# 참고: https://coding-grandpa.tistory.com/85