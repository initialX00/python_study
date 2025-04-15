#자바의 향상된 for문과 비슷하게 사용된다.
numbers = [1,2,3,4,5]
for num in numbers: #자바의 중괄호가 모두 :콜론으로 대체된다. 들여쓰기가 된부분까지가 범위가된다.
    print(num)
print(num)

print(range(10))
print(list(range(10)))

for n in range(5, 10):
    print(n)

input("입력하세요: ") #입력 받기
while True:
    selected = input("입력: ")
    if selected in ['q', '0']: #q나 0일 경우 반복 종료
        break
