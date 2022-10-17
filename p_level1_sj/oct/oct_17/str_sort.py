# 사전 순 배열, index n
def solution(strings, n):
    arr = []
    for i in range(97, 123):
        for j in strings:
            if j[n] == chr(i):
                arr.append(j)
    for i in range(0, len(arr)-1):
        if arr[i][n] == arr[i+1][n]:
            arr[i:i+2] = sorted(arr[i:i+2])

    return arr

# print(solution(["sun", "bed", "car"], 1))
# print(solution(["abce", "abcd", "cdx"], 2))


#-----------다른 사람 풀이----------------
# 람다식 사용
def solution1(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])    


#----------------------------------------
def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)

    return strings


#---------------------------------------
def solution2(strings, n):
    str=[]
    for i in strings:
        str.append(i[n]+i)       # n번째 문자를 앞에 붙임
    str.sort()
    # print(f'str-----------> {str}')     ['cabcd', 'cabce', 'xcdx']
    return [i[1:] for i in str]

print(solution2(["sun", "bed", "car"], 1))
print(solution2(["abce", "abcd", "cdx"], 2))