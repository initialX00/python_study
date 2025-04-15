def add(num1, num2):
    return num1 + num2, num1, num2 #리턴값이 여러개면 튜블로 자동으로 변환한다
print(add(10, 20))
n1, n2, n3 = add(10, 20)
print(n1, n2, n3)

def add(num1, num2, num3 = 0):
    return num1, num2, num3
print(add(10,20)) #파이썬은 오버로딩이 되지 않는다. 비슷하게 쓸려면 디폴트 값을 줘야한다.
#디폴트값은 뒤에서부터 잡는다.

def add(num1:str="0", num2 = 0, num3 = 0): #자료형 선언도 가능하다. 다만 안내일뿐 강제성이 없기에 다른것도 가능하다
    return num1, num2, num3
print(add(10))

def add2(*a): # *별을 사용하여 튜플의 크기를 동적으로 사용이 가능해진다
    print(a)
    result = 0
    for n in a:
        result += n
    return result
print(add2(1,2,3,4,5))

def add3(*b):
    print(__name__)
    return sum(b)
print(add3(1,2,3,4,5))
