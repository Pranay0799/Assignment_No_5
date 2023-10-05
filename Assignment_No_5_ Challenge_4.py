### Challenge 4: Implement a Banking Account


class Account:

    def __init__(self, title = None, Balance = 0):
        self.title = title
        self.Balance = Balance

class SavingsAccount(Account):

    def __init__(self,title = None, Balance = 0, interestRate = 0):
        super().__init__(title, Balance)
        self.interestRate = interestRate

a1 =Account("Ashish", 5000)
print("Title : ",a1.title)
print("Balance : ",a1.Balance)

print()

b1=SavingsAccount("Ashish", 5000, 5)
print("Title : ",b1.title)
print("Balance : ",b1.Balance)
print("InterestRate : ", b1.interestRate)



##### Thank You.....       
