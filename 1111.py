class Student_DD:
   name = ""
   major = ""
   grade = 0
   phonenumber = ""

   def __init__(self, value1, value2, value3, value4):
       self.name = value1
       self.major = value2
       self.grade = value3
       self.phonenumber = value4

   def introduce(self):
        print("안녕하세요. 저의 이름은 {}, {} 전공, {}학년이며, 연락처는 {}입니다".format(self.name, self.major, self.grade, self.phonenumber))

student1 = Student_DD("정영희", "데사", "1", "010-1234-5678")
student1.introduce()

