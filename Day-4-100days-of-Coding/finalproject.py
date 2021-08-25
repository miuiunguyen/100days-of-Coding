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
you_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choose_list = [rock, paper, scissors]
final_you_choose = choose_list[you_choose]
print(final_you_choose)

import random
random_choose = random.randint(0, 2)
final_computer_choose = choose_list[random_choose]
print(f"Computer choose:")
print(final_computer_choose)

if you_choose > 2 or you_choose < 0: 
  print("You typed an invalid number, you lose!") 
elif you_choose == 0 and random_choose == 2:
  print("You win!")
elif random_choose == 0 and you_choose == 2:
  print("You lose")
elif random_choose > you_choose:
  print("You lose")
elif you_choose > random_choose:
  print("You win!")
elif random_choose == you_choose1:
  print("It's a draw")
