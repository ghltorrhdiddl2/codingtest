#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
numbers = list(range(1, 10001))
remove_list = []

for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_list.append(num)

for remove_num in set(remove_list):
    numbers.remove(remove_num)

for self_num in numbers:
    print(self_num)


#---------------------------------------------------------
numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)

#-----------------------------------------------------------------
#set() 자료형 : 교집합, 합집합, 차집합 가능!!
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])
#교집합
print(set1 & set2)
print(set1.intersection(set2))

#합집합
print(set1 | set2)
print(set1.union(set2))

#차집합
print(set1 - set2)
print(set1.difference(set2))

#대칭 차집합
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])

print(set1 ^ set2)

#{1, 2, 8, 9}

#집합 추가와 제거
set1 = set([1,2,3,4,5,6])
set1.update([7,8,9])         # update
print(set1)

set1.remove(9)               # remove
print(set1)

#{1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3, 4, 5, 6, 7, 8}