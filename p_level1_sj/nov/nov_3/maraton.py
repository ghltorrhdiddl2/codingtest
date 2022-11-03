# 해시
import collections
def solution(participant, completion):
    par = collections.Counter(participant)
    com = collections.Counter(completion)
    answer = par-com
    return list(answer.keys())[0]   # ==> list()로 형변환 시켜줘야 값을 뽑을 수 있다!!


# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))


#------------------------다른 사람 풀이---------------------------
def solutionn(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]

print(solutionn(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))


#--------------------------------------------------------------
def ssolution(participant, completion):
    hashDict = {}
    sumHash = 0

    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part   # key, value = hash(part), part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]  # hashDict[sumHash]의 value를 리턴

print(ssolution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))