user_info={'pin_num':1234,'Fund_available':50000}


def withdraw():
    amount=int(input("Enter The amount to withdraw: "))
    if amount>user_info['Fund_available']:
        print("You do not have sufficient Funds to withdraw.please withdraw a smaller fund.")
    else:
        user_info['Fund_available']=user_info['Fund_available']-amount
        print(str(amount),"Rupees Successfully withdrawn .Remaining Balance is :" ,str({user_info['Fund_available']}))
def Deposit():
    amount=int(input("Enter the money to deposit:"))
    print("Place The Money In The Machine")
    print("You have Successfully Deposited Money.Remaining Balance is : ",str({user_info['Fund_available']+amount}))
           
def Balance():    
    print("Total Amount Available in your Account is:",user_info['Fund_available'],"ruppess") 
print("Welcome to the Bank") 
pin_num=int(input("Enter Your Four Digit Pin Number: "))
if pin_num ==user_info['pin_num']:
 print("please select the Option: 1. withdrawl 2. Deposit  3.Balance")
 Option=int(input("Enter Your Option now: "))
 if Option==1:
    withdraw()
 elif Option ==2:
    Deposit()
 elif Option ==3:
    Balance()  
 else:
    print("Please Enter a valid option: ")   
else:
    print("You have Entered a Wrong pin number")          

