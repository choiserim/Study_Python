"""
함수는 어떤 작업을 수행하는 코드를 모아 이름을 붙인 것이다. 
변수를 이용해 데이터에 이름을 붙이는 것처럼, 함수를 이용해 프로그램 조각에 이름을 붙일 수 있다. 
이렇게 코드를 묶어 이름을 붙이는 것을 함수 정의라고 한다. 
함수를 사용하는 것을 함수를 호출한다고 표현하며 함수를 호출할 때는 괄호 내부에 여러 가지 자료를 
넣게 되는데 이러한 자료를 매개변수라고 한다.
또한 함수를 호출해서 최종적으로 나오는 결과를 리턴값이라고 부른다."""

# 기본적인 함수

# 함수 정의 
def print_3_times():
    # 수행 문장
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

# 함수 호출
print_3_times()
print()

# 매개변수를 이용한 함수 

# 함수 정의
def print_n_times(value, n):
    # 수행 문장
    print("매개변수를 이용한 함수")
    for i in range(n):
        print(value)

# 함수 호출
print_n_times("안녕하세요", 6)

# 가변 매개변수 - 매개변수 개수가 변할 수 있다는 의미
# 가변 매개변수의 제약 조건
# 1. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# 2. 가변 매개변수는 하나만 사용할 수 있다.

# 함수 정의
def print_n_times(n, *values):
    # 수행 문장
    print()
    print("가변 매개변수")
    for i in range(n):
        for value in values:
            # 줄바꿈 없애기 end=""
            print(value, end=" ")
        print()

# 함수 호출
print_n_times(3,"안녕하세요", 23, "cloud39")

# 기본 매개변수 - 매개변수=값 형태이며 매개변수를 입력하지 않았을 경우 기본 매개변수가 기본값이 된다.
# 기본 매개변수의 제약조건
# 기본 매개변수 뒤에는 일반 매개변수 올 수 없다.

# 함수 정의
def print_n_times(value, n=2):
    print()
    print("기본 매개변수")
    # 수행 문장
    for i in range(n):
        print(value)

# 함수 호출
print_n_times("반갑습니다.")


# 가변 매개변수와 키워드 매개변수 사용하기
# 키워드 매개변수 함수 호출시 사용되는 기본 매개변수를 말한다.
# 키워드 매개변수를 가변 매개변수와 함께 사용할 때는 키워드 매개변수를 지정해서 값을 입력한다.

# 함수 정의
def print_n_times(*values, n=2):
    print()
    print("가변 매개변수와 키워드 매개변수 함깨 사용")
    # 수행 문장
    for i in range(n):
        for value in values:
            print(value)
        
        print()

# 함수 호출
print_n_times("일하는", "감사함", "갖자", n=3)

# 기본 매개변수 중에서 필요한 값만 입력하기

# 함수 정의
def test(a, b=10, c=100):
    # 수행 문장
    print(a + b + c)

# 함수 호출
test(10, 20, 30)
test(20)
test(20, c=20, b=40)
print()

# 리턴 - 함수를 실행했던 위치로 돌아가라는 뜻으로 함수가 끝나는 위치를 의미한다.
# 자료 없이 리턴하기

print("return - 자료없이 리턴하기")
# 함수 정의
def return_exam1():
    # 수행 문장
    print("A위치 입니다.")
    return
    print("B위치 입니다.")

# 함수 호출
return_exam1()
print()

# 자료와 함께 리턴하기
print("return - 자료와 함께 리턴하기")

# 함수 정의
def return_exam2():
    return 100

# 함수 호출
value = return_exam2()
print(value)

print()
# 기본적인 함수의 활용 - 함수 정의, 변수 선언, return을 사용
print("기본적인 함수의 활용")

# 함수 정의
def sum_all(start, end):
    # 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더한다.
    for i in range(start, end + 1):
        output += i
    # return 사용
    return output

# 함수 호출
print("0 부터 100까지의 합=", sum_all(0, 100))
print("0 부터 1000까지의 합=", sum_all(0, 1000))
print()

# 함수 정의
def sum_all(start=0, end=100, step=1):
    # 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더한다.
    for i in range(start, end + 1, step):
        output += i
    # return 사용
    return output

# 함수 호출
print("0 부터 100까지의 합=", sum_all(0, 100))
print("0 부터 100까지의 합=", sum_all(end=100))
print("0 부터 100까지 2씩증가 할때의 합=", sum_all(step=2))

# 재귀함수
# 파보나치 수열

# 함수 정의
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))
    
# global keyword

# 변수 선언
counter = 0

# 함수 정의
def fibonacci(n):
    counter += 1

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

print("fibonacci(1):", fibonacci(1))

 