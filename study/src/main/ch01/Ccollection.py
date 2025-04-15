numberList = []
numberList = list()
numberList.append(10) #배열 합치기
numberList.append("가")
numberList.append([1,2,3,True])
print(numberList)

nameDict = {}
nameDict = dict() #키밸류의 자료형
nameDict["name1"] = "김준일"
print(nameDict)
print(nameDict["name1"])
print(nameDict.get("name1"))
nameDict2 = {"name1": "김준일", "name2": "김준이"}
print(nameDict2.keys())
print(nameDict2.values())
print(nameDict2.items()) #키밸류 묶음 (튜플)

#튜플 자료형
#리스트와 같지만 소괄호로 나타낸다. 불변이다.
#불변이기에 사용할 수 있는 함수가 제한적이다. list로 감싸서 list로서 사용할 수 있다.

nameList = ["김준일", "김준이"]
nameTuple = ("김준일", "김준이")
for name in nameList:
    print(name)
for name in nameTuple:
    print(name)

nameList2 = nameList + list(nameTuple)
print(nameList2)