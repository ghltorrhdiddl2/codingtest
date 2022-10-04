#문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
#s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주
def solution(s):
    arr = []
    arr2 = []

    #ord()로 아스키코드 숫자로 변환
    for i in s:
        arr.append(ord(i))

    #버블 정렬 사용, 큰 수 앞으로
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    #숫자를 아스키코드 문자로 변환
    for i in arr:
        arr2.append(chr(i))

    #.join()으로 묶어서 출력
    return ''.join(arr2)

print(solution("Zbcdefg"))


#---------------다른 사람 풀이-------------------
def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))

#문자열도 sorted()로 정렬 가능!!!!!!
#''.join()으로 각 char들 한 단어로 묶어주기