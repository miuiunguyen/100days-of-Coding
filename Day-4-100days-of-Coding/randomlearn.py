import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

states_of_america = ["Delaware", "Pennsylvania"]
states_of_america[1] = "Pennsilvania" #Change the name
states_of_america.append("Angelaland") #Append to the list
states_of_america.extend({"Anellaland", "Miuiu"}) #Extend the list
num_of_states = len(states_of_america) #count the length of list
print(states_of_america[num_of_states - 1])

