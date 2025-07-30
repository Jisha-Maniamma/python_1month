grocerry_avaiable=["pen","pencil","book","erraser","mouse","white paper"]

indexes=[]
for i in range(1,len(grocerry_avaiable)+1):
    indexes.append(str(i))

print(indexes)
my_choice="-1"
my_list=[]

while my_choice!="0":
    print(f"->{my_choice} ")

    if my_choice in indexes:
        item_selected=grocerry_avaiable[int(my_choice)-1]
        # if my_list.count(item_selected)>0:
        #     print("list already has this item")
        if item_selected in my_list:
            print("list already has this item")
            print(f"do you want to remove {item_selected} alraedy in your cart, type 'y' or 'n' otherwise if so")
            choice=input().casefold()
            if choice=="y":
                my_list.remove(item_selected)


        else:
            my_list.append(item_selected)
            print(f"added {item_selected}")


    else:
        print("The available items are:")
        for index, item in enumerate(grocerry_avaiable):
            print(f"{index + 1}. {item.capitalize()}")
        print("you can choose 0 to exit")

    my_choice = input("you choice is: ")
    if not my_choice.isnumeric():
        print(f"{my_choice} is not valid value")
else:
    print(f"items in you cart are {my_list}")