#내가 푼 문제
# def solution(num):
#     if num % 2 == 1:
#         answer = "Odd"
#     else:
#         answer = "Even"
#     return answer
#
# solution(3)


#다른 사람이 푼 문제
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))

#-> if문 만족하면 바로 return시켜 나오게 함