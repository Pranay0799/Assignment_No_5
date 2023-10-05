### Challenge 4: Implement a Banking Account


class Account:

    def __init__(self, title = None, Balance = 0):
        self.title = title
        self.Balance = Balance

class SavingsAccount(Account):

    def __init__(self,title = None, Balance = 0, interestRate = 0):
        super().__init__(title, Balance)
        self.interestRate = interestRate

b =SavingsAccount("Ashish", 5000, 5)
print("Title : ",b.title)
print("Balance : ",b.Balance)
print("InterestRate : ", b.interestRate)



##### Thank You.....       
