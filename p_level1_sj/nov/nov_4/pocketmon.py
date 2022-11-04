from collections import Counter
def solution(nums):
    n = int(len(nums)/2)    # n마리
    species = len(Counter(nums))   # 종 갯수

    if species == n:
        return species
    elif species > n:
        return n
    else:
        return species

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))


#------------------다른 사람 풀이------------------
def ssolution(ls):
    return min(len(ls)/2, len(set(ls)))   # min(n마리, 종 갯수)

print(ssolution([3,3,3,2,2,4]))
print(ssolution([3,3,3,2,2,2]))