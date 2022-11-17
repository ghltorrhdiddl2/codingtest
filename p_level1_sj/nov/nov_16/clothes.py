from collections import Counter
def solution(clothes):
    answer = 1
    cnt = Counter([type for clothe, type in clothes])
    print(cnt)
    for i in cnt.values():
        answer *= (i+1)
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
