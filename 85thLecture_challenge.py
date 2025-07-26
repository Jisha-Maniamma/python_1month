text="enter an activity of your choice\n" \
     "1.swimming\n" \
     "2.learning python\n" \
     "3.cuscling\n" \
     "4.dancing \n"

choicee=""
while choicee!="0":
    print(text)
    choicee = input()
    print("choice is ", choicee)

    if choicee in "1234":
        print(f"you chose {choicee}")
        break
    elif choicee not in "1234":
        print("enter a valid option")


else:
    print("exiting as you chose 0")