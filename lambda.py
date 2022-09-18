# 람다란 함수의 매개변수로 함수전달 
# 함수의 매개변수에 사용하는 함수를 콜백함수라 한다.

# 함수 정의
def call_10_times(func):
    for i in range(10):
        func()

# 함수 정의
def print_hello():
    print("hello")

# 함수 호출
print("콜백함수 이용하기")
call_10_times(print_hello)
print()

# 대표적인 콜백함수 filter(), map() 함수
# 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성

# 함수 정의
def multiply(item):
    return item * item

def under_3(item):
    return item < 3

# 리스트 선언
list_input = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(multiply, list_input)
print("map()함수의 실행 결과")
print("map(multiply, list_input)", output_a)
print("map(multiply, list_input)", list(output_a))
print()

# filter() 함수 사용 - 리턴값이 True인 것
output_b = filter(under_3, list_input)
print("filter()함수의 실행 결과")
print("filter(under_3, list_input)", output_b)
print("filter(under_3, list_input)", list(output_b))
print()

# 람다 사용해 보기

# 람다 선언
power = lambda x: x * x
under = lambda x: x < 3

# 리스트 선언
list_input = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(multiply, list_input)
print("람다를 이용한 map()함수의 실행 결과")
print("map(multiply, list_input)", output_a)
print("map(multiply, list_input)", list(output_a))
print()

# filter() 함수 사용 - 리턴값이 True인 것
output_b = filter(under_3, list_input)
print("람다를 이용한 filter()함수의 실행 결과")
print("filter(under_3, list_input)", output_b)
print("filter(under_3, list_input)", list(output_b))
print()

# 람다를 매개변수로 사용하기

# 리스트 선언
list_input = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(lambda x: x * x, list_input)
print("람다를 매개변수로 이용한 map()함수의 실행 결과")
print("map(multiply, list_input)", output_a)
print("map(multiply, list_input)", list(output_a))
print()

# filter() 함수 사용 - 리턴값이 True인 것
output_b = filter(lambda x: x < 3, list_input)
print("람다를 매개변수로 이용한 filter()함수의 실행 결과")
print("filter(under_3, list_input)", output_b)
print("filter(under_3, list_input)", list(output_b))
print()


