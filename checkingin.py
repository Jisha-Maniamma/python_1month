parrot="tattama"

letter=input("enter character ").casefold()


if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("no match")