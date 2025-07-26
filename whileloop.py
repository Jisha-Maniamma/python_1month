for i in range(10):
    print(f"i is now {i}")

print(f"--{i}--")

i=0
while i<10:
    print(f"i is {i}")
    i+=1

aguess_direction=["east","west","south","north"]
guess_to_exit_game=""
while guess_to_exit_game not in aguess_direction:
    guess_to_exit_game=input("guess another direction ")
print("you can exit this game now")