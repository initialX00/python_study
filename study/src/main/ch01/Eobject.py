class Student:

    def __init__(self, name): # __init__으로 기본 실행
        self.name = name
        print("생성자 호출")

    def printInfo(self): # self가 this의 역할을 수행
        print("학생정보 출력")
        print(f"이름: {self.name}")

    @staticmethod
    def printId():
        print("아이디 출력")

    def __str__(self): # __str__로 toString의 역할을 수행한다. 호출없이 수행
        return f"이름: {self.name}"

s1 = Student("김준일")
print(s1)
s1.printInfo()
Student.printId()
