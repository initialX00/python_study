import Ffunction as f
print(f.add(10))

from Ffunction import add, add4
print(__name__) # __name__은 파일실행 위치를 나타낸다 => F__main__에서 실행하므로 main이라 나온다
print(add(10,20,30))

if __name__ == "__main__": #파이썬은 main문이 따로 없기에 직접 만들어야한다.
    print("시작")
    print(add4(10,20,30)) # => Ffunction의 __name__이 실행되므로 Ffunction이라 나온다

    try:
        print("예외처리")
        raise Exception("예외생성") # throw대신에 raise를 사용하여 예외를 실행시킨다
    except Exception as e:
        print("예외발생")
        print(e)