import random
options=['Stone','Paper','Scissor']
c=random.choice(options)
def stone():
    if c=='Stone':
        print("Tied!🤐")
    elif c=='Paper':
        print("You Lost!🥺")
    else:
        print("You Won!😏")

def paper():
    if c=='Stone':
        print("You Won!😏")
    elif c=='Paper':
        print("Tied!🤐")
    else:
       print("You Lost!🥺")
       
def scissor():
    if c=='Stone':
       print("You Lost!🥺")
    elif c=='Paper':
       print("You Won!😏")
    else:
       print("Tied!🤐")
