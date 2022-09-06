# cast(자료형 변환)
# 문자열 자료형을  숫자형 자료형으로 변환

string_a = input("첫 번째 숫자를 입력하세요>")
int_a = int(float(string_a))
float_a = float(string_a)

string_b = input("두 번째 숫자를 입력하세요>")
int_b = int(float(string_b))
float_b = float(string_b)

print("입력한 숫자를 이용한 문자열 연결 연산 결과:", string_a + string_b, type(string_a + string_b))
print("문자열 자료형을 int형 자료형으로 변환 후 덧셈 연산 결과:", int_a + int_b, type(int_a + int_b))
print("문자열 자료형을 float형 자료형으로 변환 후 덧셈 연산 결과:", float_a + float_b, type(float_a + float_b))

# 숫자형 자료형을 문자형 자료형으로 변환

output_a = str(52)
output_b = str(52.273)

print(type(output_a), output_a)
print(type(output_b), output_b)
print("문자열 연결 연산자를 이용한 결과:", output_a + output_b)

# inch를 cm단위로 변경하기
raw_input = input("inch 단위의 숫자를 입력하세요>")

inch = int(raw_input)
cm = inch * 2.54

print("inch를 cm으로 변환한 결과 값은:", cm)