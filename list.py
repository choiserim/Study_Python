# list란 대괄호[] 내부에 여러 종류의 자료형을 element(요소)로 구분하여 넣어 사용한다.
# 제로 인덱스(index - 차례, 목록) 방식으로 위치를 나타낸다.

list_a = [273, 32, "문자열", 3.14, True, False]
list_b = [[1, 2, 3], [4, 5, 5], [7, 8, 9]] # 리스트안에 리스트를 사용할 수 있다.

print("list_a 이용하기")
print(list_a[2])
print(list_a[2][2]) # 리스트 접근 연산자를 이중으로 사용할 수 있다.
print()
print("list_b 이용하기")
print(list_b[1])
print(list_b[2][2])
print()
print("list_b 요소 변경하기")
list_b[2][2]=10
print(list_b)
print()

# 리스트 연산자 - + 연결, * 반복, len() 길이

print("리스트 연산자 활용하기")
print("+ 연결 연산자 이용하기", list_a + list_b)
print("* 반복 연산자 이용하기", list_a * 2)
print("len()함수를 이용한 길이 구하기", len(list_a)) # len()함수는 1부터 숫자가 시작된다.

# 리스트에 요소 추가하기 - append()는 리스트 마지막 요소 뒤에, insert()는 원하는 위치에 추가된다.
# 리스트명.append(요소), 리스트명.insert(위치, 요소)
# append(), insert()는 한 개의 요소(매개변수) 값만 지정할 수 있다.

list_a = [1, 2, 3]

# append()를 이용한 리스트 요소 추가

print()
print("append()를 이용한 리스트 뒤에 요소 추가하기")
list_a.append([4, 5, 6]) # 리스트 자체를 한 개의 요소로 인식
print(list_a)

# insert()를 이용한 리스트 요소 추가

print()
print("insert()를 이용한 리스트 뒤에 요소 추가하기")
list_a.insert(0, [7, 8, 9])  # 리스트 자체를 한 개의 요소로 인식
print(list_a)

# extend()를 이용하여 여러 요소를 추가하기

list_a = [1, 2, 3]
list_a.extend([4, 5, 6])

print()
print("extend()를 이용한 여러 요소 추가하기")
print(list_a)
print()

# 리스트에 요소 제거하기
# 리스트의 요소를 제거하는 인덱스로 제거, 값으로 제거 방법으로 크게 두 가지로 나눱니다.
# 인덱스로 제거하기 - del 키워드:슬라이싱으로 여러 요소를 제거할 수 있다., pop() 함수
# 값으로 제거하기 - remove() 함수:지정한 값이 리스트 내부에 중복된 경우 먼저 발견된 하나만 제거된다.
# 모두 제거하기 - claer()

list_a = [0, 1, 2, 3, 4, 5]

print("리스트 요소 하나 제거하기")

del list_a[0]
print("1. del 키워드를 이용한 리스트 요소 제거:", list_a)

del list_a[1:3]

print("1. del 키워드 슬라이싱 이용한 리스트 요소 제거:", list_a)


list_a.pop(0)
print("2. pop() 함수를 이용한 리스트 요소 제거:", list_a)

list_c = [1, 2, 1, 2]
list_c.remove(2)

print("3. remove() 함수를 이용한 리스트 요소제거:", list_c)

list_c.clear()
print("4. clear() 함수를 이용한 모든 리스트 요소 제거하기:", list_c)
print()

# 리스트 정렬하기 - sort():오름차순, reverse():내림차순

list_e = [57, 273, 103, 32, 275, 1, 7]
list_e.sort()

print("리스트 정렬하기")
print("1. sort()함수로 정렬하기:", list_e)

list_e.reverse()

print("2. reverse()함수로 정렬하기:", list_e)

# 리스트 내부에 있는지 없는지 확인하기 - in, not in는 boolean형태로 값을 반환한다.

list_check = [273, 32, 105, 57, 52]

print()
print("리스트 내부에 있는지 없는지 확인하기")
print(273 in list_check)
print(213 not in list_check)
