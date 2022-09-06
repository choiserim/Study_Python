# 복합 대입 연산자(숫자) - 기존의 연산자와 조합해서 사용
number = 100 # 110 -> 100 -> 200 -> 100.0 -> 몫:33 나머지:1 -> 1**2 = 1.0

number += 10 # number = 100 + 10
number -= 10 # number = 110 - 10
number *= 2  # number = 100 * 2
number /= 2  # number = 200 / 2
number %= 3  # number = 100 % 3
number **= 3

print(number)

# 복합 대입 연산자(문자열) - 기존의 연산자와 조합해서 사용
string = "안녕하세요?"
string += "반갑습니다."
string += "제 이름은 cloud39입니다."

print(string)

string *= 3 # 문자열과 숫자 조합으로 구성

print(string)