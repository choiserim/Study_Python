# 오류(error) - 프로그램 실행 전에 발생하는 구문 오류
#               프로그램 실행 중에 발생하는 예외 또는 런차임 오류

# 구문 오류 발생

# print("hellpo)

# 구문 오류 해결 - 코드를 제대로 작성하면 된다

print("hellp")

# 예외(exception) 처리 방법

# 프로그램 시작
print()
print("프로그램이 시작되었습니다.")

# 예외 발생
# print(list_a[1])

# 예외 해결 - 코드를 제대로 작성하면 된다
list_a = [1, 2, 3, 4, 5]

print(list_a[1])
print()

# 1.기본 예외 처리 - 조건문을 사용하여 예외를 처리

# 변수 선언
print("조건문으로 예외 처리하기")
user_input = input("정수 입력:")

# 기본 예외 처리 부분
if user_input.isdigit():

    input_number = int(user_input)

    print("입력한 숫자는{}".format(input_number))
else:
    print("정수가 아닙니다.")

print()


# 2.try except 구문 사용하기
print("try except 구문으로 예외 처리하기")
try:
    user_input = int(input("정수 입력:"))
    print("입력한 숫자는{}".format(user_input))

except:
    # pass
    print("정수가 아닙니다.")

print()

# 3.try except else 구문 사용하기
print("try except else구문으로 예외 처리하기")
try:
    user_input = int(input("정수 입력:"))
    
except:
    print("정수가 아닙니다.")

else:
    print("입력한 숫자는{}".format(user_input))