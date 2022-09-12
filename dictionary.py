# 키를 기반으로 값을 저장하는 자료형 
# {키:값, 키:값, ...}형태로 ,를 연결해서 선언한다

# 딕셔너리 선언
dic_a = {
    "name":["스파이터 맨", "어벤져스", "헐크", "토르"], "type":"히어로 무비", 
    "director":["안소니 루소", "조 루소"],
    "age":[18, 20], 1:40, 2:[3, 4, 5], 4:"cloud39"
}

# 딕셔너리 출력
print("dictionary 이용하기") 
print(dic_a[4], dic_a["name"])

# 값 변경
dic_a["name"][2] = "아이어맨" 

print()
print("name 키의 헐크 변경 값:", dic_a["name"])

# 딕셔너리에 값 추가하기
dic_a["price"] = 5000, 10000, 20000

print()
print("딕셔너리 값 추가하기")
print(dic_a)

# 딕셔너리에 값 제거하기
del dic_a[1]

print()
print("딕셔너리 값 제거하기")
print(dic_a)

# 딕셔너리 내부에 키가 있는지 확인하기 - in 키워드
dic_a = {
    "name":["스파이터 맨", "어벤져스", "헐크", "토르"], "type":"히어로 무비", 
    "director":["안소니 루소", "조 루소"],
    "age":[18, 20], 1:40, 2:[3, 4, 5], 4:"cloud39"
}

key = input("접근하고자 하는 키값을 입력하세요>")

print("현재의 딕셔너리\n", dic_a)

if key in dic_a:
    print(dic_a[key])

elif int(key) in dic_a:
    print(dic_a[int(key)])

else:
    print("접근하고자 하는 키값이 없습니다.")

# 딕셔너리 내부에 키가 있는지 확인하기 - get()
dic_a = {
    "name":["스파이터 맨", "어벤져스", "헐크", "토르"], "type":"히어로 무비", 
    "director":["안소니 루소", "조 루소"],
    "age":[18, 20], 1:40, 2:[3, 4, 5], 4:"cloud39"
}

key = input("get() 함수를 이용해 값을 가져옵니다>")

if key in dic_a:
    print(dic_a.get(key))

elif int(key) in dic_a:
    print(dic_a.get(int(key)))

else:
    print("접근하고자 하는 키값이 없습니다.")

# for 반복문과 딕셔너리 함께 사용하기
dic_a = {
    "name":["스파이터 맨", "어벤져스", "헐크", "토르"], "type":"히어로 무비", 
    "director":["안소니 루소", "조 루소"],
    "age":[18, 20], 1:40, 2:[3, 4, 5], 4:"cloud39"
}

print()
print("for 반복문과 딕셔너리 함께 사용하기")

for i in dic_a:
    print("키는 {} 값은 {} 입니다".format(i, dic_a[i]))