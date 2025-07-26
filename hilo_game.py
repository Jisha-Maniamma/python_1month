low = 1
high = 1000
print(f"please think of a number between {low} and {high}")
input("Press ENTER to start ")
guess_count = 0

while low!=high:
    print(f"guessing in the range {low} and {high}")
    computers_new_guess = low+ (high - low) // 2
    print(f"my guess is {computers_new_guess}")
    instruction = input(f"my guess is {computers_new_guess}, should i guess highor low if so enter 'h'"
                        f", or 'l', if i am correct enter 'c' ")
    if instruction=='h':
        low=computers_new_guess+1
    elif instruction=='l':
        high=computers_new_guess-1
    elif instruction=='c':
        print("I got it")
        break
    else:
        print("print correct instruction either 'l','h' or'c' ")
else:
    print(f"i guessed the number {computers_new_guess}  at attempt {guess_count}")

