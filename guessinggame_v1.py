import random

lowest=0
highest=10
answer=random.randint(lowest,highest)

print(f"please guess a value between {lowest} and {highest} ")
guess=int(input())

if guess == answer:
    print("you guessed correctly")
else:
    if guess<answer:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("you guessed correctly")
    else:
        print("sorry you lost")
print(f"the answer was {answer}")
