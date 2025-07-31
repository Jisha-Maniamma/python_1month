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
            print(items)
    print()