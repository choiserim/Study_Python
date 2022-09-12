# while 반복문 

# for 반복문처럼 반복하기
i = 0

print("for 반복문 처럼 반복하기")

while i < 10:
    print(i)
    i += 1

# 상태를 기반으로 반복하기
list_a = [1, 2, 1, 2]
i = 2

print()
print("상태를 기반으로 반복하기")
while i in list_a:
    list_a.remove(i)

print(list_a)

# break 키워드와 continue 키워드 사용하기
# break 키워드를 이용한 반복문 종료
i = 0

# 반복문 실행
while True:
    print("{}번째 반복 입니다.".format(i))
    i += 1

    input_text = input("종료하시겠습니가?(y/n)")

    # break 키워드를 이용한 반복문 종료
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break

# continue 키워드를 이용한 다음 반복문으로 넘어가기
# 변수 선언
numbers = [5, 15, 6, 20, 7, 25]

# 반복문 실행
for number in numbers:

    # continue 키워드를 이용한 다음 반복문으로 넘어가기
    if number < 10:
        continue
    print(number)
