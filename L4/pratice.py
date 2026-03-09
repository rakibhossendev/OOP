import faker

class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

n = int(input("Enter student number: "))
fake = faker.Faker()

i = 1
while i <= n:
    s = Student(i, fake.name(), 20+i)
    
    data = [f"Id :{s.id}",f"Name :{s.name}",f"age :{s.age}"]
    for el in data:
        print(el)
    

    i += 1