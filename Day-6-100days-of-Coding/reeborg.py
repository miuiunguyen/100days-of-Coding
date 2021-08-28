def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():  
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

#using while loop
number_of_hurders = 6
while number_of_hurders > 0:
    jump()
    number_of_hurders -=1
    print(number_of_hurders)