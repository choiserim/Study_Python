# min(), max(), sum()는 매개변수로 리스트를 사용한다.
# 리스트 선언
numbers = [103, 52, 273, 32, 45]

# 결과값 출력
print("리스트내 최솟값은:", min(numbers))
print("리스트내 최대값은:", max(numbers))
print("리스트내 합계는:", sum(numbers))
print("리스트를 사용하지 않고 구한 최솟값은:", min(27, 35, 11))
print("리스트를 사용하지 않고 구한 최대값은:", max(27, 35, 11))
print("리스트를 사용하지 않고 구한 합계는:", sum((27, 11)))
# sum()함수는 리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형 매개변수가 와야 한다.
print()


# reversed()함수로 리스트 뒤집기
# 리스트 선언
list_a = [1, 2, 3, 4, 5]
print("reversed() 함수 이용하기")
print(reversed(list_a))
print("reversed를 이용한 리스트 뒤집기:", list(reversed(list_a)))
print()

# 리스트의 enumerate()함수, 딕셔너리의 items() 함수와 반복문 조합하기
# 리스트의 enumerate()함수
# 리스트 선언
list_e = ["요소1", 1, 1.0]

# 반복문사용과 결과 출력
print("enumerate()함수")
for par, val in enumerate(list_e):
    print("{}번째 요소는 {}입니다".format(par, val))
print()

# 딕셔너리의 items() 함수
# 딕셔너리 선언
dic_a = {"키1":"값A", 2:3, "영화":["아이언맨", "미션임파서블"]}

# 반복문사용과 결과 출력
print("enumerate()함수")
for par, val in dic_a.items():
    print("{}번째 키의 값은 {}입니다".format(par, val))

# 리스트 내포 - 리스트 선언시 for 구문을 리스트 내부에 사용하는 것을 말한다.
# 리스트내 for 반복문 사용하기
list_for = [i * i for i in range(0, 20, 2)]

# 출력하기
print()
print("리스트 내포 사용 결과는:", list_for)

# 리스트 내포에 for 반복문과 if 조건문 사용하기
# 리스트 선언
arr = ["사과", "자두", "초콜릿", "바나나"]
output = [fruit for fruit in arr if fruit != "초콜릿"]

# 출력하기
print()
print("리스트 내포 for, if 사용 결과는:", output)

