# 튜플은 리스트와 비슷한 자료형이지만 한번 결정된 요소는 바꿀 수 없다.

# 튜플 선언 - 소괄호() 사용
tuple_exam1 = (10, 20, 30)

print("타입 구하기:", type(tuple_exam1))
print("길이 구하기:", len(tuple_exam1))
print(tuple_exam1)
print("요소로 접근해 값구하기:", tuple_exam1[0])
print("요소로 접근해 값구하기:", tuple_exam1[1])
print("요소로 접근해 값구하기:", tuple_exam1[2])
print()
# 튜플에 요소 하나만 추가할때는
# a = (24, ) 콤마(쉼표)를 사용한다.

# 괄호 없는 튜플

# *리스트와 튜플의 특이한 사용 - 변수를 선언과 할당이 가능하다
[a, b] = [10, 20]
(c, d) = (30, 40)

print("리스트와 튜플의 특이한 사용")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

tuple_exam2 = 10, 20, 30, 40
print("괄호가 없는 튜플의 값과 자료형")
print("tuple_exam2:", tuple_exam2)
print("type(tuple_exam2):", type(tuple_exam2))
print()

a, b, c = 10, 20, "hello"
print("괄호가 없는 튜플을 활용한 변수 선언과 할당")
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print()


a, b, c = 10, 20, "hello"
print("튜플을 활용한 변수 값 교환")
print("교환 전")
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print()

a, b, c = c, b, a
print("교환 후")
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print()

# 튜플과 함수
# 여러 개의 값을 리턴하고자 할 때 사용한다.

# 함수 정의
def test():
    return (10, 20)

# 함수 호출
a1, b1 = test()
# a, b, c = test()

# 출력
print("여러 개의 값을 리턴")
print("a:", a1, type(a1))
print("b:", b1, type(b1))
# print("c:", c1, type(c1))

