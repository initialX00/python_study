#__main__에서 사용된다

def add(num1:str="0", num2 = 0, num3 = 0):
    return num1, num2, num3
print(add(10))

def add4(*b):
    print(__name__)
    return sum(b)

if __name__ == "__main__": #파이썬은 main문이 따로 없기에 직접 만들어야한다. 다른 곳에서 함수를 호출할 경우 실행되지 않느다.
    print(add4(1, 2, 3, 4, 5))

