class Restaurant:
    
    def __init__(self, name):
        self.restroName=name
        self.food={}
        self.food={1 : {"Name":"Tandoori Chicken","Quantity":"4 Pices","Price":240,"Discount":10,"Stock":20},
                   2 : {"Name":"Vegan Burger","Quantity":"1 Pices","Price":320,"Discount":20,"Stock":10},
                   3 :{"Name":"Truffle Cake","Quantity":"500 gm","Price":900,"Discount":30,"Stock":5}}
        self.adminDetails={}
        self.userDetails={}
        self.ordered_item=[]
        self.food_ID=len(self.food)+1
        

    # admin functionalities
    def admin_register(self):
        try:
            self.adminEmail=input("Enter your email-id : ")
            self.adminPass=input("Enter your password : ")
            self.adminDetails={"Email_ID":self.adminEmail,"Password":self.adminPass}
            print("!! Admin account is created Successfully !!\n")
            print(f"Welcome TO {self.restroName} Restaurant\n")
            print("Admin Details : ")
            for i in self.adminDetails:
                print(i , ":", self.adminDetails[i])
        except Exception as e:
            print("!! Please provide valid inputs !!\n ")
            
            
    def admin_login(self):
        try:
            print(f"Welcome to {self.restroName} Restaurant...!!!\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.adminDetails.values())!=0:
                if email==self.adminEmail and pas==self.adminPass:
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item\n5. Exit\nYour Responce : ")
                        z=input("Pleaase select one option and Enter your option :")
                        if z=="1":
                            self.add_food_item()
                        elif z=="2":
                            self.edit_food_item()
                        elif z=="3":
                            self.view_food_item()
                        elif z=="4":
                            self.delete_food_item()
                        elif z=="5":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!!You enter Incorrect Email or Password!!\n")
            else:
                print("\n! There is no admin account !\n!! Please creat your Account First..!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")
            
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs : "))
            discount=float(input("Enter the discount in Rs : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
        
        
    def edit_food_item(self):
        try:
            x=int(input("Enter the Food ID you want to update : "))
            if x in self.food.keys():
                y = int(input("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \nYour responce : "))
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n! Successfully Updated !\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n! Successfully Updated !\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs : "))
                    print("\n! Successfully Updated !\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs : "))
                    print("\n! successfully Updated !\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n! Successfully Updated !\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n! Incorrect Food ID or This food ID not present.!\n")
        except Exception as e:
            print("\n!! Please provide valid inputs !!\n")  
            
            
    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")
            

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood item will Delete Permanently\n")
            x = int(input("Enter the Food ID "))
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
                
                
    # user functionalities    
    def user_register(self):
        try:
            user_name = input("Enter your full name : ")
            phone_no = int(input("Enter your 10 digit phone number : "))
            email = input("Enter your email id : ")
            password = input("Enter your password : ")
            address = input("Enter your address with area PIN code ")
            self.userDetails = {"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
            print("!! Your Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restroName} Restaurant\n")
            print("User Details : ")
            for i in self.userDetails:
                print(i, ":", self.userDetails[i])        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")                 
               
    def user_login(self):
        try:
            print(f"Welcome TO {self.restroName} Restaurant!!!\n")
            email = input("Enter Your Email ID : ")
            pas = input("Enter Your Password : ")
            if len(self.userDetails.values())!=0:                                                           
                if email==self.userDetails["Email_ID"] and pas==self.userDetails["Password"]:     
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit\nYour Responce : ")
                        z=input()
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no User Account with this Email ID !\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  
            
            
    def place_order(self):
        try:
            if len(self.food)!=0:
                print("list of Availabe Food Items :\n")
                menu=[]
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"],self.food[items]["Price"]]) 
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    x = input("\nEnter 1 to Place the Order\nEnter 2 to Exit \n")
                    if x=="1":
                        print("Enter the Food Id number You want to ordered separated by comma : ")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                                break
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                        print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("!! Sorry! No Food Items are available Now !!\n")
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")     
                
                
    def ordered_history(self):
        print("List of Previous ordered : \n")
        for i in self.ordered_item:
            print(i)
                    
    def update_details(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                x=input("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\nYour Responce : ") 
                if x=="1":
                    self.userDetails["User Name"]=input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x=="2":
                    self.userDetails["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")      
                elif x=="3":
                    self.userDetails["Email_ID"]=input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")
                    
                elif x=="4":
                    self.userDetails["Password"]=input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="5":
                    self.userDetails["Address"]=input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")
                    
                if x in ["1","2","3",'4',"5"]:
                    for i in self.userDetails:
                        print(i, ":",self.userDetails[i])
                else:
                    print("\nPlease Enter correct Input\n")      
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")
            
            
       # defining the Main function    

try:
    def main():
        obj=Restaurant("Pranay's")
        print(f"!!  Welcome To {obj.restroName} Restaurant  !!")
        print("!!----------------------------------------------------------")
        print("Sir/Ma'am ! What you want to eat in my Restro ?:)")
        print("-----------------------------------------------------------!!")
        
        while True:
            x = input("1. Admin\n2. User\n3. Exit\nYour Responce : ")
            if x=="1":
                while True:
                    print("\nEnter the Below Options")
                    y = input("1. Register\n2. Login\n3. Exit\nYour Responce : ")
                    
                    if y=="1":
                        obj.admin_register()
                    elif y=="2":
                        obj.admin_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")
                    
            elif x=="2":
                while True:
                    print("Enter the Below Options")
                    y=input("1. Register\n2. Login\n3. Exit\nYour Responce : ")
                    
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("Something went wrong please give input carefully")


if __name__ == "__main__":
    main()
