import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('''Rules to play:
      Rock wins against scissors.
      Scissors win against paper.
      Paper wins against rock.\n''')

#Storing ASCII images in to a list
game_images = [rock, paper, scissors]
#Asking for the user choice
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

#if user enter an invalid number i.e other than 0,1,2
if user_choice >=3 or user_choice < 0:
  print("You typed an invalid number, you lose!")

#if user enter's the valid number
else:
  #print the ASCII code against user inpput
  print(game_images[user_choice])
  #generation a random number from computer
  computer_choice = random.randint(0,2)
  print(f"Computer chose:")
  #ASCII code for computer choice
  print(game_images[computer_choice])
  #Rock wins against scissors.
  if user_choice == 0 and computer_choice ==2:
    print("You win!")
  #Rock wins against scissors.
  elif computer_choice == 0 and user_choice ==2:
    print("You lose.")
  #Rock wins against scissors and paper.
  elif computer_choice > user_choice:
    print("You lose.")
  #Rock wins against scissors and paper.
  elif user_choice > computer_choice:
    print("You Win!")
  #Draw if both select the same choice.
  elif computer_choice == user_choice:
    print("It's a draw.")