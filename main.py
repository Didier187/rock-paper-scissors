import random
# 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# 1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# 2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input("rock, paper, scissors\n"))
computer_choice = random.randint(0,2)


if(user_input == computer_choice):
  if user_input == 0:
    print(f'you both chose {user_input}\n')
    print(rock)
    print("it\'s a tie")
  elif user_input ==1:
    print(f'you both chose {user_input}\n')
    print(paper)
    print("it\'s a tie")
  elif user_input == 2:
    print(f'you both chose {user_input}\n')
    print(scissors)
    print('it\'s a tie')
  elif user_input < 0 or user_input >2:
    print('number has to be between 0 and 2 inclusive')
else:
  # scissors wins
  if(computer_choice == 2 and user_input == 1):
    print("computer wins")
    print(f"computer: \n {scissors}")
    print(f"user: \n {paper}")
  elif(user_input == 2 and computer_choice == 1):
    print("you  win")
    print(f"user: \n {scissors}")
    print(f"computer: \n {paper}")
  # rock wins
  elif( computer_choice == 0 and user_input == 2):
    print("computer wins")
    print(f"computer: \n {rock}")
    print(f"user: \n {scissors}")
  elif(user_input == 0 and computer_choice == 2):
    print("you win")
    print(f"user: \n {rock}")
    print(f"computer: \n {scissors}")
  # paper Wins 
  elif(computer_choice == 1 and user_input == 0):
    print("computer wins")
    print(f"computer: \n {paper}")
    print(f"user: \n {rock}")
  elif(user_input == 1 and computer_choice == 0):
    print("you win")
    print(f"user: \n {paper}")
    print(f"computer: \n {rock}")
  elif user_input < 0 or user_input >2:
    print('number has to be between 0 and 2 inclusive')