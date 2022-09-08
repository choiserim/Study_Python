# boolean - 어떤 조건이 참이냐 거짓이냐 판단
# 비교 연산자를 이용한 boolean 활용
# == 같다, != 다르다, < 작다, > 크다, <= 작거나 같다, >= 크거나 같다

a = 10
b = 100
print("비교 연산자 활용")
print("a와 b는 같다", a == b)
print("a와 b는 서로 다르다", a != b)
print("a가 b보다 작다", a < b)
print("a가 b보다 크다", a > b)
print("a가 b보다 작거나 같다", a <= b)
print("a가 b보다 크거나 같다", a >= b)
print()

# 논리 연산자를 활용
# and 그리고, or 또는, not 아니다

print("논리 연산자 활용")
if a < b and a <= b: # 둘 다 참일때
    print("and 연산자의 값은 True")
else:
    print("and 연산자의 값은 False")

if a == b or a < b: # 한 쪽만 참일때
    print("or 연산자의 값은 True")
else:
    print("or 연산자의 값은 False")

if not a < b: # 참과 거짓을 반대로
    print("not 연산자의 값은 True")
else:
    print("not 연산자의 값은 False")


