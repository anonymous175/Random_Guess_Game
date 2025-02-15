import random

rand = random.randint(1,10)

user = int(input("Enter Your Number: "))
#comp = int(input("Enter your Number: "))

while True: 
    if rand > user:
        print("Computer Wins and Entered: {} ".format(rand))
        break
    elif user > rand:
        print("You Wins and Entered {}".format(user))  
        break  
    elif rand == user:
        print("\nGame Draw... \nComputer Enters {} and You Entres {}".format(rand,user))
        break
    else:
        print("Please enter the Correct Number...")