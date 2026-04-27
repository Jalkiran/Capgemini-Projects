
def menu():
    while True:
        print("\nMenu")
        print("1.Stone")
        print("2.Paper")
        print("3.Scissor")
        print("4.Exit\n")

        try:
            choice=int(input("Enter your choice:"))
        except:
            print("Invalid input")
            continue

        if choice==1:
            pass
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            print("GoodBye!")
            break
        else:
            print("Invalid Input")
menu()