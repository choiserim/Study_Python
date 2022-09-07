# format()는 문자열이 가지고 있는 함수
# "{} {}".format(1000, "금액")의 형태로 괄호 안에 매개변수는 차례로 대치되며 문자열이 된다.
# {}개수가 format()함수의 매개변수보다 많거나 적으면 indexError가 발생한다.

print("{}만원".format(50000))
print("인공지능{}로 {}억 만들기".format("개발", 9000))

#공백, 기호, 0을 이용하여 특정 칸에 출력하기 

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)

print(output_a, type(output_a)) #기본
print(output_b, type(output_b)) #5칸 띄어서 출력하기

output_c = "{:05d}".format(52) #52를 5칸을 띄어서 출력하며 앞에 빈칸은 0으로 채운다
output_d = "{:05d}".format(-52)
print(output_c, type(output_c))
print(output_d, type(output_d))

# 부동 소수점 출력하기
# 소수점 끝 부분에 0이 추가된다.
# {:f}에서 f는 기본적으로 소수점 6자리까지 표현된다.

float_a = "{:f}".format(5.273)
float_b = "{:5f}".format(52.27)
float_c = "{:.2f}".format(52.273)  #소수점 아래 자릿수 지정하기
float_d = "{:+011f}".format(52.273)
float_e = "{:g}".format(52.00) #소수점 아래 0제거하기

print(float_a, type(float_a))
print(float_b, type(float_b))
print(float_c, type(float_c))
print(float_d, type(float_d))
print(float_e, type(float_e))