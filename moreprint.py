name="jisha"
age=10
print(name,age,"hello",2020)
print(name,age,"hello",2020,sep=", ")

menu = [
    ["egg", "chicken"],
    ["spam", "egg"],
    ["bacon", "egg"],
    ["egg", "cheese", "bacon", "spam"],
    ["bacon", "egg", "spam", "spam"]
]
for item in menu:
    for items in item:
        if items!="spam":
            print(items,end=", ")
    print()