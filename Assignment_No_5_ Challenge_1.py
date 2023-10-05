# Challenge 1: Square Numbers and Return Their Sum   

## Way - I

class Point:

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x **2
        b = self.y **2
        c = self.z **2
        sum = a +  b + c
        return f"Sum of all {self.x}, {self.y} and {self.z} square is {sum}"

p = Point(1,3,5)
print(p.sqSum())




#### Taking input from user
## Way - II

# class Point:

#     def __init__(self, x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def sqSum(self):
#         a = self.x **2
#         b = self.y **2
#         c = self.z **2
#         sum = a +  b + c
#         return f"Sum of all {self.x}, {self.y} and {self.z} square is {sum}"

# x = int(input("Enter 1st number : "))
# y = int(input("Enter 2nd number : "))
# z = int(input("Enter 3rd number : "))

# p = Point(x,y,z)
# print(p.sqSum())



#### Thank You....













