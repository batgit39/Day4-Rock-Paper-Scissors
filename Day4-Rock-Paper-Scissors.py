import random
art = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
attributes = ["rock", "paper", "scissors"]

print("Welcome to the game! We're gonna play Rock Paper Scissors")
#print(rock + paper + scissors)

users_choice = int(input("enter your choice:\nFor Rock press-1\nFor Paper press-2\nFor Scissors press-3\n"))
users_choice -= 1
print("You chose:" + art[users_choice])
users_choice = attributes[users_choice]


int_computers_choice = random.randint(0,2)
computers_choice = attributes[int_computers_choice]
print("Computer chose:" + art[int_computers_choice])



if(users_choice == "rock"):
    if (computers_choice == "scissors"):
        print("You won! Rock breaks Scissors")
    elif(computers_choice == "paper"):
        print("You lost! Paper covers Rock")
    else:
        print("It's a Tie")

elif(users_choice == "paper"):
    if (computers_choice == "rock"):
        print("You won! Paper covers Rock")
    elif(computers_choice == "scissors"):
        print("You lost! Scissors cut Paper")
    else:
        print("It's a Tie")
   
elif(users_choice == "scissors"):
    if (computers_choice == "paper"):
        print("You won! Scissors cut Paper")
    elif(computers_choice == "rock"):
        print("You lost! Rock breaks Scissors")
    else:
        print("It's a Tie")
else:
    print("wrong input please try again")

