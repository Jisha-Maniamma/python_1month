# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
# Zero is considered divisible by everything (zero should not appear in the output).

for i in range(21):
    if i%3!=0 or i%5!=0:
        print(i)

print("---")

for i in range(21):
    if i%3==0 or i%5==0:
        continue
    print(i)
