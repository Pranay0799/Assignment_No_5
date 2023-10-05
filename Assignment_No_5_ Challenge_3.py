### Challenge 3: Implement the Complete Student Class



class Student:

    def __init__(self):
        self.__name = "Pranay"
        self.__rollNumber = "DS140823"

    def setName(self, new_name):
        self.__name = new_name

    def getName(self):
        return self.__name
    
    def setRollNumber(self, new_rollNumber):
        self.__rollNumber = new_rollNumber

    def getRollNumber(self):
        return self.__rollNumber


s1 = Student()
print(s1.getName())
print(s1.getRollNumber())

print()

##### setting name and rollnumber
s1.setName("Edyoda")
s1.setRollNumber("DS200000")
print("After set Name : ", s1.getName())
print("After set RollNumber : ",s1.getRollNumber())



### Thank You.....

