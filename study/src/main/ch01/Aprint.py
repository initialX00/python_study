print("hello python", end="") #printf, println처럼 비슷한 함수를 쓰지 않고, 하나의 함수로 함수 내부의 설정값을 조정한다.
print("hello python2", end="!!!")

num = 10
name = "김준일"
print(num == 10)
isEmpty = False and True #boolean값은 첫글자 대문자

text = """
aaaaa
aaaaa
"""
print(text)

print(id(num), id(10)) #id함수는 주소값을 나타낸다.

name = "김준일"
age = 32
profile1 = "이름: {0}, 나이: {1}".format(name, age) #문자열 자체가 객체이기때문에 . 사용가능 (자바도 마찬가지)
print(profile1)
profile2 = f"이름: {name}, 나이: {age}" #문자열에 f를 붙여 f포맷팅이되어 변수를 넣을 수 있다. (자바의 백쿼터)
print(profile2)

