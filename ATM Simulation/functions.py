account=[]
withdrawn_money=[]

def total():
    balance=0
    for i in account:
        balance+=i
    return balance

def deposit_money():
    try:
        amount=float(input("Enter amount:"))
        if amount>0:
            account.append(amount)
            print(f"{amount} credited to your account.")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Amount should be in number.")

def display_money():
    if len(account)==0:
        print("Zero Balance.")
    else:
        total=0
        for i in account:
            total+=i
        print(f"Total balance={total}")

def withdraw_money():
    try:
        amount=float(input("Enter amount:"))
        balance=total()
        if amount>0:
            if amount<= balance:
                withdrawn_money.append(amount)
                print(f"{amount}debited from your account")
                account.append(-amount)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid Amount")
    except ValueError:
        print("Amount should be in number.")

def statement():
    for i in account:
        if i>0:
            print(f"Deposited-{i}")
        else:
            print(f"Withdrawn-{abs(i)}")
    balance=total()
    print(f"\nTotal balance-{balance}")

