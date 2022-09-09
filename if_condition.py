# if조건문은 조건에 따라 실행의 흐름을 변경하는 구문이며 조건 분기라고 부른다.
# else 구문은 if 조건문 뒤에 사용하며 if 조건문의 조건이 충족되지 않을 경우 실행되는 부분이다.
# elif 세 개 이상의 조건을 연결해서 사용해야 할 경우 사용한다.

# 예제1. 현재시간 구하기
# 날짜/시간과 관련된 모듈을 가져온다.
import datetime

# 현재 날짜/시간을 구한다.
current_day = datetime.datetime.now()

# datetime 내용을 출력한다.
if 12 > current_day.hour:
    print("현재 시간은 오전{}시 {}분 입니다".format(current_day.hour, current_day.minute))
else:
    print("현재 시간은 오후{}시 {}분 입니다".format(current_day.hour, current_day.minute))

# 예제2. 홀수 짝수 구분하기
input_num = input("홀수짝수 구분을 위해 숫자를 입력하세요>")
cast_int = int(input_num)

if cast_int % 2 == 0:
    print("입력한 {}은 양수 입니다.".format(input_num))
else:
    print("입력한 {}은 음수 입니다.".format(cast_int))

# elif를 사용한 계절 구하기
# 날짜/시간과 관련된 모듈을 가져온다.
# import datetime

# 현재 날짜/시간을 구한다.
# current_day = datetime.datetime.now()

# 조건문을 이용하여 계절을 출력한다.
if 3<= current_day.month <=6:
    print("현재 {}월은 봄입니다.".format(current_day.month))
elif 7<= current_day.month <=8:
    print("현재 {}월은 여름입니다.".format(current_day.month))
elif 9<= current_day.month <=10:
    print("현재 {}월은 가을입니다.".format(current_day.month))
else:
    print("현재 {}월은 봄입니다.".format(current_day.month))

# if 조건문에 불이 아닌 다른 값이 들어 오면 False로 처리한다. - None, 0, 0.0, ""(빈문자열)
print()
print("False 값으로 처리하는 예")

if None:
    print("None은 True로 변환됩니다.")
else:
    print("None은 False로 변환됩니다.")

if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")

# ""와 " "는 결과값이 다르다.
print(type(""))
print(type(" "))
print("" == " ")
if "":
    print("\"빈문자열은\"은 True로 변환됩니다.")
else:
    print("\"빈문자열은\"은 False로 변환됩니다.")