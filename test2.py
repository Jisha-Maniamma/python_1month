#let the computer fix the number and let me guess
import random

low=0
high=10
computer_guess=random.randint(low,high)
print(computer_guess)

my_low=low
my_high=high
count=0

my_guess=-1

while my_guess!= computer_guess:
    my_guess=int(input(f"enter a value between {low} and {high}"))
    count+=1
    if my_guess>computer_guess:
        my_high=my_guess
        print("this guessed value is a higher value ")
    elif my_guess<computer_guess:
        my_low=my_guess
        print("this guessed value is a lower value ")
    else:
        print(f"you found the number {computer_guess}! in you attempt {count}")
        break


# else:
#     print(f"you found the number {computer_guess}! in you attempt {count}")