import random

lowest=0
highest=1000
answer=random.randint(lowest+1,highest)

print(f"please guess a value between {lowest+1} and {highest} ")
guess = int(input())
count=0

while lowest!=highest and count<5:
    count+=1
    print(f"your {count} guess, {5-count} more to go")
    if guess==0:
        print("exiting the game ")
        break
    elif guess == answer:
        print("you guessed correctly")
        break
    else:
        if guess < answer:
            print("guess higher")
        else:
            print("guess lower")
        guess = int(input())
        # continue

else:
    print(f"the answer was {answer}") #TODO: remove after testing
    print(f"i guesed it at {count}")




