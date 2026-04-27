import random
options=['Stone','Paper','Scissor']
def stone():
    c=random.choice(options)
    print("Opponent",c)
    if c=='Stone':
        print("Tied!🤐")
    elif c=='Paper':
        print("You Lost!🥺")
    else:
        print("You Won!😏")

def paper():
    c=random.choice(options)
    print("Opponent-",c)
    if c=='Stone':
        print("You Won!😏")
    elif c=='Paper':
        print("Tied!🤐")
    else:
       print("You Lost!🥺")
       
def scissor():
    c=random.choice(options)
    print("Opponent",c)
    if c=='Stone':
       print("You Lost!🥺")
    elif c=='Paper':
       print("You Won!😏")
    else:
       print("Tied!🤐")
