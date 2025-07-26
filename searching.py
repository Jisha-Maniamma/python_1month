shopping_list=["milk","rice","egg","banana"]
found_at=0

for item in shopping_list:
    found_at+=1;
    # print(found_at)
    if item=="egg":
        break
print(f"egg was found at {found_at}")
print("------")
found_at=None
for i in range(len(shopping_list)):
    if shopping_list[i]=="egg":
        found_at=i
        break
print(f"egg was found at {found_at}")
found_at=None
print(found_at!="")

print("------")
found_at=None
to_find="egg"

if to_find in shopping_list:
    print(shopping_list.index(to_find))
