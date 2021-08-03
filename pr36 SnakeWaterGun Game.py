# Snake water gun
import random

lst = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("****************Snake,Water,Gun Game****************\n")
print("Game Rules are:")
print("snake can drink water, gun can shoot snake, and water can damage the gun.")
print("s for snake \t w for water \t g for gun \t and q to quit")

# making the game in while
while no_of_chance < chance:
    _input = input('\nSnake,Water,Gun:')
    _random = random.choice(lst)

    if _input == "q":
        break
    elif _input == _random:
        print("Tie Both 0 point to each \n ")

    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")

    else:
        print("you have input wrong \n")
        no_of_chance = no_of_chance - 1

    print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")
print(f"Out of {no_of_chance} times, You won {human_point} times and Computer won {computer_point} times and {no_of_chance-human_point-computer_point} times match Tie")

print("The overall result is:")
if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")
