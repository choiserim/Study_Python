# 반복문에 반복할 수 있는 것에는 문자열, 리스트, 딕셔너리, 범위 등이 있습니다.
# range() 0부터 시작해서 지정한 숫자 -1까지 

from array import array


print("반복문 기본")
for i in range(10):
    i += 1
    print("{}번 반복합니다".format(i))

# 리스트와 반복문 함께 사용하기
# enumerate()는 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용하며
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환

list_a = [273, 32, 103, 45, 56]

print()
print("리스트와 반복문 함께 사용하기")
for i, element in enumerate(list_a):
    print("{}번째 요소는 {}입니다.".format(i, element))


for i in range(1, 10):
    print(i)

for element in range(len(list_a)):
   
    print("{}번째 요소는 {}입니다.".format(element, list_a[element]))

# 중첩 반목문

list_double = [[1, 2], [3, 4, 5], [6, 7, 8, 9] ]

print()
print("중첩 반복문")

for i in list_double:
    for j in i:
        print(i)

print()
print("중첩 반복문을 이용한 구구단")

for i in range(2, 10):
    #print(str(int(i)) + "단")
    #print("{}단".format(i))
    print(i, "단")
    for j in range(1, 10):
        k = i * j 
        #print(str(int(i)) + "*" + str(int(j)) + "=" + str(int(k)))
        #print("{}*{}={}".format(i, j, k))
        print(i, "*" , j, "=", k)

# 전개 연산자 - 리스트 앞에 *기호를 사용

a = [1, 2, 3, 4]
b = [*a, *a]
c = [*a, 5]

print()
print("전개 연산자 이용하기")
print(*a)
print(b)
print(c)