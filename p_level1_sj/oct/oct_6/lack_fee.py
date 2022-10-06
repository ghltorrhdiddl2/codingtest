#이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면,
#총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 10만큼 부족하므로 10을 return
def solution(price, money, count):
    for i in range(1, count+1):
        money -= price*i
        
    return 0 if money > 0 else abs(money)

print(solution(3, 20, 4))