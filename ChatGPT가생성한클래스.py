# Base class Person
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string: 포맷 스트링(python 3.6이상)
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        #super()함수 제공
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")


# 테스트 코드
def test():
    print("=== Person 테스트 ===")
    p1 = Person(1, "Alice")
    p1.printInfo()

    print("\n=== Manager 테스트 ===")
    m1 = Manager(2, "Bob", "Team Lead")
    m1.printInfo()

    m2 = Manager(3, "Charlie", "Project Manager")
    m2.printInfo()

    print("\n=== Employee 테스트 ===")
    e1 = Employee(4, "David", "Python")
    e1.printInfo()

    e2 = Employee(5, "Eve", "JavaScript")
    e2.printInfo()

    # 추가 테스트
    print("\n=== 추가 테스트 ===")
    p2 = Person(6, "Frank")
    p2.printInfo()

    m3 = Manager(7, "Grace", "Senior Manager")
    m3.printInfo()

    e3 = Employee(8, "Hannah", "Data Analysis")
    e3.printInfo()

    # 동적 타입 테스트
    people = [p1, m1, e1, m2, e2, m3, e3]
    print("\n=== 리스트에서 각 객체 출력 ===")
    for person in people:
        person.printInfo()


# 테스트 실행
test()
