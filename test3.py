#you have the guess number and you want computer to guess
import random

my_guess=3
high=10
low=0
print(f"this game please select a number between {low} and {high} and the computer will make guess!")
# computer_guess=random.randint(low,high)
computer_low=low
computer_high=high

while True:
    computer_guess=computer_low+(computer_high-computer_low)//2
    direction=input(f"my guess is {computer_guess}, do i need to guess low 'l' or high 'h' or am i correct 'o'")
    if direction=='l':
        computer_low=computer_guess
    elif direction == 'h':
        computer_high=computer_guess
    elif direction == 'o':
        print("yeah! i won!")
        break
    else:
        print("invalid input! type 'l'/'h'/'o'")
        continue
