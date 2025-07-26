shopping_list=["milk","rice","egg","banana"]

for item in shopping_list:
    if item!="egg":
        print("bug "+item)

print(".......")

for item in shopping_list:
    if item=="egg":
        continue
    print("bug "+item)

print(".......")
for item in shopping_list:
    if item=="egg":
        break
    print("bug "+item)