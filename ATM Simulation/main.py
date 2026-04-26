from functions import *
print(deposit_money)

def ATM():
    while True:
        print('\nMenu')
        print('1.Deposit Money')
        print('2.Check Balance')
        print('3.Withdraw Money')
        print('4.Bank Statement')
        print('5.Exit\n')

        choice=int(input("Enter your choice:"))
    
        if choice==1:
            deposit_money()
        elif choice==2:
            display_money()
        elif choice==3:
            withdraw_money()
        elif choice==4:
            statement()
        elif choice==5:
            print("Goodbye!")
            break
        else:
            print("Invalid Input")
ATM()