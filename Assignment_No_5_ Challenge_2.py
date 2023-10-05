### Challenge 2: Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        add = self.num1 + self.num2
        return f"Addition of {self.num1} and {self.num2} is {add}"
    
    def subtract(self):
        sub = self.num2 - self.num1
        return f"Subtraction of {self.num2} from {self.num1} is {sub}"
    
    def multiply(self):
        multi = self.num1 * self.num2
        return f"Multiplication of {self.num1} and {self.num2} is {multi}"
    
    def divide(self):
        divi = self.num2 / self.num1
        return f"Division of {self.num2} by {self.num1} is {divi}"

obj = Calculator(10,94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())






## way 2 Taking input from user

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         add = self.num1 + self.num2
#         return f"Addition of {self.num1} and {self.num2} is {add}"
    
#     def subtract(self):
#         sub = self.num2 - self.num1
#         return f"Subtraction of {self.num2} from {self.num1} is {sub}"
    
#     def multiply(self):
#         multi = self.num1 * self.num2
#         return f"Multiplication of {self.num1} and {self.num2} is {multi}"
    
#     def divide(self):
#         divi = self.num2 / self.num1
#         return f"Division of {self.num2} by {self.num1} is {divi}"
    

# a = int(input("Enter num1 number : "))
# b = int(input("Enter num2 number : "))

# obj = Calculator(a, b)
# print(obj.add())
# print(obj.subtract())
# print(obj.multiply())
# print(obj.divide())

        


##### Thank You ..........













#### Thank You....